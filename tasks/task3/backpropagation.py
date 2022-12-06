from utils.preprocessing import prepare_data, prepare_mnist_data, split
import pandas as pd
from task3.network import Network
from gui.gui_output import show_output


def run_backpropagation(m_neurons, epochs, active, bias, rate, labels, feat_no):
    df = prepare_data()
    train1, test1 = split("Adelie", df)
    train2, test2 = split("Gentoo", df)
    train3, test3 = split("Chinstrap", df)
    frames1 = [train1, train2, train3]
    training_df = pd.concat(frames1)
    # to shuffle training dataframe
    training_df = training_df.sample(frac=1, random_state=1, ignore_index=True)
    # to join test1 and test2 in one dataframe
    frames2 = [test1, test2, test3]
    testing_df = pd.concat(frames2)
    # to shuffle testing dataframe
    testing_df = testing_df.sample(frac=1, random_state=1, ignore_index=True)
    network1 = Network(rate, epochs, active, bias, m_neurons, labels, feat_no)
    network1.learning(training_df)
    mat, classes, acc = network1.testing(testing_df)
    show_output(mat, classes, acc)


def run_bonus_back(m_neurons, epochs, active, bias, rate, labels, feat_no):
    train, test = prepare_mnist_data()
    print(train.head())
    train = train.iloc[:500, :]
    test = test.iloc[:100, :]
    network1 = Network(rate, epochs, active, bias, m_neurons, labels, feat_no)
    network1.learning(train)
    mat, classes, acc = network1.testing(test)
    show_output(mat, classes, acc)
    print(acc)
