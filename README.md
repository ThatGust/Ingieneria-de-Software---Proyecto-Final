
DDD - Final Proyect
=================
## Propósito del proyecto
Como proposito del trabajo final de nuestro procceding tenemos el  de facilitar el acceso a la información de eventos relacionados a la semana de la computacion dirigido a los estudiantes universitarios. Así como incentivarlos y ayudarlos a su registro e inscripcion en concurso en el que desen participar, ademas de poder programar su horario de asistencia a las charlas de distinguidos ponenetes.


![cs](https://noticias.uneatlantico.es/wp-content/uploads/2017/10/inforuno.jpg)

## Funcionalidades
En primer lugar se tienen wireframes de cada pestaña: Registro, Login, Ponencia, Poster, Programacion Competitiva, los cuales obtienen los datos del usuario que participan en los concursos como de los que no
# Inicio
Dando paso a la presentacion del trabajo final, el inicio se muestra para elegir la opcion que el ususario desee tomar 

### Login
Para login se toma los datos se usuario y del password

### Register
Para esta parte se genera un nuevo usuario con nuevo password que sera parte de la base de datos

### C.Programacion
Realiza el registro para el concurso de programacion competitiva para ser alamacenados en la base de datos 

### Posters
Realiza el registro de nuevos posters para ser alamacenados en la base de datos 

### Logout
Una vez realizado los registros se puede dar la opcion de salir con logout

## Buenas Practicas - Codigo Legible
**Lenguaje**: <br>
La documentacion, la cual se definiria mas adelante, esta en ingles. Asi para lograr un orden e impecabilidad en el proyecto. <br>
```
    ########################################
#Declaracion de las tablas para la base de datos 
########################################

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
```
**Documentacion de codigo**: <br>
Cada una de nuestras funciones esta ordenada de tal manera que esta sea facilmente entendida por terceros. A continuacion un fragmento ejemplificando el enunciado anterior. <br>
```
@app.route('/contest', methods=('GET', 'POST'))
def contest():
    title = "Programacion"
    if request.method == 'POST':
      if not request.form['name'] or not request.form['email'] or not request.form['institution'] or not request.form['resume']: #Si no se encuentra una casilla que el proceso se detenga
         flash('Llene todos los espacios', 'error')
      else:
         Progra = Program(name=request.form['name'], email=request.form['email'], #Se insertan los valores segun el form
            institution=request.form['institution'], resume=request.form['resume'])

         db.session.add(Progra) #Se ejecuta la variable insertando la data
         db.session.commit()
         
         flash('Forma enviada')
    return render_template('contest.html', title=title)

@app.route('/contest2', methods=('GET', 'POST'))
def contest2():
    title = "Posters"
    if request.method == 'POST':
      file=request.files['data']
      if not request.form['name'] or not request.form['email'] or not request.form['institution'] or not request.files['data']: #Si no se encuentra una casilla que el proceso se detenga
         flash('Llene todos los espacios', 'error')
      else:
         file=request.files['data']
         Posterm = Poster_C(name=request.form['name'], email=request.form['email'], #Se insertan los valores segun el form
            institution=request.form['institution'], data=file.read())#Se ejecuta la variable insertando la data

         db.session.add(Posterm) 
         db.session.commit()
         
         flash('Forma enviada')
    return render_template('contest2.html', title=title)
```
**Modularidad**: <br>
Cada fragmento del codigo ejerce una sola funcion; teniendo el cuenta que utilizamos el framework de Flask, la modularidad y flexibilidad es necesaria. Todo ello permite tambien a la resolucion de errores de forma sencilla, sin comprometer la integridad del resto del proyecto. A continuacion un modulo implementado por el presente. <br>
```
{% extends "layout_2.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block head %}
{{ super() }}
{% endblock %}
{% block title %}{{title}}{% endblock %}
{% block content %}
<section class="ftco-section contact-section">
    <div class="container">
        <div class="row d-flex mb-5 contact-info">
            <div class="col-md-12 mb-4">
                <h2 class="h3">Concurso de Posters</h2>
            </div>
            <div class="w-100"></div>
            <div class="col-md-3">
                <p>Para entrar al concurso, porfavor sirvase de llenar la forma que usted desee</p>
            </div>
        </div>
        <div class="row block-9">
            <div class="col-md-6 order-md-last d-flex">
                <form action="{{ request.path }}" class="bg-light p-5 contact-form" enctype="multipart/form-data" method = "post">
                    <div class="form-group">
                        <input type="text" class="form-control" name = "name" placeholder="Nombre">
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control" name = "email" placeholder="Email">
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control" name = "institution" placeholder="Institucion">
                    </div>
                    <div class="form-group">
                        <input type="file" name="data">
                    </div>
                    <div class="form-group">
                        <input type="submit" value="Enviar Formulario" class="btn btn-primary py-3 px-5">
                    </div>
                </form>
            </div>
            <div class="col-md-6 d-flex">
                <div id="map" class="bg-white"></div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
```

## Estilos de Programación aplicados;
1. CODE-GOLF

Tan pocas líneas de código como sea posible

```
@app.route('/')
def index():
    title = "Inicio"
    return render_template('index.html', title=title)

```
2. PIPELINE

Problema mayor descompuesto en abstracciones funcionales. Las funciones, según las Matemáticas, son relaciones de entradas a salidas.
Problema más grande resuelto como una canalización de aplicaciones de funciones

```
@app.route('/download/<upload_id>')
def download(upload_id):
    Posterm = Poster_C.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(Posterm.data), attachment_filename=Posterm.filename, as_attachment=True)
```



3. Programación funcional

Se caracteriza principalmente por permitir declarar y llamar a funciones dentro de otras funciones.


# SOLID

## 1. S-Principio de Resposabilidad Única:
  Este principio tiene como objetivo separar los comportamientos para que, si surgen errores como resultado de su cambio, no         afecten otros comportamientos no relacionados.
```
@app.route('/download/<upload_id>')
def download(upload_id):
    Posterm = Poster_C.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(Posterm.data), attachment_filename=Posterm.filename, as_attachment=True)

@app.route('/ponent')
def ponent():
    title = "Ponentes"
    return render_template('ponent.html', title=title)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
```
**Formato**: <br>
El codigo en su totalidad esta ordenado y formateado en funcion que sea legible. <br>

![Open_Closed](https://github.com/ThatGust/Ingieneria-de-Software---Proyecto-Final/blob/main/image_2022-08-29_141629603.png)
## 2. O-Principio de Abierto-Cerrado:
  Este principio tiene como objetivo extender el comportamiento de una Clase sin cambiar el comportamiento existente de esa Clase.   Esto es para evitar causar errores dondequiera que se use la Clase.
  Para aplicar este ejemplo todas  las clases deben descender de una clase abstracta donde se presenten todos aquellos métodos que   son la base de las respectivas clases.
```
{% extends "layout_2.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block head %}
{{ super() }}
{% endblock %}
{% block title %}{{title}}{% endblock %}
```
## 3. L - Sustitución de Liskov:
  Este principio tiene como objetivo hacer cumplir la coherencia para que la Clase principal o su Clase secundaria se puedan     usar de la misma manera sin errores.
  Para aplicar este ejemplo todas  las clases que sean subtipos de una superclase , y esta misma debe incluir solo aquellos       métodos que comparten ambas subclases sin romper la lógica.
```
Layouts
```
![Open_Closed](https://github.com/ThatGust/Ingieneria-de-Software---Proyecto-Final/blob/main/Capture.PNG)
