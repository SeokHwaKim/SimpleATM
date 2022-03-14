import logging


class CardCompany:
    company_name = None
    company_serial = None

    def set_company(self, company_name, company_serial):
        self.company_name = company_name
        if self.company_name is None:
            logging.error("Company - company_name_add_failed {}".format(company_name))
            return False
        if self.set_serial(company_serial):
            logging.info("Company - company_add_success {} {}".format(company_name, company_serial))
            return True
        else:
            return False

    def set_serial(self, company_serial):
        self.company_serial = company_serial
        if self.company_serial is not None:
            return True
        logging.error("Company - company_serial_reg_faile {}".format(company_serial))
        return False

    def get_company_name(self):
        return self.company_name

    def get_company_serial(self):
        return self.company_serial
