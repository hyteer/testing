from flask import Flask, redirect
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/test')
def test():
    return 'Test....'

@app.route('/red')
def red():
    return redirect('http://www.ifcld.com')

@app.route('/bad')
def bad():
    return 'Bad request.',400

if __name__ == '__main__':
    manager.run()

