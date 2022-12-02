from task3.bonus.network import *
from task3.bonus.preprocessing import *
from gui.gui_output import show_output


def run_bonus_back(layers, neurons, epochs, active, bias, rate):
    train, test = prepare_data()
    print(train.head())
    #train = train.iloc[:10000, :]
    #test = test.iloc[:2000, :]
    network1 = Network(rate, epochs, active, bias, layers, neurons)
    network1.learning(train)
    mat, classes, acc = network1.testing(test)
    show_output(mat, classes, acc)
    print(acc)
