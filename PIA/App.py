from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import matplotlib
matplotlib.use('Agg')  # Cambia el backend
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__, static_folder='static')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'evaluaciones'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

def CrearGraficas():
    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT calificacion FROM
                        (
                        SELECT * FROM asesoria ORDER BY idAsesoria DESC LIMIT 5
                        ) AS temp
                        ORDER BY idAsesoria ASC;""")
    datos = cursor.fetchall()

    # Crear la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(datos)
    plt.title('Evaluaciones')
    plt.xticks(np.arange(0, 5, 1))
    plt.xlabel('Número de persona')
    plt.ylabel('Calificación')
        
    # Guardar la gráfica como imagen
    imagen_path = os.path.join('PIA/static', 'grafica1.png')
    plt.savefig(imagen_path)
    plt.close()

    cursor.execute("""SELECT calificacion FROM
                        (
                        SELECT * FROM asesoria ORDER BY idAsesoria DESC LIMIT 10
                        ) AS temp
                        ORDER BY idAsesoria ASC;""")
    datos = cursor.fetchall()

    # Crear la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(datos)
    plt.title('Evaluaciones')
    plt.xticks(np.arange(0, 10, 1))
    plt.xlabel('Número de persona')
    plt.ylabel('Calificación')

    # Guardar la gráfica como imagen
    imagen_path = os.path.join('PIA/static', 'grafica2.png')
    plt.savefig(imagen_path)
    plt.close()

    cursor.execute("""SELECT calificacion FROM
                        (
                        SELECT * FROM asesoria ORDER BY idAsesoria DESC LIMIT 20
                        ) AS temp
                        ORDER BY idAsesoria ASC;""")
    datos = cursor.fetchall()

        # Crear la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(datos)
    plt.title('Evaluaciones')
    plt.xticks(np.arange(0, 20, 1))
    plt.xlabel('Número de persona')
    plt.ylabel('Calificación')
        
    # Guardar la gráfica como imagen
    imagen_path = os.path.join('PIA/static', 'grafica3.png')
    plt.savefig(imagen_path)
    plt.close()

    cursor.execute("SELECT calificacion FROM asesoria")
    datos = cursor.fetchall()

    # Crear la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(datos)
    plt.title('Evaluaciones')
    plt.xlabel('Número de persona')
    plt.ylabel('Calificación')
        
    # Guardar la gráfica como imagen
    imagen_path = os.path.join('PIA/static', 'grafica4.png')
    plt.savefig(imagen_path)
    plt.close()

def CrearGraficaMateria(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT calificacion FROM asesoria WHERE idMaterias = {0}".format(id))
    datos = cursor.fetchall()

    # Crear la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(datos)
    plt.title('Evaluaciones')
    plt.xticks(np.arange(0, 5, 1))
    plt.xlabel('Número de persona')
    plt.ylabel('Calificación')
        
    # Guardar la gráfica como imagen
    imagen_path = os.path.join('PIA/static', 'graficaMateria'+id+'.png')
    plt.savefig(imagen_path)
    plt.close()

def CrearGraficaEstudiante(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT calificacion FROM asesoria WHERE idEstudiantes = {0}".format(id))
    datos = cursor.fetchall()

    # Crear la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(datos)
    plt.title('Evaluaciones')
    plt.xticks(np.arange(0, 5, 1))
    plt.xlabel('Número de evaluación')
    plt.ylabel('Calificación')
        
    # Guardar la gráfica como imagen
    imagen_path = os.path.join('PIA/static', 'graficaEstudiante'+id+'.png')
    plt.savefig(imagen_path)
    plt.close()

def EliminarGraficaEstudiante(id):
    try:
        imagen_path = os.path.join('PIA/static', 'graficaEstudiante'+id+'.png')
        os.remove(imagen_path)
    except:
        pass

def EliminarGraficaMateria(id):
    try:
        imagen_path = os.path.join('PIA/static', 'graficaMateria'+id+'.png')
        os.remove(imagen_path)
    except:
        pass

@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    # Query to check if the table exists
    cursor.execute("""
      SELECT COUNT(*) 
    FROM information_schema.tables 
    WHERE table_schema = %s 
    AND table_name = %s
    """, ('evaluaciones', 'asesoria'))

    table_exists = cursor.fetchone()[0] > 0

    if not table_exists:
        cursor.execute("""
        CREATE TABLE `evaluaciones`.`asesoria` (
        `idAsesoria` INT NOT NULL AUTO_INCREMENT,
        `idEstudiantes` INT NULL,
        `idMaterias` INT NULL,
        `calificacion` INT NULL,
        `comentario` VARCHAR(200) NULL,
        PRIMARY KEY (`idAsesoria`));
    """, )
        
    cursor.execute("""
      SELECT COUNT(*) 
    FROM information_schema.tables 
    WHERE table_schema = %s 
    AND table_name = %s
    """, ('evaluaciones', 'estudiantes'))

    estudiantes_exists = cursor.fetchone()[0] > 0
    
    cursor.execute("""
      SELECT COUNT(*) 
    FROM information_schema.tables 
    WHERE table_schema = %s 
    AND table_name = %s
    """, ('evaluaciones', 'materias'))

    materias_exists = cursor.fetchone()[0] > 0
    
    if estudiantes_exists and materias_exists:
        try:
            cursor.execute("""
            ALTER TABLE `evaluaciones`.`asesoria`
            ADD CONSTRAINT fk_asesoria_estudiante
            FOREIGN KEY (`idEstudiantes`) REFERENCES `evaluaciones`.`estudiantes`(`idEstudiantes`)
            ON DELETE CASCADE
            ON UPDATE CASCADE;
            """) 

            cursor.execute("""
                ALTER TABLE `evaluaciones`.`asesoria`
                ADD CONSTRAINT fk_asesoria_materia
                FOREIGN KEY (`idMaterias`) REFERENCES `evaluaciones`.`materias`(`idMaterias`)
                ON DELETE CASCADE
                ON UPDATE CASCADE;
            """)
        except:
            pass



    imagen1_path = os.path.join('PIA/static', 'grafica1.png')
    imagen2_path = os.path.join('PIA/static', 'grafica2.png')
    imagen3_path = os.path.join('PIA/static', 'grafica3.png')
    imagen4_path = os.path.join('PIA/static', 'grafica4.png')
    if(not os.path.exists(imagen1_path) or not os.path.exists(imagen2_path) or not os.path.exists(imagen3_path) or not os.path.exists(imagen4_path)):   
        CrearGraficas()

    # Obtener las materias existentes en la base de datos
    cursor.execute("SELECT idMaterias, nombre FROM materias ORDER BY nombre;")
    materias = cursor.fetchall()

    cursor.execute("SELECT idEstudiantes, nombre FROM estudiantes ORDER BY nombre;")
    estudiantes = cursor.fetchall()

    return render_template('index.html', imagen1 = '/static/grafica1.png', imagen2 = '/static/grafica2.png', imagen3 = '/static/grafica3.png', imagen4 = '/static/grafica4.png', materias = materias, estudiantes = estudiantes)

@app.route('/estudiantes')
def mostrar_estudiantes():
    cursor = mysql.connection.cursor()
    # Query to check if the table exists
    cursor.execute("""
      SELECT COUNT(*) 
    FROM information_schema.tables 
    WHERE table_schema = %s 
    AND table_name = %s
    """, ('evaluaciones', 'estudiantes'))

    table_exists = cursor.fetchone()[0] > 0

    if not table_exists:
        cursor.execute("""
        CREATE TABLE `evaluaciones`.`estudiantes` (
        `idEstudiantes` INT NOT NULL AUTO_INCREMENT,
        `nombre` VARCHAR(45) NULL,
        `matricula` INT NULL,
        `carrera` VARCHAR(45) NULL,
        `semestre` INT NULL,
        PRIMARY KEY (`idEstudiantes`));
    """, )

    cursor.execute("SELECT * FROM estudiantes ORDER BY nombre;")
    data = cursor.fetchall()
    return render_template('estudiantes.html', estudiantes = data)
    
@app.route('/materias')
def mostrar_materias():
    cursor = mysql.connection.cursor()
    # Query to check if the table exists
    cursor.execute("""
      SELECT COUNT(*) 
    FROM information_schema.tables 
    WHERE table_schema = %s 
    AND table_name = %s
    """, ('evaluaciones', 'materias'))

    table_exists = cursor.fetchone()[0] > 0

    if not table_exists:
        cursor.execute("""
        CREATE TABLE `evaluaciones`.`materias` (
        `idMaterias` INT NOT NULL AUTO_INCREMENT,
        `nombre` VARCHAR(45) NULL,
        PRIMARY KEY (`idMaterias`));
    """, )
    
    cursor.execute("SELECT * FROM materias ORDER BY nombre;")
    data = cursor.fetchall()
    return render_template('materias.html', materias = data)

@app.route('/datos_materia/<string:id>')
def ver_perfil_profesor(id):
    imagenmateria_path = os.path.join('PIA/static', 'graficaMateria'+id+'.png')
    if(not os.path.exists(imagenmateria_path)):
        CrearGraficaMateria(id)
    cur = mysql.connect.cursor()
    cur.execute('SELECT * FROM materias WHERE idMaterias = {0}'.format(id))
    data = cur.fetchone()
    return render_template('datos_materia.html', idMateria = data[0], nombre = data[1], imagen = '/static/graficaMateria'+id+'.png')

@app.route('/perfil_estudiante/<string:id>')
def ver_perfil_estudiante(id):
    imagenestudiante_path = os.path.join('PIA/static', 'graficaEstudiante'+id+'.png')
    if(not os.path.exists(imagenestudiante_path)):
        CrearGraficaEstudiante(id)
    cur = mysql.connect.cursor()
    cur.execute('SELECT * FROM estudiantes WHERE idEstudiantes = {0}'.format(id))
    data = cur.fetchone()
    return render_template('perfil_estudiante.html', idEstudiante = data[0], nombre = data[1], matricula = data[2], carrera = data[3], semestre = data[4], imagen = '/static/graficaEstudiante'+id+'.png')

@app.route('/añadir_materia', methods=['POST'])
def añadir_materia():
    if (request.method == 'POST'):
        nombre = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO materias (nombre) VALUES (%s);", [nombre])
        mysql.connection.commit()
        return redirect(url_for('mostrar_materias'))

@app.route('/añadir_estudiante', methods=["POST"])
def añadir_estudiante():
    if (request.method == 'POST'):
        nombre = request.form['nombre']
        matricula = request.form['matricula']
        carrera = request.form['carrera']
        semestre = request.form['semestre']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO estudiantes (nombre, matricula, carrera, semestre) VALUES (%s, %s, %s, %s);", [nombre, matricula, carrera, semestre])
        mysql.connection.commit()
        return redirect(url_for('mostrar_estudiantes'))
    
@app.route('/añadir_calificacion', methods=["POST"])
def añadir_calificacion():
    if(request.method == "POST"):
        idEstudiantes = request.form['nombre']
        idMaterias = request.form['materia']
        calificacion = request.form['calificacion']
        comentario = request.form['comentario']
        print(idEstudiantes, idMaterias)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO asesoria (idEstudiantes, idMaterias, calificacion, comentario) VALUES (%s, %s, %s, %s);", [idEstudiantes, idMaterias, calificacion, comentario])
        mysql.connection.commit()
        CrearGraficas()
        CrearGraficaEstudiante(idEstudiantes)
        CrearGraficaMateria(idMaterias)
        return redirect(url_for("Index"))

@app.route('/calificaciones')
def calificaciones():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT a.idAsesoria, e.nombre AS estudiante, m.nombre AS materia, a.calificacion, a.comentario
        FROM asesoria a
        INNER JOIN estudiantes e ON a.idEstudiantes = e.idEstudiantes
        INNER JOIN materias m ON a.idMaterias = m.idMaterias;
    """)
    datos = cur.fetchall()
    return render_template('calificaciones.html', datos = datos)

