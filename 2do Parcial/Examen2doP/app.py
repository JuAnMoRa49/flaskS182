# app.py es el lugar donde se realizará toda la configuración del servidor

# importacion de flask
from flask import Flask, render_template, request, redirect, url_for, flash
# importacion de mysql
from flask_mysqldb import MySQL

# se declara app y se asigna un nombre, es decir, es la inicialización del servidor Flask
app = Flask(__name__)
# se establece la configuracion para host
app.config['MYSQL_HOST']="127.0.0.1"
# se establece el puerto
app.config['MYSQL_PORT']=3306
# se establece el usuario que se utilizara
app.config['MYSQL_USER']="root"
# se establece la contraseña del usuario que se utilizara
app.config['MYSQL_PASSWORD']=""
# se establece la conexion a la base de datos que se utilizara
app.config['MYSQL_DB']="DB_Floreria"

mysql= MySQL(app)

@app.route('/')
def index():
    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM tbFlores')
    consulta = curSelect.fetchall()
    curSelect.close()
    
    return render_template ('index.html', consulta=consulta)


# para poder ejecutar esta funcion, en el link se le agrega /guardar
@app.route('/guardar', methods=['POST'])

def guardar():
    if request.method == 'POST':
        VNombre = request.form['txtNombre']
        VCantidad = request.form['txtCantidad']
        VPrecio = request.form['txtPrecio']
        
        # #variable de tipo cursor para almacenar la informacion
        CS= mysql.connection.cursor()
        # # es el query que se ejecutará para ingresar los datos en la base de datos
        CS.execute('insert into tbFlores (nombre, cantidad, precio) values(%s, %s, %s)',(VNombre, VCantidad, VPrecio))
        mysql.connection.commit()
        
    flash('Se guardó la flor de manera correcta')
    return redirect(url_for('index'))

@app.route('/editar/<nombre>')

def editar(nombre):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM tbFlores WHERE nombre=%s', (nombre,))
    consulNm = curEditar.fetchone()
    curEditar.close()
    
    return render_template('editarFlor.html', album=consulNm)


# ejecucion
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
    