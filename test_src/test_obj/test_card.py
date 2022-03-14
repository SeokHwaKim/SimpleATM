from obj.Card.Card import Card

import unittest

class Test_Card(unittest.TestCase):
    card = None

    def card_init(self):
        card_name = "test_card"
        card_serial = "1"
        self.card = Card(card_name, card_serial)

    def test_set_card_bank(self):
        self.card_init()
        test_bank_name = "test_bank"
        test_bank_serial = "0001"
        self.assertTrue(self.card.set_bank_info(test_bank_name, test_bank_serial))

    def test_set_person(self):
        self.card_init()
        test_person_name = "test_person"
        test_person_serial = "0001"
        self.assertTrue(self.card.set_person(test_person_name, test_person_serial))

    def test_set_card_company(self):
        self.card_init()
        test_company_name = "test_company"
        test_company_serial = "0001"
        self.assertTrue(self.card.set_card_company(test_company_name, test_company_serial))

    def test_set_account(self):
        self.card_init()
        test_account_serial = "00000000"
        test_account_balance = 50000
        self.assertTrue(self.card.set_account(test_account_serial, test_account_balance))
