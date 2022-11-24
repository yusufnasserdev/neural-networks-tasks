


import numpy as np
from neuron import *
class layer():



    def __init__(self,neurons_current,neurons_before,neurons_after,check_bias,choice,**weights_before):
        self.neurons_current = neurons_current
        self.neurons_after = neurons_after
        self.neurons_before = neurons_before
        self.weights_before = np.random.rand([self.neurons_current, (self.neurons_before + 1)])
        self.check_bias = check_bias
        self.neurons_array = [neurons() for i in range(neurons_current)]
        self.choice = choice

    def forward(self,input, input_shape):
        if self.check_bias:
            input.append(1)
        else:
            input.append(0)

        for i in range(self.neurons_current):
            self.neurons_array[i].get_net(input,self.weights_before[i,:],self.choice)



#arr_rand = np.random.rand(3,4)
