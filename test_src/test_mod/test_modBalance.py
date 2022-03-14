from modules.Mod_Card.Mod_Card import Mod_Card
from modules.Mod_Account.Mod_Account import Mod_Account
from modules.Mod_Balance.Mod_Balance import Mod_Balance

import unittest
import json
import os

class Test_Mod_Blance(unittest.TestCase):
    card = None
    account = None

    mod_card = None
    mod_account = None
    mod_balance = None

    def test_mod_card_init(self):
        self.mod_card = Mod_Card()

    def test_card_init(self):
        self.test_mod_card_init()
        with open("test_data\cardData.json") as f:
            card_data = json.load(f)
        f.close()
        self.mod_card.read_card(card_data)
        self.card = self.mod_card.get_card()

    def test_accounts_init(self):
        self.test_card_init()
        self.mod_account = Mod_Account(self.card)
        self.mod_account.load_account(self.card.get_card_serial())

    def test_mod_balance_init(self):
        self.mod_balance = Mod_Balance(self.card, self.account)

    def test_account_init(self):
        self.test_accounts_init()
        self.account = self.mod_account.choice_account(2)
        self.test_mod_balance_init()

    def test_deposit_balance(self):
        self.test_account_init()
        self.assertTrue(self.mod_balance.deposit_balance(10000), "Deposit Test")
        self.assertEqual(self.mod_balance.account.get_balance(), 40000, "Deposit Test")

    def test_withdraw_balance_true(self):
        self.test_account_init()
        self.assertTrue(self.mod_balance.withdraw_balance(10000), "Withdraw Test")
        self.assertEqual(self.mod_balance.account.get_balance(), 30000,
                         "Withdraw Test")

    def test_withraw_balance_none(self):
        self.test_account_init()
        self.assertIsNone(self.mod_balance.withdraw_balance(30001))
