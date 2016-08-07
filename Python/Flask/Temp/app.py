from flask import Flask, redirect
app = Flask(__name__)

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
    app.run(debug=True,port=8000)