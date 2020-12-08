from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask: Hello World from Docker'


@app.route('/api')
def rest_hello_world():
    return '{"id":1,"message":"Flask: Hello World from Docker"}'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/index', methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':

        if request.form['username'] == "ofir":
            return render_template('hello.html')
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html', error=error)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
