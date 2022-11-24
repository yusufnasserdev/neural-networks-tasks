import math

from layer import *
import numpy as np


class neurons():
    net = 0
    sigma_back = 0

    def calc_net(self, input, weight, activation_chocie):
        result = np.dot(input, np.transpose(weight))
        net = self.activation_function(activation_chocie, result)

    def activation_function(self, activation_choice, result):
        if activation_choice == True:
            return 1 / (1 + math.exp(-result))
        else:
            return (1 - math.exp(-result)) / (1 + math.exp(-result))

    def calc_sigma_output_layer(self, desired, activation_choice):
        if activation_choice == True:
            return (desired - self.net) * self.net * (1 - self.net)
        else:
            return (desired - self.net) * (self.net + 1) * (1 - self.net)

    def calc_sigma(self, input, weight, activation_choice):
        if activation_choice == True:
            return self.net * (1 - self.net) * np.dot(input, weight)
        else:
            return (self.net + 1) * (1 - self.net) * np.dot(input, weight)

    def getsigma(self):
        return self.sigma_back

    def getnet(self):
        return self.net
