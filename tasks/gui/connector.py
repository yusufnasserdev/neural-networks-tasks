from task1.perceptron import run_perceptron
from task2.adaline import run_adaline
from task3.backpropagation import run_backpropagation
from task3.bonus.backpropagation import run_bonus_back


def input_perceptron(c1, c2, f1, f2, epochs, bs, rate):
    run_perceptron(c1, c2, f1, f2, epochs, bs, rate)


def input_adaline(c1, c2, f1, f2, epochs, bs, rate, mse):
    run_adaline(c1, c2, f1, f2, epochs, bs, rate, mse)


def input_backpropagation(layers, neurons, epochs, active, bias, rate):
    run_backpropagation(layers, neurons, epochs, active, bias, rate)


def input_bonus(layers, neurons, epochs, active, bias, rate):
    run_bonus_back(layers, neurons, epochs, active, bias, rate)
