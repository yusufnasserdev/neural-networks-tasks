from task1 import perceptron
from task2 import adaline
from task3 import backpropagation


def input_perceptron(c1, c2, f1, f2, epochs, bs, rate):
    perceptron.run_perceptron(c1, c2, f1, f2, epochs, bs, rate)


def input_adaline(c1, c2, f1, f2, epochs, bs, rate, mse):
    adaline.run_adaline(c1, c2, f1, f2, epochs, bs, rate, mse)


def input_backpropagation(layers, neurons, epochs, active, bias, rate):
    backpropagation.run_backpropagation(layers, neurons, epochs, active, bias, rate)
