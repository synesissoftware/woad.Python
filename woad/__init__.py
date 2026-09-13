
"""
Minimal ANSI terminal colour codes, for Python.
"""

__author__      =   'Matt Wilson'
__copyright__   =   'Copyright 2026, Synesis Information Systems'
__credits__     =   [
    'Matt Wilson',
]
__email__       =   'matthew@synesis.com.au'
__license__     =   'BSD-3-Clause'
__maintainer__  =   'Matt Wilson'
__status__      =   'Alpha'
__version__     =   '0.0.1'


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
]
