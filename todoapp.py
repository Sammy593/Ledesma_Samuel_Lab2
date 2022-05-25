#importar la libreria flask
import time
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods =["GET", "POST"])
#contenedor para llamar a index.html en la ruta principal
#def principal():
 #   return render_template('/index.html')

def principal():
   """ if request.method == "POST":
        #Recibiendo valores del formulario
        nombre = request.form.get("nombre")
        
        #cambiamos a la ruta enviar
        enviar()
       # time.sleep(5)
        #Retornamos respuesta a la ruta index
        return "Tu nombre es: "+nombre"""
   return render_template('/index.html')

@app.route('/enviar')
#contenedor para llamar a enviar.html
def enviar():
    return render_template('/enviar.html')

@app.route('/borrar')
#contenedor para llamar a borrar.html
def borrar():
    return render_template('/borrar.html')


#ejecutar
if __name__ == '__main__':
    app.run(debug=True)