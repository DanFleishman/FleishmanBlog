from app import app
from flask import render_template, request
from datetime import datetime


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/photos')
def photos():
    return render_template('photos.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# AdminPanel


@app.route('/admin/auth')
def admin():
    return render_template('admin_auth.html')


@app.route('/admin/create-article', methods=['POST', 'GET'])
def create_article():
    return render_template('create_article.html')


@app.route('/admin/mainpanel')
def mainpanel():
    return render_template('')


# @app.route('/user/<string:name>/<int:id>')
# def user(name, id):
#     return "User Page: " + name + " - " + str(id)
