
DDD - Final Proyect
=================
## Propósito del proyecto
Como proposito del trabajo final de nuestro procceding tenemos el  de facilitar el acceso a la información de eventos relacionados a la semana de la computacion dirigido a los estudiantes universitarios. Así como incentivarlos y ayudarlos a su registro e inscripcion en concurso en el que desen participar, ademas de poder programar su horario de asistencia a las charlas de distinguidos ponenetes.

## Funcionalidades
En primer lugar se tienen wireframes de cada pestaña: Inicio, Nosotros, Servicio, Actividad. Los cuales cada uno nos lleva a conocer mas sobre el proyecto.

## Buenas Practicas - Codigo Legible
**Lenguaje**: <br>
La documentacion, la cual se definiria mas adelante, esta en ingles. Asi para lograr un orden e impecabilidad en el proyecto. <br>
```
    class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80))
    institution = db.Column(db.String(100))
    
    
```
```
    class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')
```
**Documentacion de codigo**: <br>
Cada una de nuestras funciones esta ordenada de tal manera que esta sea facilmente entendida por terceros. A continuacion un fragmento ejemplificando el enunciado anterior. <br>
```
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
```
**Modularidad**: <br>
Cada fragmento del codigo ejerce una sola funcion; teniendo el cuenta que utilizamos el framework de Flask, la modularidad y flexibilidad es necesaria. Todo ello permite tambien a la resolucion de errores de forma sencilla, sin comprometer la integridad del resto del proyecto. <br>
```
{% extends "bootstrap/base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}
Login
{% endblock %}

{% block styles %}
{{super()}}
<link rel="stylesheet" href="{{ url_for('static',filename='css/style_02.css') }}">
{% endblock %}

{% block content %}
    <div class="container">

      <form class="form-signin" method="POST" action="/login">
        <h2 class="form-signin-heading">Login</h2>
        {{ form.hidden_tag() }}
        {{ wtf.form_field(form.username) }}
        {{ wtf.form_field(form.password) }}
        {{ wtf.form_field(form.remember) }}
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </form>

    </div> <!-- /container -->
{% endblock %}
```
# SOLID
