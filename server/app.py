from flask import Flask, request, jsonify
from neural_net import NeuralNet
from flask_cors import CORS, cross_origin
from data_reader import DataReader
import numpy as np

app = Flask(__name__)
CORS(app)

nn = NeuralNet()

model = nn.build_model(10, 20000)

app.logger.info("Model zbudowany")

coded_letter = DataReader.get_letter_mapping()
coded_output = DataReader.get_output_mapping()


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