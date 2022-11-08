from task1 import preprocessing
from gui.gui_output import show_output

import pandas as pd
import random


def training(x1, x2, t, w0, w1, w2, l_rate, b):

    res = w0 + x1 * w1 + x2 * w2

    # The hard limit transfer function forces a neuron to output a 1 if its net input reaches a threshold, otherwise
    # it outputs 0. This allows a neuron to make a decision or classification. It can say yes or no. This kind of
    # neuron is often trained with the perceptron learning rule.

    if res >= 0:
        y_hat = 1
    else:
        y_hat = -1
    w0_new = 0
    if b == 1:
        w0_new = w0 + l_rate * (t - y_hat) * 1
    w1_new = w1 + l_rate * (t - y_hat) * x1
    w2_new = w2 + l_rate * (t - y_hat) * x2
    return w0_new, w1_new, w2_new


def testing(x1, x2, w0, w1, w2):
    res = w0 + x1 * w1 + x2 * w2
    if res >= 0:
        y_hat = 1
    else:
        y_hat = -1
    return y_hat


def run(class1, class2, x1, x2, ep, bs, rate):
    df=preprocessing.prepare_data()
    train1, test1 = preprocessing.split(class1,df)
    train2, test2 = preprocessing.split(class2,df)
    # to join train1 and train2 in one dataframe
    frames = [train1, train2]
    training_df = pd.concat(frames)
    # to shuffle training dataframe
    training_df = training_df.sample(frac=1, random_state=1, ignore_index=True)
    # to join test1 and test2 in one dataframe
    frames2 = [test1, test2]
    testing_df = pd.concat(frames2)
    # to shuffle testing dataframe
    testing_df = testing_df.sample(frac=1, random_state=1, ignore_index=True)
    # to encode the class name (string) to 1 and -1
    training_df = training_df.replace(to_replace=class1.strip(), value=1)
    training_df = training_df.replace(to_replace=class2.strip(), value=-1)
    testing_df = testing_df.replace(to_replace=class1.strip(), value=1)
    testing_df = testing_df.replace(to_replace=class2.strip(), value=-1)

    w0 = 0
    # take random value between 0 and 1
    w1 = random.random()
    w2 = random.random()
    if bs == 1:
        w0 = random.random()
    cnt = 0
    # Training phase
    for i in range(ep):
        for count in range(0, len(training_df)):
            w0, w1, w2 = training(training_df[x1][count], training_df[x2][count],
                                  training_df['species'][count], w0, w1, w2, rate, bs)

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    # Testing phase to calculate accuracy
    for count in range(0, len(testing_df)):
        target = testing_df['species'][count]
        yhat = testing(testing_df[x1][count], testing_df[x2][count], w0, w1, w2)
        if yhat == target:
            cnt += 1
        if yhat == 1 and target == 1:
            tp += 1
        elif yhat == 1 and target == -1:
            fp += 1
        elif yhat == -1 and target == 1:
            fn += 1
        else:
            tn += 1

    acc = cnt / len(testing_df)

    # visualization.visualize(test1, test2, x1, x2, w0, w1, w2)
    show_output(tp, tn, fp, fn, acc)

    return acc
