import numpy as np
from task3.bonus.neuron import *


class Layer():

    def __init__(self, neurons_current, neurons_before, check_bias, choice, islastlayer):
        self.neurons_current = neurons_current
        self.neurons_before = neurons_before
        self.weights_before = np.random.randn(self.neurons_current, (self.neurons_before + 1))
        self.check_bias = check_bias
        self.neurons_array = [Neurons() for i in range(neurons_current)]
        self.choice = choice
        self.islastlayer = islastlayer

    def forward(self, input):
        if self.check_bias == 1:
            input.append(1)
        else:
            input.append(0)
        for i in range(self.neurons_current):
            self.neurons_array[i].calc_net(input, self.weights_before[i, :], self.choice)
        arr = list()
        for i in range(self.neurons_current):
            arr.append(self.neurons_array[i].get_net())
        return arr

    def backward(self, segmabefore, weights, target):
        for i in range(self.neurons_current):
            if self.islastlayer:
                self.neurons_array[i].calc_sigma_output_layer(target[i], self.choice)
            else:
                self.neurons_array[i].calc_sigma(segmabefore, weights[:, i], self.choice)
        arr = list()
        for i in range(self.neurons_current):
            arr.append(self.neurons_array[i].get_sigma())
        return arr, self.weights_before

    def update(self, input, L):
        for i in range(self.neurons_current):
            for j in range(self.neurons_before + 1):
                self.weights_before[i][j] = self.weights_before[i][j] + (
                        L * self.neurons_array[i].get_sigma() * input[j])
        arr = list()
        for i in range(self.neurons_current):
            arr.append(self.neurons_array[i].get_net())
        return arr
