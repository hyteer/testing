# encoding:utf-8
from flask import request
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1><br><p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s</h1>' % name

@app.route('/test/<args>')
def test(args):
    return '<h1>Test: Your args is:%s'% args

if __name__ == '__main__':
    app.run(debug=True, port=5001)

# 定义了动态路由/user/<name>