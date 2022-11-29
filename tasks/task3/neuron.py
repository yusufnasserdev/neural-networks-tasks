import math

from layer import *
import numpy as np


def activation_function(activation_choice, result):
    if activation_choice == 1:
        return 1 / (1 + math.exp(-result))
    else:
        return (1 - math.exp(-result)) / (1 + math.exp(-result))


class neurons():
    net = 0
    sigma_back = 0

    def calc_net(self, input, weight, activation_chocie):
        try:
            result = np.dot(input, np.transpose(weight))
            self.net = activation_function(activation_chocie, result)
        except:
            print(input)
            print("//////////////////////////")
            print(weight)


    def calc_sigma_output_layer(self, desired, activation_choice):
        if activation_choice == 1:
            self.sigma_back = (desired - self.net) * self.net * (1 - self.net)
        else:
            self.sigma_back = (desired - self.net) * (self.net + 1) * (1 - self.net)

    def calc_sigma(self, input, weight, activation_choice):
        if activation_choice == 1:
            self.sigma_back = self.net * (1 - self.net) * np.dot(input, weight)
        else:
            self.sigma_back = (self.net + 1) * (1 - self.net) * np.dot(input, weight)

    def getsigma(self):
        return self.sigma_back

    def getnet(self):
        return self.net
