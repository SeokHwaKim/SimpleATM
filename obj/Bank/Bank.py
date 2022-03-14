class Bank:
    bank_name = None
    bank_serial = None

    def __init__(self, bank_name, bank_serial):
        self.bank_name = bank_name
        self.bank_serial = bank_serial

    def get_bank_name(self):
        return self.bank_name

    def get_bank_serial(self):
        return self.bank_serial

    def check_pin(self, pin_number):
        # This function will be checked the right Pin number using Bank API.
        # But, API is unknown
        return True

    def change_pin(self, old_pin, new_pin):
        # First, check if original Pin was right.
        # Second, change Pin number to new_ping using Bank API
        return True

    def connect_bank_API(self):
        # Insert your code for connecting read banking system
        return True