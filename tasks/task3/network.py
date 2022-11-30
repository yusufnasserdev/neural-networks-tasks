import numpy as np

from layer import *


class Network:
    def __init__(self, rate, epochs, choice, bias, layers_num, neurons_num):
        self.rate = rate
        self.epochs = epochs
        self.choice = choice  # int
        self.bias = bias  # int
        self.layers_num = layers_num + 1
        self.layers_array = list()

        # Hidden layers
        for i in range(len(neurons_num)):
            if i == 0:
                self.layers_array.append(Layer(neurons_num[i], 5, self.bias, self.choice, False))
            else:
                self.layers_array.append(Layer(neurons_num[i], neurons_num[i - 1], self.bias, self.choice, False))

        # Output layer
        self.layers_array.append(Layer(3, neurons_num[-1], self.bias, self.choice, True))

    def learning(self, train):
        # Iterate the epochs
        for i in range(self.epochs):
            # Iterate the train dataset
            for count in range(len(train)):
                # Row features
                row = train.iloc[count][1:].tolist()

                # Forward step

                # Layer FNet
                f_net = list()
                # Iterate the layers
                for j in range(len(self.layers_array)):
                    if j == 0:
                        output = self.layers_array[j].forward(row)
                    else:
                        output = self.layers_array[j].forward(f_net)

                # Backward step

                # One hot encoding to the actual output
                target = list()

                # Classes list
                classes = ['Adelie', 'Gentoo', 'Chinstrap']

                for x in classes:
                    if train['species'][count] == x:
                        target.append(1)
                    else:
                        target.append(0)

                # Sigma list
                sigma = list()

                layers_reversed = self.layers_array[::-1]
                output, weights = layers_reversed[0].backword(1, 1, target)

                for j in range(len(layers_reversed)):
                    output, weights = layers_reversed[j].backword(sigma, weights, target)

                # update step
                output = list()
                for j in range(len(self.layers_array)):
                    if j == 0:
                        output = self.layers_array[j].update(row, self.rate)
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
                if i == self.layers_num - 1:
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
