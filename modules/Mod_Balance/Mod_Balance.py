import logging


class Mod_Balance:
    card = None
    account = None

    def __init__(self, card, account):
        self.card = card
        if card is None:
            logging.error("Mod_Balance - card_set_failed")
        else:
            logging.info("Mod_Balance - card_set_success")
        self.account = account
        if account is None:
            logging.error("Mod_Balance - account_set_failed")
        else:
            logging.info("Mod_Balance - account_set_success")

    def clear(self):
        self.card = None
        self.account = None

    def dump_account(self):
        if self.account is None:
            logging.error("Mod_Balance - account_is_not_setted")
            return False
        print("=====================================")
        print("= Selected : {}".format(self.account.get_serial()))
        print("= Balance  : {}".format(self.account.get_balance()))
        print("=====================================")

    def deposit_balance(self, money):
        money = int(money)
        remains = self.account.get_balance()
        remains += money
        self.account.set_balance(remains)
        if remains == self.account.get_balance():
            logging.info("Mod_Balance - depoit success (seriral: {}".format(self.account.get_serial()))
            return True
        return False

    def withdraw_balance(self, money):
        money = int(money)
        remains = self.account.get_balance()
        if remains < money:
            logging.error("Mod_Balance - lack of balance (seriral: {}".format(self.account.get_serial()))
            return None
        remains -= money
        self.account.set_balance(remains)
        if remains == self.account.get_balance():
            logging.info("Mod_Balance - withdraw success (seriral: {}".format(self.account.get_serial()))
            return True
        return False