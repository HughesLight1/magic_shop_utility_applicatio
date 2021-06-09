from flask import render_template, request, Blueprint, redirect
import repositories.alchemist_repository as alchemist_repository
import repositories.item_repository as item_repository
from models.alchemist import Alchemist


alchemist_blueprint = Blueprint('alchemist', __name__)


#INDEX

@alchemist_blueprint.route("/alchemists")
def alchemists():
    alchemists = alchemist_repository.select_all()
    return render_template('alchemists/index.html', alchemists=alchemists)

# GET a life
@alchemist_blueprint.route("/alchemists/new")
def new():
    return render_template("alchemists/new.html")


# POST a letter to yourself, pretend you have friends.
@alchemist_blueprint.route("/alchemists/new", methods = ['POST'])
def create_alchemist():
    name = request.form['name']
    email = request.form['email']
    status = 'active'
    alchemist =(name, email, status)
    alchemist_repository.save(alchemist)
    return redirect('/alchemists')

# SHOW the world what you are made of, mainly water, you are essentially a cucumber with issues.
@alchemist_blueprint.route("/alchemists/<id>/edit")
def show_alchemist(id):
    alchemist = alchemist_repository.select(id)
    items = item_repository.select_all_by_alchemist(id)
    return render_template('alchemists/show.html', alchemist=alchemist, items=items)

# EDIT every picture you post to your antisocial media you phony!
@alchemist_blueprint.route("/alchemists/<id>/edit")
def edit_alchemist(id):
    alchemist = alchemist_repository.select(id)
    return render_template('alchemists/edit.html', alchemist=alchemist)

# UPDATE 
@alchemist_blueprint.route("/alchemists/<id>", methods = ['POST'])
def update_alchemist(id):
    name = request.form['name']
    email = request.form['email']
    status = request,form.getlist('status')
    print(status)
    if status == []:
        status = 'inactive'
    else:
        status = 'active'
    alchemist = Alchemist(name, email, status, id)
    alchemist_repository.update(alchemist)
    return redirect('/alchemists')




