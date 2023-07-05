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
app.config['MYSQL_DB']="dbflask"

app.secret_key='mysicretkey'

mysql= MySQL(app)

# se declaró la ruta
# se declaró la ruta Index, o la ruta principal, http://localhost:5000
# la ruta se compone por el nombre de la ruta y el nombre de la funcion

@app.route('/')
#si la ruta existe, regrela index
@app.route('/')
def index():
    curSelect = mysql.connection.cursor()
    curSelect.execute('SELECT * FROM Albums')
    consulta = curSelect.fetchall()
    curSelect.close()
    
    return render_template('index.html', listaAlbums=consulta)


# para poder ejecutar esta funcion, en el link se le agrega /guardar
@app.route('/guardar', methods=['POST'])

def guardar():
    if request.method == 'POST':
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        #print(titulo, artista, anio)
        
        # #variable de tipo cursor para almacenar la informacion
        CS= mysql.connection.cursor()
        # # es el query que se ejecutará para ingresar los datos en la base de datos
        CS.execute('insert into Albums (titulo, artista, anio) values(%s, %s, %s)',(Vtitulo, Vartista, Vanio))
        mysql.connection.commit()
        
    flash('Album agregado correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<id>')

def editar(id):
    curEditar = mysql.connection.cursor()
    curEditar.execute('SELECT * FROM Albums WHERE id=%s', (id,))
    consulId = curEditar.fetchone()
    curEditar.close()
    
    return render_template('editarAlbum.html', album=consulId)

@app.route('/actualizar/<id>', methods=['POST'])

def actualizar(id):
    if request.method == 'POST':
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        
        curAct = mysql.connection.cursor()
        curAct.execute('UPDATE Albums SET titulo=%s, artista=%s, anio=%s WHERE id=%s', (Vtitulo, Vartista, Vanio, id))
        mysql.connection.commit()
        
        flash('Album actualizado correctamente')
        return redirect(url_for('index'))


@app.route('/eliminar/<id>')

def eliminar(id):
    curEliminar = mysql.connection.cursor()
    curEliminar.execute('DELETE FROM Albums WHERE id=%s', (id,))
    mysql.connection.commit()
    
    flash('Album eliminado correctamente')
    return redirect(url_for('index'))


# ejecucion
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
    
