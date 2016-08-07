from flask import Flask, request
app = Flask(__name__)


#### Def methods

def do_the_login():
        print "You've posted a login request."
        return "Hi,you've posted a login request."
def show_the_login_form():

    print 'Hello, please login.'
    return '<h2>Hi,please login.</h2>'

#### Def Routes

@app.route('/')
def index():
    return '<h1>Test2:method</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True,port=8000)