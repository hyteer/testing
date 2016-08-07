from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://www.ifcld.com')

@app.route('/test')
def test():
    return 'Test....'

@app.route('/bad')
def bad():
    return 'Bad request.',400

if __name__ == '__main__':
    app.run(debug=True,port=8000)