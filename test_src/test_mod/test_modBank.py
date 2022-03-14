from modules.Mod_Card.Mod_Card import Mod_Card
from modules.Mod_Bank.Mod_Bank import Mod_Bank

import unittest
import json
import os

class Test_Mod_Bank(unittest.TestCase):
    card = None
    bank = None

    mod_card = None
    mod_bank = None

    def test_mod_card_init(self):
        self.mod_card = Mod_Card()

    def test_card_init(self):
        self.test_mod_card_init()
        with open("{}\\test_data\\cardData.json".format(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))) as f:
            card_data = json.load(f)
        f.close()
        self.mod_card.read_card(card_data)
        self.card = self.mod_card.get_card()

    def test_bank_init(self):
        self.test_card_init()
        self.bank = self.card.get_bank_info()
        self.mod_bank = Mod_Bank(self.card)

    def test_card_in_bank_true(self):
        self.test_bank_init()
        self.assertTrue(self.mod_bank.check_card_in_banks(self.bank.get_bank_serial()))

    def test_card_in_bank_false(self):
        self.test_bank_init()
        self.assertFalse(self.mod_bank.check_card_in_banks("000000000"))

    def test_check_pin(self):
        self.test_bank_init()
        self.assertTrue(self.mod_bank.check_pin("1234"))

