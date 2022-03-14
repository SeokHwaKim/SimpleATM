from modules.Mod_Card.Mod_Card import Mod_Card
from modules.Mod_Account.Mod_Account import Mod_Account

import unittest
import json
import os

class Test_Mod_Account(unittest.TestCase):
    card = None
    account = None

    mod_card = None
    mod_account = None

    def test_mod_card_init(self):
        self.mod_card = Mod_Card()

    def test_card_init(self):
        self.test_mod_card_init()
        with open("{}\\test_data\\cardData.json".format(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))) as f:
            card_data = json.load(f)
        f.close()
        self.mod_card.read_card(card_data)
        self.card = self.mod_card.get_card()

    def test_account_init(self):
        self.test_card_init()
        self.mod_account = Mod_Account(self.card)
        self.mod_account.load_account(self.card.get_card_serial())

    def test_choice_account_true(self):
        self.test_account_init()
        self.assertTrue(self.mod_account.choice_account(1))

    def test_choice_account_false(self):
        self.test_account_init()
        self.assertFalse(self.mod_account.choice_account(999))

