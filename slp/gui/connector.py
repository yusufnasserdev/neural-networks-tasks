from task1 import perceptron
from task2 import adaline


def input_perceptron(c1, c2, f1, f2, epochs, bs, rate):
    perceptron.run(c1, c2, f1, f2, epochs, bs, rate)


def input_adaline(c1, c2, f1, f2, epochs, bs, rate, mse):
    adaline.run(c1, c2, f1, f2, epochs, bs, rate, mse)
