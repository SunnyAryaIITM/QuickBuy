from flask import Blueprint, render_template

App = Blueprint('main', __name__)

@App.route('/')
def index_page():
    return render_template("index.html")