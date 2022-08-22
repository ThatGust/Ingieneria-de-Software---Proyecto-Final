import glob
import io
import os
import uuid

import numpy as np
from flask import Flask, jsonify, make_response, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    institution = db.Column(db.String(100))

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

@app.route('/')
def index():
    title = "Inicio"

    return render_template('index.html', title=title)

@app.route('/')
def ponent():
    title = "Ponentes"

    return render_template('ponent.html', title=title)

@app.route('/create/', methods=('GET', 'POST'))
def contest():
    title = "Inscripciones"
    if request.method == 'POST':
        name = request.form['title']
        email = request.form['email']
        insti = request.form['insti']
        resume = request.form['resume']

        if not name:
            flash('Se requiere nombre')
        elif not email:
            flash('Se requiere email')
        elif not insti:
            flash('Se requiere institucion')
        elif not resume:
            flash('Se requiere resumen')
    return render_template('contest.html', title=title)

@app.route('/')
def register():
    title = "Regitrarse"

    return render_template('register.html', title=title)

@app.route('/')
def login():
    title = "Login"

    return render_template('login.html', title=title)

db.session.add()
db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)