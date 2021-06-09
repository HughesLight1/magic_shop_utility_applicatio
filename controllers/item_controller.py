from flask import render_template, request, Blueprint, redirect
from models.item import Item
import repositories.item_repository as item_repository
import repositories.alchemist_repository as alchemist_repository

item_blueprint = Blueprint('item',__name__)



#INDEX
@item_blueprint.route("/items")
def index():
    items = item_repository.select_all()
    alchemist = alchemist_repository.select_all()
    types= item_repository.select_types()
    return render_template('index.html', items=items, alchemist=alchemist, types=types)

#SHOW me the money
@item_blueprint.route("/items")
def item(id):
    item = item_repository.select(id)
    return render_template('/items/show.html', item=item)

#CREATE this is for new items
#GET down, down, down, down, down
@item_blueprint.route("/new")
def new_item():
    alchemists = alchemist_repository.select_all
    return render_template("/items/newhtml", alchemists=alchemists)

#CREATE
#POST
@item_blueprint.route("/new", methods = ['POST'])
def create_item():
    name = request.form['name']
    type = request.form['type']
    description =request.form['description']
    quantity = request.form['quantity']
    cost = request.form['cost']
    price = request.form['price']
    alchemist_id = request.form['alchemist']
    alchemist = alchemist_repository.select(alchemist_id)
    item = Item(name, type, description, quantity, cost, price, alchemist)
    item_repository.save(item)
    return redirect('/')

#EDIT
@item_blueprint.route("/items/<id>/edit")
def edit_item(id):
    item = item_repository.select.select(id)
    alchemists = alchemist_repository.select_all()
    return render_template('/items/edit.html', item=item, alchemists=alchemists)

#UPDATE
@item_blueprint.route("/items/<id>", methods=['POST'])
def update_item(id):
    name = request.form['name']
    type = request.form['type']
    description =request.form['description']
    quantity = request.form['quantity']
    cost = request.form['cost']
    price = request.form['price']
    alchemist_id = request.form['alchemist']
    alchemist = alchemist_repository.select(alchemist_id)
    item = Item(name, type, description, quantity, cost, price, alchemist)
    item_repository.save(item)
    return redirect('/')

#SELECT ALL BY TYPE
@item_blueprint.route("/items/types/<type>")
def item_types(type):
    items= item_repository.select_all_by_type(type)
    alchemists = alchemist_repository.select_all()
    return render_template('items/type.html', items =items, alchemists=alchemists)

    

