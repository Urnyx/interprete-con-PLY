from flask import Flask, render_template, request
import json

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar_contenido',methods = ['POST'])

def guardarCodigo():
    data = request.get_json()
    content = data['content']
    # Realiza cualquier procesamiento necesario con el contenido del textarea
    resultado = procesar_contenido(content)
    return resultado

def procesar_contenido(content):
    # Realiza aquí tu lógica de procesamiento del contenido
    # Por ejemplo, puedes simplemente devolver el contenido en mayúsculas
    return content.upper()

if __name__=='__main__':
    app.run(debug=True)
