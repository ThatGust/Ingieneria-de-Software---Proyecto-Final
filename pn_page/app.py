import glob
import io
from io import BytesIO
import os
import uuid

import numpy as np
from flask import Flask, render_template, redirect, url_for, request, flash, send_file
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))
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
    data = db.Column(db.LargeBinary)

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
    photo = db.Column(db.LargeBinary)

class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    author = db.Column(db.String(60))
    file = db.Column(db.LargeBinary)

class Poster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    author = db.Column(db.String(60))
    file = db.Column(db.LargeBinary)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    institution = StringField('institution', validators=[InputRequired(), Length(max=80)])

def __init__(self, name, email, institution, resume):
   self.name = name
   self.email = email
   self.institution = institution
   self.resume = resume

def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('El usuario ya esta en uso.')

@app.route('/')
def index():
    title = "Inicio"
    return render_template('index.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))

        return '<h1>Contraseña o usuario invalido</h1>'
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, institution=form.institution.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>Nuevo usuario registrado</h1>'

    return render_template('register.html', form=form)

@app.route('/contest', methods=('GET', 'POST'))
def contest():
    title = "Programacion"
    if request.method == 'POST':
      if not request.form['name'] or not request.form['email'] or not request.form['institution'] or not request.form['resume']:
         flash('Llene todos los espacios', 'error')
      else:
         Progra = Program(name=request.form['name'], email=request.form['email'],
            institution=request.form['institution'], resume=request.form['resume'])
         
         db.session.add(Progra)
         db.session.commit()
         
         flash('Forma enviada')
    return render_template('contest.html', title=title)



@app.route('/contest2', methods=('GET', 'POST'))
def contest2():
    title = "Posters"
    if request.method == 'POST':
      file=request.files['data']
      if not request.form['name'] or not request.form['email'] or not request.form['institution'] or not request.files['data']:
         flash('Llene todos los espacios', 'error')
      else:
         file=request.files['data']
         Posterm = Poster_C(name=request.form['name'], email=request.form['email'],
            institution=request.form['institution'], data=file.read())
         
         db.session.add(Posterm)
         db.session.commit()
         
         flash('Forma enviada')
    return render_template('contest2.html', title=title)

@app.route('/download/<upload_id>')
def download(upload_id):
    Posterm = Poster_C.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(Posterm.data), attachment_filename=Posterm.filename, as_attachment=True)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)