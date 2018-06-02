import numpy as np
from data_reader import DataReader


class NeuralNet:

    @staticmethod
    def sigmoid_function(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def derivative_sigmoid_function(x):
        return x * (1 - x)

    def build_model(self, nn_hdim, num_passes=20000, learning_rate=0.1):
        X, y = DataReader.read_training_data()

        nn_input_dim = 6  # input layer dimensionality
        nn_output_dim = 26  # output layer dimensionality

        # Initialize the parameters to random values. We need to learn these.
        np.random.seed(0)
        W1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
        b1 = np.zeros((1, nn_hdim))
        W2 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)
        b2 = np.zeros((1, nn_output_dim))

        # This is what we return at the end
        model = {}

        # Gradient descent
        for i in range(0, num_passes):
            # Forward propagation
            z1 = X.dot(W1) + b1
            a1 = self.sigmoid_function(z1)
            z2 = a1.dot(W2) + b2
            exp_scores = self.sigmoid_function(z2)

            # Softmax
            # probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

            # Backpropagation
            delta3 = (exp_scores - y) * self.derivative_sigmoid_function(exp_scores)
            dW2 = (a1.T).dot(delta3)
            db2 = np.sum(delta3, axis=0, keepdims=True)

            delta2 = delta3.dot(W2.T) * self.derivative_sigmoid_function(a1)
            dW1 = (X.T).dot(delta2)
            db1 = np.sum(delta2, axis=0)

            # Gradient descent parameter update
            W1 += -learning_rate * dW1
            b1 += -learning_rate * db1
            W2 += -learning_rate * dW2
            b2 += -learning_rate * db2

            # Assign new parameters to the model
            model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}

        return model

    def predict_test(self, model):

        x = DataReader.read_test_data()

        W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
        z1 = x.dot(W1) + b1
        a1 = self.sigmoid_function(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = self.sigmoid_function(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        return np.argmax(probs)

    def predict(self, model, x):

        W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
        z1 = x.dot(W1) + b1
        a1 = self.sigmoid_function(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = self.sigmoid_function(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        return np.argmax(probs)


def main():
    nn = NeuralNet()

    model = nn.build_model(10, 20000)
    predictions = nn.predict_test(model)

    print(predictions)


if __name__ == "__main__":
    main()
