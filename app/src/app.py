from flask import Flask, render_template
from flask import request
import predict

app = Flask(__name__)

model = predict.Model()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        product_name = request.form['product']
        prediction = model.predict_our_model(product_name)

        return render_template('index.html', prediction=prediction, product_name=product_name)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
