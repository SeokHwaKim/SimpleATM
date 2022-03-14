import logging


class Account:
    account_balance = None
    account_serial = None

    def __init__(self, serial):
        self.account_serial = serial

    def set_balance(self, money):
        self.account_balance = money
        if self.account_balance is not None:
            return True
        return False

    def get_balance(self):
        if self.account_balance is None:
            logging.error("Account - balance_is_none")
        return self.account_balance

    def get_serial(self):
        if self.account_serial is None:
            logging.error("Account - serial_is_none")
        return self.account_serial
