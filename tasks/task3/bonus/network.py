import numpy as np

from task3.bonus.layer import *


class Network:
    def __init__(self, rate, epochs, choice, bais, numoflayerss, numofneurons):
        self.rate = rate
        self.epochs = epochs
        self.choice = choice  # int
        self.bais = bais  # int
        self.numoflayers = numoflayerss + 1
        self.layers_array = list()
        for i in range(len(numofneurons)):
            if i == 0:
                self.layers_array.append(Layer(numofneurons[i], 784, bais, choice, False))
            else:
                self.layers_array.append(Layer(numofneurons[i], numofneurons[i - 1], bais, choice, False))
        self.layers_array.append(Layer(10, numofneurons[-1], bais, choice, True))

    def learning(self, train):
        for i in range(self.epochs):
            print(i)
            for count in range(len(train)):
                features = train.iloc[count][1:]
                features = features.tolist()
                # forward step
                output = list()
                for j in range(len(self.layers_array)):
                    if j == 0:
                        output = self.layers_array[j].forward(features)
                    else:
                        output = self.layers_array[j].forward(output)
                # backward step
                cnt = self.numoflayers - 1
                target = list()
                for x in range(10):
                    if train['label'][count] == x:
                        target.append(1)
                    else:
                        target.append(0)

                output = list()
                rev = self.layers_array[::-1]
                for j in range(len(rev)):
                    if j == 0:
                        output, weights = rev[j].backward(1, 1, target)
                    else:
                        output, weights = rev[j].backward(output, weights, target)

                # update step
                output = list()
                for j in range(len(self.layers_array)):
                    if j == 0:
                        output = self.layers_array[j].update(features, self.rate)
                        output.append(self.bais)
                    else:
                        output = self.layers_array[j].update(output, self.rate)
                        output.append(self.bais)

    def testing(self, test):
        cnt = 0
        for count in range(0, len(test)):
            features = test.iloc[count][1:]
            features = features.tolist()
            # forward step
            output = list()
            for i in range(len(self.layers_array)):
                if i == 0:
                    output = self.layers_array[i].forward(features)
                else:
                    output = self.layers_array[i].forward(output)
                if i == self.numoflayers - 1:
                    mx = -1
                    idx = -1
                    for j in range(len(output)):
                        if output[j] > mx:
                            mx = output[j]
                            idx = j
                    if test['label'][count] == idx:
                        cnt += 1
        return cnt / len(test)
