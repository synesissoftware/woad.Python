
"""
Minimal ANSI terminal colour codes, for Python.
"""

import os
import threading

__author__      =   'Matt Wilson'
__copyright__   =   'Copyright 2026, Synesis Information Systems'
__credits__     =   [
    'Matt Wilson',
]
__email__       =   'matthew@synesis.com.au'
__license__     =   'BSD-3-Clause'
__maintainer__  =   'Matt Wilson'
__status__      =   'Alpha'
__version__     =   '0.1.0-alpha1'


# Attributes

BLINKING                =   '\033[5m'
BOLD                    =   '\033[1m'


# Reset

RESET                   =   '\033[0m'


# Foreground (standard)

FG_BLACK                =   '\033[30m'
FG_RED                  =   '\033[31m'
FG_GREEN                =   '\033[32m'
FG_YELLOW               =   '\033[33m'
FG_BLUE                 =   '\033[34m'
FG_MAGENTA              =   '\033[35m'
FG_CYAN                 =   '\033[36m'
FG_WHITE                =   '\033[37m'


# Foreground (bright)

FG_BRIGHT_BLACK         =   '\033[90m'
FG_BRIGHT_RED           =   '\033[91m'
FG_BRIGHT_GREEN         =   '\033[92m'
FG_BRIGHT_YELLOW        =   '\033[93m'
FG_BRIGHT_BLUE          =   '\033[94m'
FG_BRIGHT_MAGENTA       =   '\033[95m'
FG_BRIGHT_CYAN          =   '\033[96m'
FG_BRIGHT_WHITE         =   '\033[97m'


# Background (standard)

BG_BLACK                =   '\033[40m'
BG_RED                  =   '\033[41m'
BG_GREEN                =   '\033[42m'
BG_YELLOW               =   '\033[43m'
BG_BLUE                 =   '\033[44m'
BG_MAGENTA              =   '\033[45m'
BG_CYAN                 =   '\033[46m'
BG_WHITE                =   '\033[47m'


# Background (bright)

BG_BRIGHT_BLACK         =   '\033[100m'
BG_BRIGHT_RED           =   '\033[101m'
BG_BRIGHT_GREEN         =   '\033[102m'
BG_BRIGHT_YELLOW        =   '\033[103m'
BG_BRIGHT_BLUE          =   '\033[104m'
BG_BRIGHT_MAGENTA       =   '\033[105m'
BG_BRIGHT_CYAN          =   '\033[106m'
BG_BRIGHT_WHITE         =   '\033[107m'


# Colour policy. The values are the woad 0.3.0 discriminants.

COLOUR_POLICY_AUTO      =   0
COLOUR_POLICY_FORCE     =   1
COLOUR_POLICY_INHIBIT   =   2


_FALSEY = (
    '0',
    'false',
    'never',
    'no',
    'none',
    'off',
)
_TRUEY = (
    '1',
    'always',
    'force',
    'on',
    'true',
    'yes',
)

_lock = threading.Lock()
_determined = False
_policy = COLOUR_POLICY_AUTO
_term_is_dumb = False


def _nonempty(name):
    """The environment value when the variable is set and not empty."""

    if name not in os.environ:
        return None

    value = os.environ[name]

    if value == '':
        return None

    return value


def _listed(value, tokens):
    """Whether value equals one of tokens, ignoring case."""

    folded = value.lower()

    for token in tokens:
        if folded == token:
            return True

    return False


def _policy_from_environment():
    """The colour policy from the current environment, ignoring the cache."""

    value = _nonempty('WOAD_COLOUR')

    if value is None:
        value = _nonempty('WOAD_COLOR')

    if value is not None:
        if _listed(value, _TRUEY):
            return COLOUR_POLICY_FORCE
        elif _listed(value, _FALSEY):
            return COLOUR_POLICY_INHIBIT
        else:
            return COLOUR_POLICY_AUTO

    if _nonempty('NO_COLOR') is not None:
        return COLOUR_POLICY_INHIBIT

    value = _nonempty('CLICOLOR_FORCE')

    if value is not None and value != '0':
        return COLOUR_POLICY_FORCE

    value = _nonempty('FORCE_COLOR')

    if value is not None and value != '0' and value.lower() != 'false':
        return COLOUR_POLICY_FORCE

    value = _nonempty('CLICOLOR')

    if value is not None and value == '0':
        return COLOUR_POLICY_INHIBIT

    return COLOUR_POLICY_AUTO


