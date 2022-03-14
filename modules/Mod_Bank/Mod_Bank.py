import logging
import json
import define

class Mod_Bank:
    card = None

    def __init__(self, card):
        self.card = card
        if self.card is not None:
            logging.info("Mod_Bank - card_set_success")
        else:
            logging.error("Mod_Bank - card_set_failed")

    def clear(self):
        self.card = None

    def check_card_in_banks(self, bank_serial):
        # In my thinks, this part must be changed using real Banking API
        # But, now using json data for ATM system verifying.
        with open("test_data/bankCardList.json") as f:
            bank_data = json.load(f)
        if bank_data is None:
            logging.error("Mod_Bank - bank_list_read_failed")
            return False
        bank_dict = bank_data[define.BANK_CARD_LIST_STRING]

        if bank_dict is None:
            logging.error("Mod_Bank - bank_list_load_failed")
            return False

        if bank_serial not in bank_dict:
            logging.error("Mod_Bank - bank_serial_wrong")
            return False

        bank_cards = bank_dict[bank_serial]
        if self.card.get_card_serial() not in bank_cards:
            logging.error("Mod_Bank - bank_card_not_exist")
            return False
        return True

    def check_pin(self, pin_number):
        ret = self.card.check_pin_number(pin_number)
        if ret is True:
            logging.info("Mod_Bank - pin_number_check_success (name: {}, serial: {})".format(
                self.card.get_card_name(), self.card.get_card_serial()
            ), )
            return True
        else:
            logging.error("Mod_Bank - pin_number_check_failed (name: {}, serial: {})".format(
                self.card.get_card_name(), self.card.get_card_serial()
            ), )
            return False
