from task3.bonus.preprocessing  import *
import pandas as pd
from Network import *


def run_backpropagation(layers, neurons, epochs, active, bias, rate):
    train,test = prepare_data()
    network1 = network(rate, epochs, active, bias, layers, neurons)
    network1.learning(train)
    acc = network1.testing(test)
    print(acc)
