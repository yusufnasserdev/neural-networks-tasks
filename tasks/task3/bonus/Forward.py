import numpy
import numpy as np
from numpy import random


def forward(X, X_size, X_inputs, inputs_layer_after):
    wh_container = []
    net_function = []

    for i in range(inputs_layer_after):
        weights = np.random.rand(X_inputs)
        wh_container.append(weights)

    for i in X:
        sum = []
        for j in wh_container:
            sum.append(np.dot(np.transpose(i),j))

        net_function.append(sum)

    return numpy.array(wh_container), numpy.array(net_function)


def sigomoid(X):
    return 1 / (1 + np.exp(-X))


'''import numpy as np
from numpy import random
class layer:
    def __init__(self,my_list):
        self.my_list = []

    def build(self,num1):
        for i in len(num1):
            np1=random.rand(784)
            self.my_list.append(np1)'''
