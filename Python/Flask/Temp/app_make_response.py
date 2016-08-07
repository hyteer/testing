from flask import Flask, make_response
app = Flask(__name__)

#### Methods

def set_cookies():
    cooies = {}


#### Routes

@app.route('/')
def index():
    response = make_response('<h2>This response carries a cookie! ')
    response.set_cookie('test','11')
    return response

@app.route('/set')
def set():
    response = make_response('<h2>/set:This response carries a cookie! ')

    response.set_cookie('testset','22')

    print response.headers
    return response

if __name__ == '__main__':
    app.run(debug=True,port=8001)

