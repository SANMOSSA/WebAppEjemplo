from flask import Flask,render_template,redirect




app = Flask(__name__)

#Aplicacion web de una calculadora
@app.route('/')
def index():
    return render_template('index.html')

#ruta para cualquier pagina no encontrada
@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


if __name__ == '__main__':
    app.run(threaded=True, port=5000)