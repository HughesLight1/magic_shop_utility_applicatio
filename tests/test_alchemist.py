import unittest
from models.alchemist import Alchemist
from models.item import Item
# let the tests begin !
class TestAlchemist(unittest.TestCase):
    
    def setUp(self):
        self.alchemist = Alchemist('Baron Von Deathlord', 'baronvondeathlord@darklordmail.com', 'active', 7)

    def test_alchemist_has_name(self):
        self.assertEqual('Baron Von Deathlord', self.alchemist.name)

    def test_alchemist_has_email(self):
        self.assertEqual('baronvondeathlord@darklordmail.com', self.alchemist.email)

    def test_alchemist_has_id(self):
        self.assertEqual(7, self.alchemist.id)

    def test_alchemist_status(self):
        self.assertEqual('active', self.alchemist.status)