def _term_is_dumb_from_environment():
    """Whether TERM equals dumb, ignoring case. Absent or empty is not dumb."""

    value = _nonempty('TERM')

    if value is None:
        return False

    return value.lower() == 'dumb'


def _ensure():
    """Fills the cache when it has been dropped. Caller holds _lock."""

    global _determined
    global _policy
    global _term_is_dumb

    if not _determined:
        _policy = _policy_from_environment()
        _term_is_dumb = _term_is_dumb_from_environment()
        _determined = True


def _colour_state():
    """The cached policy and the cached TERM=dumb flag."""

    _lock.acquire()

    try:
        _ensure()

        return _policy, _term_is_dumb
    finally:
        _lock.release()


def _attached(stream):
    """True only when stream.isatty exists and returns true."""

    isatty = getattr(stream, 'isatty', None)

    if not callable(isatty):
        return False

    try:
        return True if isatty() else False
    except Exception:
        return False


def colour_policy():
    """The cached colour policy: 0 auto, 1 force, 2 inhibit.

    An unset or empty variable is absent. Values are not trimmed. The
    first match wins: non-empty WOAD_COLOUR, else non-empty WOAD_COLOR
    (truey forces, falsey inhibits, anything else selects auto and does
    not fall through); non-empty NO_COLOR inhibits; non-empty
    CLICOLOR_FORCE other than the exact bytes 0 forces; non-empty
    FORCE_COLOR other than exact 0 or false (any capitalisation) forces;
    CLICOLOR equal to the exact bytes 0 inhibits; otherwise auto.
    """

    policy, _ignored = _colour_state()

    return policy


def refresh():
    """Drops the cached policy and the cached TERM=dumb flag.

    The next query reads the environment again. On Unix there is no
    console cache to drop.
    """

    global _determined

    _lock.acquire()

    try:
        _determined = False
    finally:
        _lock.release()


def supports_colour(stream):
    """Whether colour should be emitted for this file object.

    Force is yes for every object. Inhibit is no for every object.
    Auto is yes only when the object is a terminal and TERM is not dumb.
    """

    policy, term_is_dumb = _colour_state()

    if policy == COLOUR_POLICY_FORCE:
        return True
    elif policy == COLOUR_POLICY_INHIBIT:
        return False
    else:
        return _attached(stream) and not term_is_dumb


def seq_for(stream, sequence):
    """The sequence when the stream supports colour; otherwise ''."""

    if sequence is None or not supports_colour(stream):
        return ''

    return sequence


__all__ = [
    'BG_BLACK',
    'BG_BLUE',
    'BG_BRIGHT_BLACK',
    'BG_BRIGHT_BLUE',
    'BG_BRIGHT_CYAN',
    'BG_BRIGHT_GREEN',
    'BG_BRIGHT_MAGENTA',
    'BG_BRIGHT_RED',
    'BG_BRIGHT_WHITE',
    'BG_BRIGHT_YELLOW',
    'BG_CYAN',
    'BG_GREEN',
    'BG_MAGENTA',
    'BG_RED',
    'BG_WHITE',
    'BG_YELLOW',
    'BLINKING',
    'BOLD',
    'COLOUR_POLICY_AUTO',
    'COLOUR_POLICY_FORCE',
    'COLOUR_POLICY_INHIBIT',
    'FG_BLACK',
    'FG_BLUE',
    'FG_BRIGHT_BLACK',
    'FG_BRIGHT_BLUE',
    'FG_BRIGHT_CYAN',
    'FG_BRIGHT_GREEN',
    'FG_BRIGHT_MAGENTA',
    'FG_BRIGHT_RED',
    'FG_BRIGHT_WHITE',
    'FG_BRIGHT_YELLOW',
    'FG_CYAN',
    'FG_GREEN',
    'FG_MAGENTA',
    'FG_RED',
    'FG_WHITE',
    'FG_YELLOW',
    'RESET',
    'colour_policy',
    'refresh',
    'seq_for',
    'supports_colour',
]