@app.route('/editar_calificacion/<string:id>')
def editar_calificacion(id):
    cur = mysql.connection.cursor()
    cur.execute("""SELECT a.idAsesoria, e.nombre AS estudiante, m.nombre AS materia, a.calificacion, a.comentario
        FROM asesoria a
        INNER JOIN estudiantes e ON a.idEstudiantes = e.idEstudiantes
        INNER JOIN materias m ON a.idMaterias = m.idMaterias where idAsesoria = {0}""".format(id))
    dato = cur.fetchone()
    cur.execute("SELECT * FROM estudiantes")
    estudiantes = cur.fetchall()
    cur.execute("SELECT * FROM materias")
    materias = cur.fetchall()
    return render_template("editar_calificacion.html", dato = dato, estudiantes = estudiantes, materias = materias)

@app.route('/actualizar_calificacion/<string:id>', methods=["POST"])
def actualizar_calificacion(id):
    if(request.method == "POST"):
        idEstudiantes = request.form['nombre']
        idMaterias = request.form['materia']
        calificacion = request.form['calificacion']
        comentario = request.form['comentario']
        cur = mysql.connection.cursor()
        cur.execute("SELECT calificacion FROM asesoria where idAsesoria = {0}".format(id))
        anterior_calificacion = cur.fetchone()
        cur.execute("""UPDATE asesoria
                SET idEstudiantes = %s, idMaterias = %s, calificacion = %s, comentario = %s
                    WHERE idAsesoria = %s""", (idEstudiantes, idMaterias, calificacion, comentario, id))
        mysql.connection.commit()
        if(str(anterior_calificacion[0]) != calificacion):
            CrearGraficas()
        return redirect(url_for("calificaciones"))
    
