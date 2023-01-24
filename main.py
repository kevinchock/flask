from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/flask')
def flask_app():
    return "Esta es una aplicacion de Flask"