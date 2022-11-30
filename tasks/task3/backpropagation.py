from utils.preprocessing import prepare_data, split
import pandas as pd
from network import *


def run_backpropagation(layers, m_neurons, epochs, active, bias, rate):
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
    network1 = Network(rate, epochs, active, bias, layers, m_neurons)
    network1.learning(training_df)
    acc = network1.testing(testing_df)
    print(acc)
