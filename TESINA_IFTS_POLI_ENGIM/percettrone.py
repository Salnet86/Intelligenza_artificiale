import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.eta = learning_rate

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias
        return 1 if summation > 0 else 0

    def train(self, training_inputs, labels, epochs=10):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights += self.eta * error * inputs
                self.bias += self.eta * error

inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
labels = np.array([0, 0, 0, 1])

neuron = Perceptron(input_size=2)
neuron.train(inputs, labels)

for i in inputs:
    print(f"Input: {i} -> Predizione: {neuron.predict(i)}")
  
