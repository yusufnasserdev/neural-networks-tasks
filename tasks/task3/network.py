import sys

import numpy as np
from task3.layer import Layer


class Network:
    def __init__(self, rate, epochs, choice, bias, layers_num, neurons_num):
        self.rate = rate
        self.epochs = epochs
        self.choice = choice  # int
        self.bias = bias  # int
        self.layers_num = layers_num + 1
        self.layers_array = list()
        self.classes = ['Adelie', 'Gentoo', 'Chinstrap']
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
            print("Epoch: ", i + 1)
            # Iterate the train dataset
            for count in range(len(train)):
                # Row features
                row = train.iloc[count][1:].tolist()
                # Forward step
                # FNet first layer
                f_net = self.layers_array[0].forward(row)
                # Iterate the layers
                for j in range(1, len(self.layers_array)):
                    f_net = self.layers_array[j].forward(f_net)
                # Backward step
                # One hot encoding to the actual output
                target = list()
                # Classes list
                for x in self.classes:
                    if train['species'][count] == x:
                        target.append(1)
                    else:
                        target.append(0)
                # Reversing layers to execute the backpropagation
                layers_reversed = self.layers_array[::-1]
                # Last layer
                sigma, weights = layers_reversed[0].backward(1, 1, target)
                for j in range(1, len(layers_reversed)):
                    sigma, weights = layers_reversed[j].backward(sigma, weights, target)
                # Update step
                # First layer
                f_net = self.layers_array[0].update(row, self.rate)
                f_net.append(self.bias)

                for j in range(1, len(self.layers_array)):
                    f_net = self.layers_array[j].update(f_net, self.rate)
                    f_net.append(self.bias)
        cnt = 0
        for count in range(len(train)):
            # Row features
            row = train.iloc[count][1:].tolist()
            # Forward step
            # FNet first layer
            f_net = self.layers_array[0].forward(row)
            # Iterate the layers
            for i in range(1, len(self.layers_array)):
                f_net = self.layers_array[i].forward(f_net)
                if i == self.layers_num - 1:
                    mx = -1 * sys.float_info.max
                    idx = -1
                    for j in range(len(f_net)):
                        if f_net[j] > mx:
                            mx = f_net[j]
                            idx = j
                    specie = self.classes.index(train['species'][count])
                    if specie == idx:
                        cnt += 1
        print("Training acc= ", cnt / len(train))

    def testing(self, test):
        cnt = 0
        conf_matrix = np.zeros([3, 3], dtype=int)
        for count in range(len(test)):
            row = test.iloc[count][1:].tolist()
            # Forward step
            f_net = self.layers_array[0].forward(row)
            for i in range(1, len(self.layers_array)):
                f_net = self.layers_array[i].forward(f_net)
                if i == self.layers_num - 1:
                    mx = -1 * sys.float_info.max
                    idx = -1
                    for j in range(len(f_net)):
                        if f_net[j] > mx:
                            mx = f_net[j]
                            idx = j
                    specie = self.classes.index(test['species'][count])
                    conf_matrix[specie][idx] += 1
                    if specie == idx:
                        cnt += 1
        acc = cnt / len(test)
        return conf_matrix, self.classes, acc
