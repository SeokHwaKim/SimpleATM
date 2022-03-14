import logging


class PersonalInfo:
    user_name = ""
    user_serial = ""

    def __init__(self, name, serial):
        self.user_name = name
        if self.user_name is None:
            logging.error("Person - user_name_is_none {}".format(name))
        self.user_serial = serial
        if self.user_serial is None:
            logging.error("Person - user_seiral_is_none {}".format(serial))

    def get_name(self):
        if self.user_name is None:
            logging.error("Person - user_is_none ")
            return None
        return self.user_name

    def get_serial(self):
        if self.user_serial is None:
            logging.error("Person - user_serial_is_none")
            return None
        return self.user_serial
