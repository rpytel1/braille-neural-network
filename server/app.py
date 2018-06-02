from flask import Flask, request, jsonify, render_template, send_from_directory
from neural_net import NeuralNet
from flask_cors import CORS, cross_origin
from data_reader import DataReader
import builtins
builtins.unicode = str

from flask_triangle import Triangle
import numpy as np


app = Flask(__name__)
CORS(app)
Triangle(app)

nn = NeuralNet()

model = nn.build_model(10, 20000)

app.logger.info("Model zbudowany")

coded_letter = DataReader.get_letter_mapping()
coded_output = DataReader.get_output_mapping()


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/js/app.js')
def angular_script():
    return app.send_static_file('/js/app.js')

@app.route('/img/<path:path>')
def get_images(path):
    return send_from_directory('static/img', path)

@app.route("/translate", methods=['POST'])
@cross_origin()
def translate_string():
    string = request.get_json()["text"]
    output = ""

    for c in string:
        if c.isspace():
            output = output + " "
            continue
        letter = np.array(coded_letter[c])
        a = nn.predict(model, letter)
        output_letter = coded_output[a]
        output = output + output_letter

    return jsonify(output)


@app.route("/train", methods=['POST'])
@cross_origin()
def train_model():
    data = request.get_json()
    nn_hdim = data["hiddenLayer"]
    epoch = data["epoch"]
    learning_rate = data["learningRate"]

    global model
    model = nn.build_model(nn_hdim, epoch, learning_rate)

    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}



if __name__ == '__main__':
    app.run(debug=True)