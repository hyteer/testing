# encoding:utf-8
'''
This script could be run with commands
'''

from flask import Flask, redirect, abort, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

from DemoLib import Users
from DemoLib.users import load_user

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

#### Def Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',title="User",name=name)

@app.route('/userboot/<name>')
def userboot(name):
    return render_template('user_bootstrap_yt.html',title="User",name=name)

### Jinja2 Templates test
@app.route('/temptest')
def temptest():
    dict1 = {'key':1111,'name':'Tony'}
    list1 = ['aaa','bbb','ccc']
    test = "<h3>a variable</h3>"
    test2 = "another variable"

    obj = load_user(2)
    return render_template('temptest.html',mydict=dict1,mylist=list1,myobj=obj,myintvar=1,test=test,test2=test2,comments=list1)

@app.route('/temptest/<int:id>')
def get_user(id):
    print "Get user id:",id
    user = load_user(id)
    #if not user:
        #abort(404)
    return render_template('temptest_user.html',user=user)

@app.route('/tempext')
def tempextend():
    return render_template('temp_ext.html')

#### Bootstrap Test
@app.route('/bootest')
def bootest():
    dict1 = {'key':1111,'name':'Tony'}
    list1 = ['aaa','bbb','ccc']
    test = "<h3>a variable</h3>"
    test2 = "another variable"
    return render_template('bootest.html')



@app.route('/bad')
def bad():
    return 'Bad request.',400



if __name__ == '__main__':
    manager.run()




