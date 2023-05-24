from flask import Flask, render_template, request


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)


@app.route('/guardar-contenido',methods = ['POST'])
def guardarCodigo():
    contenido = request.form.get("contenido")
    return "Contenido guardado correctamente"



