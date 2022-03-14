import logging
import define
import json


class Mod_Account:
    card = None
    accounts = None

    def __init__(self, card):
        self.card = card

    def clear(self):
        self.card = None
        self.accounts = None

    def set_accounts(self, accounts):
        self.accounts = accounts
        if self.accounts is None:
            logging.error("Mod_Account - account_set_failed")
            return False
        return True

    def choice_account(self, account_index):
        account_index -= 1
        accounts = self.card.get_accounts()
        if accounts is None:
            logging.error("Mod_Account - choice_account_account_is_none")
            return False

        accounts_index_list = list(accounts.keys())
        accounts_len = len(accounts_index_list)
        if accounts_len == 0:
            logging.error("Mod_Account - choice_account_account_is_zero")
            return False
        elif accounts_len < account_index:
            logging.error("Mod_Account - choice_account_account_not_in_accounts")
            return False
        return self.card.get_accounts()[accounts_index_list[account_index]]

    def load_account(self, card_serial):
        #In my thinks, this part must be changed using real Banking API
        #But, now using json data for ATM system verifying.
        with open("test_data/bankAccount.json") as bank_file:
            account_data = json.load(bank_file)
        bank_file.close()
        account_list = self.check_account(account_data, card_serial)
        if account_list is None:
            logging.error("Mod_Account - account_info_read_failed")
            return False

        for account_info in account_list:
            if self.card.set_account(account_info[define.ACCOUNT_ACCOUNT_SERIAL_STRING],
                                    account_info[define.ACCOUNT_ACCOUNT_BALANCE_STRING]) is False:
                logging.error("Mod_Account - account_info_set_failed")
                return False
            logging.info("Mod_Account - account_info_set_success (serial: {}, balance: {})".format(
                account_info[define.ACCOUNT_ACCOUNT_SERIAL_STRING],
                account_info[define.ACCOUNT_ACCOUNT_BALANCE_STRING]))
        logging.info("Mod_Account - account_load_success")

        return True

    def check_account(self, bank_data, card_serial):
        ret = {}
        if bank_data[define.ACCOUNT_ACCOUNT_LIST_STRING] is None:
            logging.error("Mod_Account - account_read_failed")
            ret = None
        account_list = bank_data[define.ACCOUNT_ACCOUNT_LIST_STRING]

        if card_serial not in account_list:
            logging.error("Mod_Account - account_is_not_exist")
            ret = None
            return ret

        account_list = account_list[card_serial]
        for account_info in account_list:
            if account_info[define.ACCOUNT_ACCOUNT_SERIAL_STRING] is None:
                logging.error("Mod_Account - card_account_serial_read_failed")
                ret = None
            if account_info[define.ACCOUNT_ACCOUNT_BALANCE_STRING] is None:
                logging.error("Mod_Account - card_account_balance_read_failed")
                ret = None
        if ret is None:
            logging.error("Mod_Account - card_account_read_failed")
            return None

        ret = account_list
        return ret

    def dump_accounts(self):
        accounts = self.card.get_accounts()
        idx = 0
        print("============= Account =============")
        for serial, account in accounts.items():
            idx += 1
            print("= idx : {}".format(idx))
            print("= Account : {}".format(serial))
            print("= Balance : {}".format(account.get_balance()))
            print("=====================================")
