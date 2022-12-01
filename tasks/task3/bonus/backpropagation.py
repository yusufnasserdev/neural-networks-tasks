from task3.bonus.network import *
from task3.bonus.preprocessing import *


def run_bonus_back(layers, neurons, epochs, active, bias, rate):
    train, test = prepare_data()
    print(train.head())
    # train = train.iloc[:5000, :]
    # test = test.iloc[:2000, :]
    network1 = Network(rate, epochs, active, bias, layers, neurons)
    network1.learning(train)
    acc = network1.testing(test)
    print(acc)
