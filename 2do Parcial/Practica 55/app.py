# app.py es el lugar donde se realizará toda la configuración del servidor

# importacion de flask
from flask import Flask

# se declara app y se asigna un nombre, es decir, es la inicialización del servidor Flask
app = Flask(__name__)
# se establece la configuracion para host
app.config['MYSQL_HOST']="localhost"
# se establece el usuario que se utilizara
app.config['MYSQL_USER']="root"
# se establece la contraseña del usuario que se utilizara
app.config['MYSQL_PASSWORD']=""
# se establece la conexion a la base de datos que s eutilizara
app.config['MYSQL_DB']="bdflask"


# se declaró la ruta
# se declaró la ruta Index, o la ruta principal, http://localhost:5000
# la ruta se compone por el nombre de la ruta y el nombre de la funcion

@app.route('/')
#si la ruta existe, regrela index
def index():
    return 'Hola mundo'

# para poder ejecutar esta funcion, en el link se le agrega /guardar
@app.route('/guardar')
def guardar():
    return "Se guardó el album en la BD"


# para poder ejecutar esta funcion, en el link se le agrega /eliminar
@app.route('/eliminar')
def eliminar():
    return "Se eliminó el album de la BD"



# ejecucion
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
    


