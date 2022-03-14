import logging
from obj.PersonalInfo.PersonalInfo import PersonalInfo as Person
from obj.Account.Account import Account
from obj.CardCompany.CardCompany import CardCompany
from obj.Bank.Bank import Bank


class Card():
    card_name = ""
    card_serial = ""
    card_company = CardCompany()
    card_accounts = {}
    card_bank = None
    card_person = None

    def __init__(self, card_name, card_serial):
        self.card_name = card_name
        self.card_serial = card_serial

    def set_bank_info(self, bank_name, bank_serial):
        self.card_bank = Bank(bank_name, bank_serial)
        if self.card_bank is None:
            logging.error("Card - bank_obj_create_failed {} {}".format(bank_name, bank_serial))
            return False
        return True

    def set_person(self, person_name, person_serial):
        self.card_person = Person(person_name, person_serial)
        if self.card_person is None:
            logging.error("Card - person_info_set_failed".format(person_name, person_serial))
            return False
        logging.info("Card - person_info_set_success {} {}".format(person_name, person_serial))
        return True

    def set_card_company(self, company_name, company_serial):
        if self.card_company.set_company(company_name, company_serial):
            logging.info("Card - set_company_success {} {}".format(company_name, company_serial))
            return True
        else:
            logging.error("Card - set_company_failed {} {}".format(company_name, company_serial))
            return False

    def set_account(self, account_serial, account_balance):
        if self.check_account(account_serial):
            self.card_accounts[account_serial] = Account(account_serial)
            if self.card_accounts[account_serial].set_balance(account_balance) is False:
                logging.error("Card - account_balance_set_failed")
                return False
            logging.info("Card - account_add_success (serial:{} balance:{})".format(account_serial, account_balance))
        return True

    def get_person(self):
        if self.card_person is not None:
            return self.card_person
        else:
            logging.error("Card - get_person_failed_person_is_none")
            return None

    def get_card_serial(self):
        return self.card_serial

    def get_card_name(self):
        return self.card_name

    def get_bank_info(self):
        if self.card_bank is None:
            logging.error("Card - get_bank_failed_bank_is_none")
            return None
        else:
            return self.card_bank

    def get_company_info(self):
        if self.card_company is None:
            logging.error("Card - get_company_failed_company_is_none")
            return None
        else:
            return self.card_company

    def get_accounts(self):
        return self.card_accounts

    def clear(self):
        self.card_name = ""
        self.card_serial = ""
        self.card_company = CardCompany()
        self.card_accounts.clear()
        self.card_bank = None
        self.card_person = None

    def check_account(self, account_serial):
        if account_serial in self.card_accounts:
            logging.error("Card - account_add_failed_account_is_exist {}".format(account_serial))
            return False
        else:
            return True

    def check_pin_number(self, card_pin_number):
        if self.get_bank_info() is None:
            logging.error("Card - check_pin_failed_bank_is_none")
            return None
        else:
            return self.card_bank.check_pin(card_pin_number)
