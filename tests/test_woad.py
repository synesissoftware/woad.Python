import unittest

import woad


class Test_woad(unittest.TestCase):

    def test_version(self):

        self.assertEqual('0.0.2', woad.__version__)

    def test_RESET(self):

        self.assertEqual('\033[0m', woad.RESET)

    def test_FG_RED(self):

        self.assertEqual('\033[31m', woad.FG_RED)

    def test_BG_BLUE(self):

        self.assertEqual('\033[44m', woad.BG_BLUE)

    def test_all_codes_are_csi_sgr(self):

        for name in woad.__all__:

            code = getattr(woad, name)

            self.assertTrue(
                code.startswith('\033['),
                name,
            )
            self.assertTrue(
                code.endswith('m'),
                name,
            )
