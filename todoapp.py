#importar la libreria flask
#import time
from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__, template_folder='templates')

datosF = []


@app.route('/')
#contenedor para llamar a index.html en la ruta principal
def index():
    return render_template('/index.html', datosF=datosF)

@app.route('/enviar', methods =["GET", "POST"])
#contenedor para llamar a enviar.html
def enviar():
    if request.method == 'POST':
        dato = request.form['nombre']
        datosF.append({'dato':dato})
        return redirect(url_for('index'))

#Controlador para borrar
@app.route('/borrar', methods=['POST'])
#contenedor para llamar a borrar.html
def borrar():
      if request.method == 'POST':
        if datosF == []:
            return redirect(url_for('index'))
        else:
            datosF.clear()
            return redirect(url_for('index'))



#ejecutar
if __name__ == '__main__':
    app.run(debug=True)