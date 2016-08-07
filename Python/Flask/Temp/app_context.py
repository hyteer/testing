# encoding:utf-8
from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def index():pass

@app.route('/login')
def login():pass

@app.route('/user/<username>')
def profile(username):pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login',next='/')
    print url_for('profile', username='YTsee')

if __name__ == '__main__':
    app.run(debug=True)

# 定义了动态路由/user/<name>