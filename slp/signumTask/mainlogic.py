from signumTask import preprocessing, Training, Testing, visualization
import pandas as pd
import random


def logic(class1, class2, x1, x2, ep, bs, L):
    train1, test1 = preprocessing.split(class1)
    train2, test2 = preprocessing.split(class2)
    # to join train1 and train2 in one dataframe
    frames = [train1, train2]
    training = pd.concat(frames)
    # to shuffle training dataframe
    training = training.sample(frac=1, random_state=1, ignore_index=True)
    # to join test1 and test2 in one dataframe
    frames2 = [test1, test2]
    testing = pd.concat(frames2)
    # to shuffle testing dataframe
    testing = testing.sample(frac=1, random_state=1, ignore_index=True)
    # to encode the class name (string) to 1 and -1
    training = training.replace(to_replace=class1.strip(), value=1)
    training = training.replace(to_replace=class2.strip(), value=-1)
    testing = testing.replace(to_replace=class1.strip(), value=1)
    testing = testing.replace(to_replace=class2.strip(), value=-1)

    w0 = 0
    # take random value between 0 and 1
    w1 = random.random()
    w2 = random.random()
    if bs == 1:
        w0 = random.random()
    cnt = 0
    # Training phase
    for i in range(ep):
        for count in range(0, len(training)):
            w0, w1, w2 = Training.training(training[x1][count], training[x2][count],
                                           training['species'][count], w0, w1, w2, L, bs)
    # Testing phase to calculate accuracy
    for count in range(0, len(testing)):
        cnt += Testing.testing(testing[x1][count], testing[x2][count], testing['species'][count], w0, w1, w2)

    acc = cnt / len(testing)
    print(acc)
    visualization.visualize(train1, train2, x1, x2, w0, w1, w2)