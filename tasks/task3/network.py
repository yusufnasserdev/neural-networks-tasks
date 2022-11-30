import numpy as np

from layer import *


class Network:
    def __init__(self, rate, epochs, choice, bias, layers_num, neurons_num):
        self.rate = rate
        self.epochs = epochs
        self.choice = choice  # int
        self.bias = bias  # int
        self.num_layers = layers_num + 1
        self.layers_array = list()
        for i in range(len(neurons_num)):
            if i == 0:
                self.layers_array.append(Layer(neurons_num[i], 5, bias, choice, False))
            else:
                self.layers_array.append(Layer(neurons_num[i], neurons_num[i - 1], bias, choice, False))
        self.layers_array.append(Layer(3, neurons_num[-1], bias, choice, True))

    def learning(self, train):
        for i in range(self.epochs):
            for count in range(len(train)):
                features = train.iloc[count][1:].tolist()
                # forward step
                output = list()
                for j in range(len(self.layers_array)):
                    if j == 0:
                        output = self.layers_array[j].forward(features)
                    else:
                        output = self.layers_array[j].forward(output)
                # backward step
                cnt = self.num_layers - 1
                target = list()
                if train['species'][count] == 'Adelie':
                    target.append(1)
                    target.append(0)
                    target.append(0)
                elif train['species'][count] == 'Gentoo':
                    target.append(0)
                    target.append(1)
                    target.append(0)
                else:
                    target.append(0)
                    target.append(0)
                    target.append(1)
                output = list()
                rev = self.layers_array[::-1]
                for j in range(len(rev)):
                    if j == 0:
                        output, weights = rev[j].backword(1, 1, target)
                    else:
                        output, weights = rev[j].backword(output, weights, target)
                # update step
                output = list()
                for j in range(len(self.layers_array)):
                    if j == 0:
                        output = self.layers_array[j].update(features, self.rate)
                        output.append(self.bias)
                    else:
                        output = self.layers_array[j].update(output, self.rate)
                        output.append(self.bias)

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
                if i == self.num_layers - 1:
                    mx = -1
                    idx = -1
                    for j in range(len(output)):
                        if output[j] > mx:
                            mx = output[j]
                            idx = j
                    if test['species'][count] == 'Adelie' and idx == 0:
                        cnt += 1
                    elif test['species'][count] == 'Gentoo' and idx == 1:
                        cnt += 1
                    elif test['species'][count] == 'Chinstrap' and idx == 2:
                        cnt += 1
        return cnt / len(test)
