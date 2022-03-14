import unittest

from test_src.test_obj.test_card import Test_Card
from test_src.test_obj.test_bank import Test_Bank
from test_src.test_obj.test_person import Test_Person
from test_src.test_obj.test_cardCompany import Test_Company
from test_src.test_mod.test_modCard import Test_Mod_Card
from test_src.test_mod.test_modBank import Test_Mod_Bank
from test_src.test_mod.test_modAccount import Test_Mod_Account
from test_src.test_mod.test_modBalance import Test_Mod_Blance

def test_obj_card():
    suite = unittest.TestSuite()
    suite.addTest(Test_Card("test_set_account"))
    suite.addTest(Test_Card("test_set_card_company"))
    suite.addTest(Test_Card("test_set_person"))
    suite.addTest(Test_Card("test_set_card_bank"))
    return suite

def test_obj_bank():
    suite = unittest.TestSuite()
    suite.addTest(Test_Bank("test_bank"))
    return suite

def test_obj_person():
    suite = unittest.TestSuite()
    suite.addTest(Test_Person("test_person"))
    return suite

def test_obj_company():
    suite = unittest.TestSuite()
    suite.addTest(Test_Company("test_company_set"))
    suite.addTest(Test_Company("test_set_company"))
    return suite

def test_mod_card():
    suite = unittest.TestSuite()
    suite.addTest(Test_Mod_Card("test_read_card_true"))
    suite.addTest(Test_Mod_Card("test_read_card_false"))
    return suite

def test_mod_bank():
    suite = unittest.TestSuite()
    suite.addTest(Test_Mod_Bank("test_card_in_bank_true"))
    suite.addTest(Test_Mod_Bank("test_card_in_bank_false"))
    suite.addTest(Test_Mod_Bank("test_check_pin"))
    return suite

def test_mod_account():
    suite = unittest.TestSuite()
    suite.addTest(Test_Mod_Account("test_choice_account_true"))
    suite.addTest(Test_Mod_Account("test_choice_account_false"))
    return suite

def test_mod_balance():
    suite = unittest.TestSuite()
    suite.addTest(Test_Mod_Blance("test_deposit_balance"))
    suite.addTest(Test_Mod_Blance("test_withdraw_balance_true"))
    suite.addTest(Test_Mod_Blance("test_withraw_balance_none"))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_obj_card())
    runner.run(test_obj_bank())
    runner.run(test_obj_person())
    runner.run(test_obj_company())
    runner.run(test_mod_card())
    runner.run(test_mod_bank())
    runner.run(test_mod_account())
    runner.run(test_mod_balance())
