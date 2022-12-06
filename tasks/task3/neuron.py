from task3.layer import *
import numpy as np


def activation_function(activation_choice, result):
    if activation_choice == 1:
        return 1 / (1 + np.exp(-result))
    else:
        return np.tanh(result)


class Neuron:
    net = 0
    sigma_back = 0

    def calc_net(self, m_input, weight, activation_choice):
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
