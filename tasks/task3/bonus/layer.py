import numpy as np
from task3.bonus.neuron import Neurons
from neuron import calc_net_vectorized


class Layer:

    def __init__(self, neurons_current, neurons_before, check_bias, choice, is_last_layer):
        self.neurons_current = neurons_current
        self.neurons_before = neurons_before
        self.weights_before = np.random.randn(self.neurons_current, (self.neurons_before + 1))
        self.check_bias = check_bias
        self.neurons_array = [Neurons() for i in range(neurons_current)]
        self.choice = choice
        self.is_last_layer = is_last_layer

    def forward(self, m_input):
        if self.check_bias == 1:
            m_input.append(1)
        else:
            m_input.append(0)

        # f_net_current = calc_net_vectorized(m_input, np.transpose(self.weights_before), self.choice)

        for i in range(self.neurons_current):
            self.neurons_array[i].calc_net(m_input, self.weights_before[i, :], self.choice)
        f_net_current = list()
        for i in range(self.neurons_current):
            f_net_current.append(self.neurons_array[i].get_net())
        return f_net_current

    def backward(self, sigma_before, weights, target):
        for i in range(self.neurons_current):
            if self.is_last_layer:
                self.neurons_array[i].calc_sigma_output_layer(target[i], self.choice)
            else:
                self.neurons_array[i].calc_sigma(sigma_before, weights[:, i], self.choice)
        sigma = list()
        for i in range(self.neurons_current):
            sigma.append(self.neurons_array[i].get_sigma())
        return sigma, self.weights_before

    def update(self, m_input, rate):
        for i in range(self.neurons_current):
            for j in range(self.neurons_before + 1):
                self.weights_before[i][j] = self.weights_before[i][j] + (
                        rate * self.neurons_array[i].get_sigma() * m_input[j])
        f_net_current = list()
        for i in range(self.neurons_current):
            f_net_current.append(self.neurons_array[i].get_net())
        return f_net_current
