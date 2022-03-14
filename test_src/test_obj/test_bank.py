from obj.Bank.Bank import Bank

import unittest


class Test_Bank(unittest.TestCase):
    bank = None

    def test_bank(self):
        test_bank_name = "test_bank"
        test_bank_serial = "0001"
        self.bank = Bank(test_bank_name, test_bank_serial)
        self.assertIsNotNone(self.bank)
        self.assertIsNotNone(self.bank.get_bank_name())
        self.assertIsNotNone(self.bank.get_bank_serial())
        self.assertTrue(self.bank.check_pin("0001"))
