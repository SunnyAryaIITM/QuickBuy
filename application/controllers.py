import re
from flask import Blueprint, render_template, request, flash, redirect

from application.models import User
from application.database import db

App = Blueprint('main', __name__)

@App.route('/')
def index_page():
    return render_template("index.html")

@App.route('/register', methods=["GET", "POST"])
def register():
    if request.method=='POST':
        password = request.form['password']
        email = request.form['email']
        phone_number = request.form['phone_number']
        username = request.form['user_name']
        fullname = request.form['name']
        isAdmin = False
        if username == 'admin' and email == "admin@quickbuy.com":
            isAdmin = True
        user = User(
            password = password,
            email = email,
            phone_number = phone_number,
            username = username,
            fullname = fullname,
            isAdmin = isAdmin
        )
        db.session.add(user)
        db.session.commit()
        return "login page"
    return render_template('register.html')