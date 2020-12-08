from flask import Flask, render_template
from flask import request
import predict

app = Flask(__name__)

model = predict.Model()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        predictions = []

        for key in ['product', 'address']:

            field_val = request.form[key]

            prediction = model.predict_our_model(field_val)

            pred_obj = {
                "field": key,
                "field_val": field_val,
                "prediction": prediction,
            }
            predictions.append(pred_obj)

        return render_template('index.html', predictions=predictions)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
