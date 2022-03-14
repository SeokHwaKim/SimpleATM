from obj.CardCompany.CardCompany import CardCompany

import unittest

class Test_Company(unittest.TestCase):
    company = None

    def test_company_init(self):
        self.company = CardCompany()

    def test_company_set(self):
        self.test_company_init()
        self.assertIsNotNone(self.company)

    def test_set_company(self):
        self.test_company_init()
        test_company_name = "test_company"
        test_company_serial = "01"
        self.assertTrue(self.company.set_company(test_company_name, test_company_serial))
        self.assertIsNotNone(self.company.get_company_name())
        self.assertIsNotNone(self.company.get_company_serial())