from utils.preprocessing import prepare_data, split
import pandas as pd
from Network import *

def run_backpropagation(layers, neurons, epochs, active, bias, rate):
    df = prepare_data()
    train1, test1 = split("Adelie", df)
    train2, test2 = split("Gentoo", df)
    train3, test3 = split("Chinstrap", df)
    frames = [train1, train2,train3]
    training_df = pd.concat(frames)
    # to shuffle training dataframe
    training_df = training_df.sample(frac=1, random_state=1, ignore_index=True)
    # to join test1 and test2 in one dataframe
    frames2 = [test1, test2,test3]
    testing_df = pd.concat(frames2)
    # to shuffle testing dataframe
    testing_df = testing_df.sample(frac=1, random_state=1, ignore_index=True)
    network1=network(0.01,1000,1,True,3,[4,5,5])
    network1.learning(training_df)
    acc=network1.testing(testing_df)
    print(acc)
run_backpropagation(1,5,5,1,1,1)