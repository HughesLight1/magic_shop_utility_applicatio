from models.alchemist import Alchemist
from models.item import Item

import repositories.alchemist_repository as alchemist_repository
import repositories.item_repository as item_repository

alchemist_repository.delete_all()
item_repository.delete_all()

alchemist1 = Alchemist('Baron Von Deathlord', 'baronvondeathlord@darklordmail.com', 'active')
alchemist2 = Alchemist('Lady Hellcat Bloodclaws', 'hellsno1catlady@darklordmail.com', 'active')
print(alchemist1.name)

alchemist_repository.save(alchemist1)
alchemist_repository.save(alchemist2)

item_1 = Item('Begginers Grimoire Of Darklordery', 'Book', 'Begginers book of darklordery made from gypsy tears and broken dreams', 1, 300, 500, alchemist1)
item_2 = Item('Jabberwhacky', 'Staff', 'Magic staff which induces insanity in those who are whacked by it....or even just touch it', 0, 250, 400, alchemist2)

item_repository.save(item_1)
item_repository.save(item_2)

alchemist2.email= 'hellsno1catlady@darklordmail.com'
alchemist_repository.update(alchemist2)

item_1.quantity = 10
item_repository.update(item_1)