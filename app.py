from flask import Flask, redirect

from controllers.alchemist_controller import alchemist_blueprint
from controllers.item_controller import item_blueprint

import repositories.item_repository as item_repository
import repositories.alchemist_repository as alchemist_repository



app = Flask(__name__)

app.register_blueprint(alchemist_blueprint)
app.register_blueprint(item_blueprint)


@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect('/items')

if __name__=='__main__':
    app.run(debug=True)