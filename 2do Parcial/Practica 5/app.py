# app.py es el lugar donde se realizará toda la configuración del servidor

# importacion de flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# se declara app y se asigna un nombre, es decir, es la inicialización del servidor Flask
app = Flask(__name__)
# se establece la configuracion para host
app.config['MYSQL_HOST']="localhost"
# se establece el usuario que se utilizara
app.config['MYSQL_USER']="root"
# se establece la contraseña del usuario que se utilizara
app.config['MYSQL_PASSWORD']=""
# se establece la conexion a la base de datos que se utilizara
app.config['MYSQL_DB']="dbflask"

app.secret_key='mysicretkey'

mysql= MySQL(app)

# se declaró la ruta
# se declaró la ruta Index, o la ruta principal, http://localhost:5000
# la ruta se compone por el nombre de la ruta y el nombre de la funcion

@app.route('/')
#si la ruta existe, regrela index
def index():
    return render_template('index.html')


# para poder ejecutar esta funcion, en el link se le agrega /guardar
@app.route('/guardar', methods=['POST'])

def guardar():
    if request.method == 'POST':
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        #print(titulo, artista, anio)
        
        #variable de tipo cursor para almacenar la informacion
        CS= mysql.connection.cursor()
        # es el query que se ejecutará para ingresar los datos en la base de datos
        CS.execute('insert into Albums (titulo, artista, anio) values(%s, %s, %s)',(Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
        
    flash('Album agregado correctamente')
    return redirect(url_for('index'))


# para poder ejecutar esta funcion, en el link se le agrega /eliminar
@app.route('/eliminar')
def eliminar():
    return "Se eliminó el album de la BD"


# ejecucion
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
    
