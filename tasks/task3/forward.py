import numpy as np
from numpy import random


def forward(x, x_inputs, inputs_layer_after):
    wh_container = []
    net_function = []

    for i in range(inputs_layer_after):
        weights = np.random.rand(x_inputs)
        wh_container.append(weights)

    for i in x:
        m_sum = []
        for j in wh_container:
            m_sum.append(np.dot(np.transpose(i), j))

        net_function.append(m_sum)

    return np.array(wh_container), np.array(net_function)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))