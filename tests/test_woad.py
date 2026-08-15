import unittest

import woad


class Test_woad(unittest.TestCase):

    def test_version(self):

        self.assertEqual('0.0.0', woad.__version__)
