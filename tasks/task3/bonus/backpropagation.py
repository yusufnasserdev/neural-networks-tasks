from task3.bonus.preprocessing import *
import pandas as pd
from network import *


def run_backpropagation(layers, neurons, epochs, active, bias, rate):
    train, test = prepare_data()
    train = train.iloc[:5000, :]
    test = test.iloc[:2000, :]
    network1 = Network(rate, epochs, active, bias, layers, neurons)
    network1.learning(train)
    acc = network1.testing(test)
    print(acc)
