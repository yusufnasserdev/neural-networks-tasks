import random
import preprocessing
import Training
import Testing
import pandas as pd

class1 = "c1"
class2 = "c2"
x1 = "flipper_length_mm"
x2 = "bill_depth_mm"
epochs = 100
L = 0.15
bias = True

train1, test1 = preprocessing.split(class1)
train2, test2 = preprocessing.split(class2)
m_dict = {"c1": 1, "c2": 50, "c3": 100}
class1name = train1['species'][m_dict[class1]]
class2name = train2['species'][m_dict[class2]]

frames = [train1, train2]
training = pd.concat(frames)
training = training.sample(frac=1, random_state=1, ignore_index=True)

frames2 = [test1, test2]

testing = pd.concat(frames2)
testing = testing.sample(frac=1, random_state=1, ignore_index=True)
training = training.replace(to_replace=class1name, value=1)
training = training.replace(to_replace=class2name, value=-1)
testing = testing.replace(to_replace=class1name, value=1)
testing = testing.replace(to_replace=class2name, value=-1)

w0 = 0
w1 = random.random()
w2 = random.random()

if bias:
    w0 = random.random()

for i in range(epochs):
    for count in range(0, len(training)):
        w0, w1, w2 = Training.training(training[x1][count], training[x2][count], training['species'][count], w0, w1, w2,
                                       L, bias)
    cnt = 0
    for count in range(0, len(testing)):
        cnt += Testing.testing(testing[x1][count], testing[x2][count], testing['species'][count], w0, w1, w2)

acc = cnt / len(testing)
print(acc)
