#importar la libreria flask
from flask import Flask, redirect, request, render_template, url_for
import pickle
app = Flask(__name__, template_folder='templates')

datosF = []
def buscarArchivo():
    try:
        archivo = pickle.load(open("dict.pickle","rb"))
    except:
        pickle.dump(datosF, open("dict.pickle","wb"))
        
buscarArchivo()
# ************************************************************
class Tarea:
    # Constructor de clase
    def __init__(self, id, titulo, correo, prioridad):
        self.titulo = titulo
        self.correo = correo
        self.prioridad = prioridad
        self.id = id
        print('Se ha creado la tarea:',self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.id, self.titulo, self.correo, self.prioridad)
class ListaTareas:
    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.datosF.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.datosF) == 0:
            print("La lista está vacía")
            return
        for p in self.datosF:
            print(p)

    def cargar(self):
        fichero = open('dict.pickle', 'ab+')
        fichero.seek(0)
        try:
            self.datosF = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} tareas".format(len(self.datosF)))

    def guardar(self):
        fichero = open('dict.pickle', 'wb')
        pickle.dump(self.datosF, fichero)
        fichero.close()
# ************************************************************

@app.route('/')
#contenedor para llamar a index.html y los datos registrados en la ruta principal
def index():
    fichero = open('catalogo.pckl', 'ab+')
    fichero.seek(0)
    try:
        self.peliculas = pickle.load(fichero)
    except:
             print("El fichero está vacío")


    return render_template('/index.html', datosF=pickle_out)
#------------------------------------------------------
#                         ENVIAR 
#------------------------------------------------------
@app.route('/enviar', methods =["GET", "POST"])
#contenedor para llamar a enviar.html
def enviar():
    if request.method == 'POST':
        #id, titulo, correo, prioridad
        pickle_abierto = open("dict.pickle","rb")
        pickle_out = pickle.load(pickle_abierto)
        numID = pickle_out.__len__()
        pickle_abierto.close()

        tituloT = request.form['titulo']
        correoT = request.form['correo']
        prioridadT = request.form['prioridad']

        lt = ListaTareas()

        lt.agregar(Tarea(numID, tituloT, correoT, prioridadT))
        lt.mostrar()

        del(lt)

        return redirect(url_for('index'))
#------------------------------------------------------

#------------------------------------------------------
#Controlador para borrar
@app.route('/borrar', methods=['POST'])
#contenedor para llamar a borrar.html
def borrar():
    datosF.clear()
    fichero = open('dict.pickle', 'wb')
    pickle.dump(datosF, fichero)
    fichero.close()
    return redirect(url_for('index'))

#ejecutar
if __name__ == '__main__':
    app.run(debug=True)