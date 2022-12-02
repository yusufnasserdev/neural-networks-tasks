import numpy as np
from task3.bonus.layer import Layer


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
                self.layers_array.append(Layer(neurons_num[i], 784, self.bias, self.choice, False))
            else:
                self.layers_array.append(Layer(neurons_num[i], neurons_num[i - 1], self.bias, self.choice, False))

        # Output layer
        self.layers_array.append(Layer(10, neurons_num[-1], self.bias, self.choice, True))

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

                for x in range(10):
                    if train['label'][count] == x:
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

            for j in range(1, len(self.layers_array)):
                f_net = self.layers_array[j].forward(f_net)
                if j == self.layers_num - 1:
                    mx = -1
                    idx = -1
                    for j in range(len(f_net)):
                        if f_net[j] > mx:
                            mx = f_net[j]
                            idx = j
                    actual = train['label'][count]
                    if actual == idx:
                        cnt += 1
        print("Training acc= ", cnt / len(train))

    def testing(self, test):
        cnt = 0

        classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        conf_matrix = np.zeros([10, 10], dtype=int)

        for count in range(0, len(test)):
            row = test.iloc[count][1:].tolist()

            # Forward step

            f_net = self.layers_array[0].forward(row)
            for i in range(1, len(self.layers_array)):
                f_net = self.layers_array[i].forward(f_net)

                if i == self.layers_num - 1:
                    mx = -1e10
                    idx = -1
                    for j in range(len(f_net)):
                        if f_net[j] > mx:
                            mx = f_net[j]
                            idx = j

                    actual = test['label'][count]
                    conf_matrix[actual][idx] += 1

                    if actual == idx:
                        cnt += 1

        acc = cnt / len(test)
        return conf_matrix, classes, acc
