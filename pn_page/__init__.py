import glob
import io
import os
import uuid

import numpy as np
from flask import Flask, jsonify, make_response, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
''' 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    institution = db.Column(db.String(100))
'''
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    institution = db.Column(db.String(100))
    resume = db.Column(db.String(260))


class Poster_C(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    institution = db.Column(db.String(100))
    resume = db.Column(db.String(260))
''' 
class Ponent_A(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    d_start = db.Column(db.Integer, primary_key=True)
    d_end = db.Column(db.String(50))
    particip = db.Column(db.String(50))
    resume = db.Column(db.String(300))

class Ponent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(300))

    photo = db.Column(db.String(100), unique=True)
    data = db.Column(db.LargeBinary)

class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    author = db.Column(db.String(60))

    archive = db.Column(db.String(100), unique=True)

class Poster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    author = db.Column(db.String(60))

    archive = db.Column(db.String(100), unique=True)
'''
#db.session.add (model object) = CRUD

@app.route('/')
def index():
    title = "Inicio"
    return render_template('index.html', title=title)

@app.route('/contest', methods=('GET', 'POST'))
def contest():
    title = "Programacion"
    if request.method == 'POST':
      if not request.form['name'] or not request.form['email'] or not request.form['insti'] or not request.form['resume']:
         flash('Llene todos los espacios', 'Error')
      else:
         Program = Program(request.form['name'], request.form['email'],
            request.form['insti'], request.form['resume'])
         
         db.session.add(Program)
         db.session.commit()
         
         flash('Forma enviada')
    return render_template('contest.html', title=title)

@app.route('/contest2', methods=('GET', 'POST'))
def contest2():
    title = "Posters"
    if request.method == 'POST':
      if not request.form['name'] or not request.form['email'] or not request.form['insti'] or not request.form['resume']:
         flash('Llene todos los espacios', 'Error')
      else:
         Poster_C = Poster_C(request.form['name'], request.form['email'],
            request.form['insti'], request.form['resume'])
         
         db.session.add(Poster_C)
         db.session.commit()
         
         flash('Forma enviada')
         return redirect(url_for('show_all'))

    return render_template('contest2.html', title=title)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)