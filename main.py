from flask import Flask, request, make_response, redirect, render_template, abort

app = Flask(__name__)

todos = ['lalal', 'chanchito feliz 2', 'lala2']

@app.errorhandler(404)
def not_found (error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def error_server(error):
    return render_template('500.html', error=error)

@app.route('/')
def error_500():
    abort(500)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }

    return render_template('hello.html', **context)