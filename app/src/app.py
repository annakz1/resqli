from flask import Flask, render_template
from flask import request
import predict

app = Flask(__name__)

model = predict.Model()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':

        prediction = model.predict_our_model(request.form['username'])

        return render_template('index.html', prediction=prediction)
        # if request.form['username'] == "ofir":
        #    return render_template('hello.html')
        # if valid_login(request.form['username'],
        #                request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html')


# @app.route('/')
# def hello_world():
#     return 'Flask: Hello World from Docker'


@app.route('/api')
def rest_hello_world():
    return '{"id":1,"message":"Flask: Hello World from Docker"}'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
