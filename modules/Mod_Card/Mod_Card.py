from obj.Card.Card import Card
import define

import logging


class Mod_Card:
    card = None

    def __init__(self):
        logging.info("Mod_Card - card_modules_load")

    def get_card(self):
        if self.card is not None:
            return self.card
        return None

    def clear(self):
        self.card = None

    def read_card(self, card_info):
        if self.check_card_info(card_info) is False:
            logging.error("Mod_Card - card_info_read_failed")
            return False

        logging.info("Mod_Card - card_info_read_success (name: {}, serial: {})".format(
            card_info[define.CARD_NAME_STRING], card_info[define.CARD_SERIAL_STRING]))

        self.card = Card(card_info[define.CARD_NAME_STRING], card_info[define.CARD_SERIAL_STRING])

        person_info = self.check_card_person_info(card_info)
        if person_info is None:
            logging.error("Mod_Card - person_info_read_failed")
            return False

        if self.card.set_person(person_info[define.CARD_PERSON_NAME_STRING],
                               person_info[define.CARD_PERSON_SERIAL_STRING]) is False:
            logging.error("Mod_Card - person_info_set_failed")
            return False
        logging.info("Mod_Card - person_info_set_success (name: {}, serial: {})".format(
            person_info[define.CARD_PERSON_NAME_STRING], person_info[define.CARD_PERSON_SERIAL_STRING]))

        bank_info = self.check_card_bank(card_info)
        if bank_info is None:
            logging.error("Mod_Card - bank_info_read_failed")
            return False

        if self.card.set_bank_info(bank_info[define.CARD_BANK_NAME_STRING],
                                 bank_info[define.CARD_BANK_SERIAL_STRING]) is False:
            logging.error("Mod_Card - bank_info_set_failed")
            return False
        logging.info("Mod_Card - bank_info_set_success (name: {}, serial: {})".format(
            bank_info[define.CARD_BANK_NAME_STRING], bank_info[define.CARD_BANK_SERIAL_STRING]))

        company_info = self.check_card_company(card_info)
        if company_info is None:
            return False

        if self.card.set_card_company(company_info[define.CARD_COMPANY_NAME_STRING],
                                   company_info[define.CARD_COMPANY_SERIAL_STRING]) is False:
            logging.error("Mod_Card - company_info_set_failed")
            return False
        logging.info("Mod_Card - comapny_info_set_success (name: {}, serial: {})".format(
            company_info[define.CARD_COMPANY_NAME_STRING], company_info[define.CARD_COMPANY_SERIAL_STRING]))

        logging.info("Mod_Card - card_information_set_success")

        return True

    def check_card_company(self, card_info):
        ret = {}
        if card_info[define.CARD_COMPANY_STRING] is None:
            logging.error("Mod_Card - card_company_read_failed")
            ret = None
        card_company_info = card_info[define.CARD_COMPANY_STRING]

        if card_company_info[define.CARD_COMPANY_NAME_STRING] is None:
            logging.error("Mod_Card - card_company_name_read_failed")
            ret = None
        if card_company_info[define.CARD_COMPANY_SERIAL_STRING] is None:
            logging.error("Mod_Card - card_company_serial_read_failed")
            ret = None

        ret[define.CARD_COMPANY_NAME_STRING] = card_company_info[define.CARD_COMPANY_NAME_STRING]
        ret[define.CARD_COMPANY_SERIAL_STRING] = card_company_info[define.CARD_COMPANY_SERIAL_STRING]
        return ret

    def check_card_bank(self, card_info):
        ret = {}
        if card_info[define.CARD_BANK_STRING] is None:
            logging.error("Mod_Card - card_bank_read_failed")
            ret = None
        card_bank_info = card_info[define.CARD_BANK_STRING]

        if card_bank_info[define.CARD_BANK_NAME_STRING] is None:
            logging.error("Mod_Card - card_bank_name_read_failed")
            ret = None
        if card_bank_info[define.CARD_BANK_SERIAL_STRING] is None:
            logging.error("Mod_Card - card_bank_serial_read_failed")
            ret = None

        ret[define.CARD_BANK_NAME_STRING] = card_bank_info[define.CARD_BANK_NAME_STRING]
        ret[define.CARD_BANK_SERIAL_STRING] = card_bank_info[define.CARD_BANK_SERIAL_STRING]

        return ret

    def check_card_person_info(self, card_info):
        ret = {}
        if card_info[define.CARD_PERSON_STRING] is None:
            logging.error("Mod_Card - card_person_read_failed")
            ret = None
        card_person_info = card_info[define.CARD_PERSON_STRING]

        if card_person_info[define.CARD_PERSON_NAME_STRING] is None:
            logging.error("Mod_Card - card_person_name_read_failed")
            ret = None

        if card_person_info[define.CARD_PERSON_SERIAL_STRING] is None:
            logging.error("Mod_Card - card_person_serial_read_failed")
            ret = None

        ret[define.CARD_PERSON_NAME_STRING] = card_person_info[define.CARD_PERSON_NAME_STRING]
        ret[define.CARD_PERSON_SERIAL_STRING] = card_person_info[define.CARD_PERSON_SERIAL_STRING]
        return ret

    def check_card_info(self, card_info):
        if card_info is None:
            logging.error("Mod_Card - card_data_is_none")
            return False

        if card_info[define.CARD_NAME_STRING] is None:
            logging.error("Mod_Card - card_name_read_failed")
            return False

        if card_info[define.CARD_SERIAL_STRING] is None:
            logging.error("Mod_Card - card_serial_read_failed")
            return False

        return True

    def dump_card(self):
        card_name = self.card.get_card_name()
        card_serial = self.card.get_card_serial()

        bank_info = self.card.get_bank_info()
        if bank_info is None:
            logging.error("Mod_Card - card_dump_bank_read_failed")
            return False

        bank_name = bank_info.get_bank_name()
        bank_serial = bank_info.get_bank_serial()

        company_info = self.card.get_company_info()
        if company_info is None:
            logging.error("Mod_Card - card_dump_company_read_failed")
            return False

        company_name = company_info.get_company_name()
        company_serial = company_info.get_company_serial()

        person_info = self.card.get_person()
        if person_info is None:
            logging.error("Mod_Card - card_dump_person_read_failed")
            return False
        person_name = person_info.get_name()
        person_serial = person_info.get_serial()

        print("=====================================")
        print("= CardName : {}".format(card_name))
        print("= CardSerial : {}".format(card_serial))
        print("= Person : {}".format(person_name))
        print("= PersonSerial : {}".format(person_serial))
        print("= BankName : {}".format(bank_name))
        print("= BankSerial : {}".format(bank_serial))
        print("= Company : {}".format(company_name))
        print("= CompanySerial : {}".format(company_serial))
        print("=====================================")
