from obj.PersonalInfo.PersonalInfo import PersonalInfo

import unittest

class Test_Person(unittest.TestCase):
    person = None

    def test_person(self):
        test_person_name = "test_person"
        test_person_serial = "0100000000"
        self.person = PersonalInfo(test_person_name, test_person_serial)
        self.assertIsNotNone(self.person)
        self.assertIsNotNone(self.person.get_name())
        self.assertIsNotNone(self.person.get_serial())
