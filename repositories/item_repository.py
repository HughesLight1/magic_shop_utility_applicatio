from db.run_sql import run_sql
from models.item import Item
import repositories.alchemist_repository as alchemist_repository


def save(item):
    sql = "INSERT INTO items (name, type, description,  quantity, cost, price, alchemist_id) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING *"

    values =[item.name, item.type, item.description, item.quantity, item.cost, item.price, item.alchemist.id]

    results = run_sql(sql, values)
    id = results [0]['id'] #took this out to see what would happen June14@02:02 added back in @02:04
    item.id = id
    return item 

def select_all():
    items = []

    sql = 'SELECT * FROM items ORDER by id'
    results = run_sql(sql)

    for row in results:
        alchemist = alchemist_repository.select(row['alchemist_id'])
        item = Item(row['name'], row['type'], row['description'], row['quantity'], row['cost'], row['price'], alchemist, row['id'])
        items.append(item)
    return items

def select_all_by_alchemist(alchemist_id):
    items = []

    sql = "SELECT * FROM items WHERE alchemist_id = %s"
    value = [alchemist_id]
    results = run_sql(sql, value)

    for row in results:

         alchemist = alchemist_repository.select(row['alchemist_id'])
         item = Item(row['name'], row['type'], row['description'], row['quantity'], row['cost'], row['price'], alchemist, row['id'])
         items.append(item)

    return items

def select_all_by_type(type):
    items = []

    sql = "SELECT * FROM products WHERE type = %s"
    value = [type]
    results = run_sql(sql, value)

    for row in results:

        alchemist = alchemist_repository.select(row['alchemist_id'])
        item = Item(row['name'], row['type'], row['description'], row['quantity'], row['cost'], row['price'], alchemist, row['id'])
        items.append(item)

    return item

def select_types():
    types =[]
    sql = "SELECT type FROM items GROUP by type"
    results =run_sql(sql)

    for result in results:
        type = result['type']
        types.append(type)

    return types

def delete_all():
    sql = "DELETE FROM items"
    run_sql(sql)

def select_(id):
    item = None
    sql = "SELECT * FROM items WHERE id = %s"
    value =[id]
    result = run_sql(sql, value[0])

    if result is not None:
        alchemist = alchemist_repository.select(result['alchemist_id'])
        #row error below in Item()June14@03:31
        item = Item(result['name'], result['type'], result['description'], result['quantity'], result['cost'], result['price'], alchemist, result['id'])
    #undefinedvariable row added results inside Item(result['name'] etc)
    return item

def update(item):
    sql = "UPDATE items SET (name, type, description, quantity, cost, price, alchemist_id)=(%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values =[item.name, item.type, item.description, item.quantity, item.cost, item.price, item.alchemist.id, item.id]
    run_sql(sql, values)



    