@app.route('/eliminar_calificacion/<string:id>', methods=["POST"])
def eliminar_calificacion(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM asesoria WHERE idAsesoria = {0}".format(id))
    mysql.connection.commit()
    CrearGraficas()
    return redirect(url_for('calificaciones'))

@app.route('/editar_estudiante/<string:id>')
def editar_estudiante(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM estudiantes where idEstudiantes = {0}".format(id))
    estudiante = cur.fetchone()
    return render_template("editar_estudiante.html", estudiante = estudiante)

@app.route('/actualizar_estudiante/<string:id>', methods=["POST"])
def actualizar_estudiante(id):
    if(request.method == "POST"):
        nombre = request.form['nombre']
        matricula = request.form['matricula']
        carrera = request.form['carrera']
        semestre = request.form['semestre']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE estudiantes
                SET nombre = %s, matricula = %s, carrera = %s, semestre = %s
                    WHERE idEstudiantes = %s""", (nombre, matricula, carrera, semestre, id))
        mysql.connection.commit()
        return redirect(url_for("ver_perfil_estudiante", id = id))
    
@app.route('/eliminar_estudiante/<string:id>', methods=["POST"])
def eliminar_estudiante(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM estudiantes where idEstudiantes = {0}".format(id))
    mysql.connection.commit()
    CrearGraficas()
    EliminarGraficaEstudiante(id)
    return redirect(url_for('mostrar_estudiantes'))

@app.route('/editar_materia/<string:id>')
def editar_materia(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM materias where idMaterias = {0}".format(id))
    materia = cur.fetchone()
    return render_template("editar_materia.html", materia = materia)

@app.route('/actualizar_materia/<string:id>', methods=["POST"])
def actualizar_materia(id):
    if(request.method == "POST"):
        nombre = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute("""UPDATE materias
                SET nombre = %s WHERE idMaterias = %s""", (nombre, id))
        mysql.connection.commit()
        return redirect(url_for("ver_perfil_profesor", id = id))
    
@app.route('/eliminar_materia/<string:id>', methods=["POST"])
def eliminar_materia(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM materias where idMaterias = {0}".format(id))
    mysql.connection.commit()
    CrearGraficas()
    EliminarGraficaMateria(id)
    return redirect(url_for('mostrar_materias'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)