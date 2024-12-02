from flask import Flask, render_template, url_for, request
from datetime import datetime
from flask_cors import CORS
# consumir API json
import json


# Indica que este sera el modulo(archivo) principal de nuestra aplicación
app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:8080","allow_headers":"Access-Allow-Origin"}})
# configuración para cuando se trabaja con formularios y otros casos
# app.config.from_mapping(
#     SECRET_KEY = 'dev'
# )

# Crear mis propios filtros
# Filtros personalizados
# El add_template_filter se utiliza para agregar esta función a los filtros disponibles en las plantillas

# forma 1
# @app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

# forma 2
app.add_template_filter(today, 'today')

# Funciones personalizadas
# forma 1
# @app.add_template_global
def repeat(s,n):
    return s*n
# forma 2
app.add_template_global(repeat, 'repeat')

# Asignar varias rutas a una vista
@app.route('/')
@app.route('/index')
def index():
    # print(url_for('index'))
    # print(url_for('api'))
    # print(url_for('api',name='David',age=23))
    # print(url_for('code', code = 'print("Hola")'))

    with open('db.json', 'r') as file:
        data = json.load(file)

    # Acceder a los datos de los científicos
    cientificos = data[0]['cientificos']

    # Acceder a los datos de Einstein
    # einstein = cientificos['Einstein']

    db = cientificos

    print(db)
    # Enviar datos al template con render_template de flask
    name = 'David'
    # name = None
    friends = ['David','Juan','Ana','Sara']
    date = datetime.now()
    return render_template(
        'index.html', 
        name = name, 
        friends = friends, 
        # asi se haria sin el filtro
        # date = today(date)
        # Así se hace con el filtro
        date = date,
        # aqui tambien puedo enviar funciones como por ejemplo 
        # repeat = repeat
        db = db
        )




# Enviar datos a travez de las rutas con <>
# string @app.route('/hello/<string:name>')
# int @app.route('/hello/<itn:name>')
# float """"
# path """"   (Tiene un manejo mas amplio que el string)
@app.route('/api')
@app.route('/api/<name>')
@app.route('/api/<name>/<int:age>')
@app.route('/api/<name>/<int:age>/<email>')
def api(name = None, age = None, email = None):
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
   
    return render_template('api.html', data = my_data)
    

# Se utiliza escape !!!! para evitar ataques (como ataque de inyecciones), con esto lo que se ingrese en la url se ejecuta como texto plano
from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return f'{escape(code)}'

# Crear formulario con wtform
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    # Los nombres dentro de StringField son los labels del form
    username = StringField("User name", validators=[DataRequired(), Length(min=4, max=10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=10)])
    submit = SubmitField("Register")


# Registrar usuario
# Informo con que metodos voy a trabajar, el metodo GET (viene por defecto) para obtener la plantilla y el metodo POST para enviar los datos del 
# formulario de registro 
@app.route('/auth/register', methods=['GET','POST'])
def register():
    # para acceder a los datos que se estan enviando desde el form
    # print(request.form)
    form = RegisterForm()
    # if request.method == 'POST':
    #     # Estos valores para el diccionario son los name del formulario
    #     username = request.form['username']
    #     password = request.form['password']

    #     # Validación
    #     if len(username) >= 4 and len(username) <= 10 and len(password) >=6 and len(password) <= 10:
    #         return f"Username {username} and password {password}"
    #     else:
    #         error = """El nombre de usuario debe tener entre 4 y 10 caracteres y 
    #         la contraseña debe tener entre 6 y 10 caracteres
    #         """
    #         return render_template('auth/register.html', form = form, error=error)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"Username {username} and password {password}"
    return render_template('auth/register.html', form = form)



if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')