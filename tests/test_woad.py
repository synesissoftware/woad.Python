import os
import unittest

import woad


_MANAGED = (
    'CLICOLOR',
    'CLICOLOR_FORCE',
    'FORCE_COLOR',
    'NO_COLOR',
    'TERM',
    'WOAD_COLOR',
    'WOAD_COLOUR',
)


class _Terminal(object):

    def isatty(self):

        return True


class _File(object):

    def isatty(self):

        return False


def _saved_environment():

    saved = {}

    for name in _MANAGED:
        if name in os.environ:
            saved[name] = os.environ[name]
        else:
            saved[name] = None

    return saved


def _restore_environment(saved):

    for name in _MANAGED:
        value = saved[name]

        if value is None:
            if name in os.environ:
                del os.environ[name]
        else:
            os.environ[name] = value


def _clear_managed():

    for name in _MANAGED:
        if name in os.environ:
            del os.environ[name]


class Test_woad(unittest.TestCase):

    def test_version(self):

        self.assertEqual('0.1.0-alpha1', woad.__version__)

    def test_RESET(self):

        self.assertEqual('\033[0m', woad.RESET)

    def test_BOLD(self):

        self.assertEqual('\033[1m', woad.BOLD)

    def test_BLINKING(self):

        self.assertEqual('\033[5m', woad.BLINKING)

    def test_FG_RED(self):

        self.assertEqual('\033[31m', woad.FG_RED)

    def test_BG_BLUE(self):

        self.assertEqual('\033[44m', woad.BG_BLUE)

    def test_all_codes_are_csi_sgr(self):

        for name in woad.__all__:

            code = getattr(woad, name)

            if not isinstance(code, type(woad.RESET)):
                continue

            self.assertTrue(
                code.startswith('\033['),
                name,
            )
            self.assertTrue(
                code.endswith('m'),
                name,
            )


class Test_policy(unittest.TestCase):

    def setUp(self):

        self._saved = _saved_environment()
        self._terminal = _Terminal()
        self._file = _File()
        _clear_managed()
        woad.refresh()

    def tearDown(self):

        _restore_environment(self._saved)
        woad.refresh()

    def _assign(self, pairs):

        _clear_managed()

        for name, value in pairs:
            os.environ[name] = value

        woad.refresh()

    def _expect(self, attachment, policy, colour):

        stream = self._terminal if attachment else self._file

        self.assertEqual(policy, woad.colour_policy())
        self.assertEqual(colour, woad.supports_colour(stream))

        sequence = woad.seq_for(stream, woad.FG_GREEN)

        if colour:
            self.assertEqual(woad.FG_GREEN, sequence)
        else:
            self.assertEqual('', sequence)

    def test_row_01_none_terminal(self):

        self._assign(())
        self._expect(True, 0, True)

    def test_row_02_none_file(self):

        self._assign(())
        self._expect(False, 0, False)

    def test_row_03_term_dumb(self):

        self._assign((('TERM', 'dumb'),))
        self._expect(True, 0, False)

    def test_row_04_term_DUMB(self):

        self._assign((('TERM', 'DUMB'),))
        self._expect(True, 0, False)

    def test_row_05_woad_colour_1(self):

        self._assign((('WOAD_COLOUR', '1'),))
        self._expect(False, 1, True)

    def test_row_06_woad_color_always(self):

        self._assign((('WOAD_COLOR', 'always'),))
        self._expect(False, 1, True)

    def test_row_07_woad_colour_never(self):

        self._assign((('WOAD_COLOUR', 'never'),))
        self._expect(True, 2, False)

    def test_row_08_woad_colour_auto_terminal(self):

        self._assign((('WOAD_COLOUR', 'auto'),))
        self._expect(True, 0, True)

    def test_row_09_woad_colour_auto_file(self):

        self._assign((('WOAD_COLOUR', 'auto'),))
        self._expect(False, 0, False)

    def test_row_10_woad_colour_purple(self):

        self._assign((('WOAD_COLOUR', 'purple'),))
        self._expect(True, 0, True)

    def test_row_11_no_color_beats_clicolor_force(self):

        self._assign((
            ('CLICOLOR_FORCE', '1'),
            ('NO_COLOR', '1'),
        ))
        self._expect(True, 2, False)

    def test_row_12_clicolor_force(self):

        self._assign((('CLICOLOR_FORCE', '1'),))
        self._expect(False, 1, True)

    def test_row_13_clicolor_force_0_then_clicolor_0(self):

        self._assign((
            ('CLICOLOR', '0'),
            ('CLICOLOR_FORCE', '0'),
        ))
        self._expect(True, 2, False)

    def test_row_14_force_color(self):

        self._assign((('FORCE_COLOR', '1'),))
        self._expect(False, 1, True)

    def test_row_15_force_color_false_then_clicolor_0(self):

        self._assign((
            ('CLICOLOR', '0'),
            ('FORCE_COLOR', 'false'),
        ))
        self._expect(True, 2, False)

    def test_row_16_force_color_FALSE(self):

        self._assign((('FORCE_COLOR', 'FALSE'),))
        self._expect(False, 0, False)

    def test_row_17_force_color_0(self):

        self._assign((('FORCE_COLOR', '0'),))
        self._expect(True, 0, True)

    def test_row_18_clicolor_0(self):

        self._assign((('CLICOLOR', '0'),))
        self._expect(True, 2, False)

    def test_row_19_clicolor_1(self):

        self._assign((('CLICOLOR', '1'),))
        self._expect(True, 0, True)

    def test_row_20_empty_woad_colour_falls_through(self):

        self._assign((
            ('NO_COLOR', '1'),
            ('WOAD_COLOUR', ''),
        ))
        self._expect(True, 2, False)

    def test_row_21_empty_no_color_is_absent(self):

        self._assign((('NO_COLOR', ''),))
        self._expect(True, 0, True)

    def test_row_22_refresh_drops_the_cache(self):

        os.environ['WOAD_COLOUR'] = '1'
        woad.refresh()
        self.assertEqual(1, woad.colour_policy())

        woad.refresh()
        del os.environ['WOAD_COLOUR']
        os.environ['NO_COLOR'] = '1'

        self._expect(True, 2, False)

    def test_seq_for_none_is_empty(self):

        self._assign((('WOAD_COLOUR', '1'),))
        self.assertEqual('', woad.seq_for(self._terminal, None))

    def test_missing_isatty_is_not_a_terminal(self):

        self._assign(())
        self.assertFalse(woad.supports_colour(object()))

    def test_force_ignores_term_dumb(self):

        self._assign((
            ('TERM', 'dumb'),
            ('WOAD_COLOUR', '1'),
        ))
        self._expect(False, 1, True)
