import unittest
from models.item import Item
from models.alchemist import Alchemist

class TestItem(unittest.TestCase):
    def setUp(self):

        self.alchemist = Alchemist('Baron Von Deathlord', 'baronvondeathlord@darklordmail.com', 'active', 7)
        self.item_1 = Item('Begginers Grimoire Of Darklordery', 'Book', 'Begginers book of darklordery made from gypsy tears and broken dreams', 1, 300, 500, self.alchemist, 6657)
        self.item_2 = Item('Jabberwhacky', 'Staff', 'Magic staff which induces insanity in those who are whacked by it....or even just touch it', 0, 250, 400, self.alchemist, 5873)
        self.item_3 = Item('A guide to being social', 'book', 'Chances are if you are a budding darklord then the contents of this book will forever be lost to you, but its worth a shot', 40, 60, 80, self.alchemist, 1111)
        self.item_4 = Item('Possesed Immortal Hamster', 'An immortal hamster seemingly posseed with the spirit of disgrunteled demon...or maybe its just a really agressive russian hamster, those thing always bite', 'begginers book of darklordery made from gypsy tears and broken dreams', 1, 600, 1000, self.alchemist, 6077)
        self.item_5 = Item('Serpent', 'Dagger', 'Enchanted dagger with a curvy blade', 1, 200, 300, self.alchemist, 666)
    

    def test_item_has_name(self):
        self.assertEqual('Begginers Grimoire Of Darklordery', self.item_1.name)
        
    def test_item_has_description(self):
        self.assertEqual('Begginers book of darklordery made from gypsy tears and broken dreams', self.item_1.description)

    def test_item_has_type(self):
        self.assertEqual('Book', self.item_1.type)

    def test_item_has_price(self):
        self.assertEqual(500, self.item_1.price)

    def test_item_has_cost(self):
        self.assertEqual(300, self.item_1.cost)

    def test_item_has_alchemist(self):
        self.assertEqual(7, self.item_1.alchemist.id)
    
    def test_item_has_id(self):
        self.assertEqual(6657, self.item_1.id)

    def test_item_has_quantity(self):
        self.assertEqual(1, self.item_1.quantity)

    def test_low_stock_on_item(self):
        self.assertEqual(True, self.item_1.low_stock())

    def test_low_stock_on_items_at_0_stock(self):
        self.assertEqual(False, self.item_2.low_stock())

    def test_item_is_out_of_stock_true(self):
        self.assertEqual(True, self.item_2.out_of_stock())

    def test_item_is_out_of_stock_false(self):
        self.assertEqual(False, self.item_4.out_of_stock())

    def test_item_total(self):
        self.assertEqual(200, self.item_1.calculate_total())