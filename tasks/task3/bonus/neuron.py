from task3.bonus.layer import *
import numpy as np


def activation_function(activation_choice, result):
    if activation_choice == 1:
        return 1 / (1 + np.exp(-result))
    else:
        return (1 - np.exp(-result)) / (1 + np.exp(-result))


def calc_net_vectorized(m_input, weight, activation_choice):
    result = np.dot(np.transpose(m_input), weight)

    # https://peterroelants.github.io/posts/neural-network-implementation-part04/

    for i in range(len(result)):
        result[i] = activation_function(activation_choice, result[i])

    return result


class Neurons:
    net = 0
    sigma_back = 0

    def calc_net(self, m_input, weight, activation_choice):
        # try:
        result = np.dot(m_input, np.transpose(weight))
        self.net = activation_function(activation_choice, result)

    def calc_sigma_output_layer(self, desired, activation_choice):
        if activation_choice == 1:
            self.sigma_back = (desired - self.net) * self.net * (1 - self.net)
        else:
            self.sigma_back = (desired - self.net) * (self.net + 1) * (1 - self.net)

    def calc_sigma(self, m_input, weight, activation_choice):
        if activation_choice == 1:
            self.sigma_back = self.net * (1 - self.net) * np.dot(m_input, weight)
        else:
            self.sigma_back = (self.net + 1) * (1 - self.net) * np.dot(m_input, weight)

    def get_sigma(self):
        return self.sigma_back

    def get_net(self):
        return self.net
