from modules.Mod_Card.Mod_Card import Mod_Card

import unittest
import json
import sys
import os

class Test_Mod_Card(unittest.TestCase):
    mod_card = None

    def test_mod_card_init(self):
        self.mod_card = Mod_Card()

    def test_read_card_true(self):
        self.test_mod_card_init()
        with open("{}\\test_data\\cardData.json".format(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))) as f:
            card_data = json.load(f)
        f.close()
        self.assertTrue(self.mod_card.read_card(card_data))

    def test_read_card_false(self):
        self.test_mod_card_init()
        card_data = None
        self.assertFalse(self.mod_card.read_card(card_data))

