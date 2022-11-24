import math

from layer import *
import numpy as np
class neurons():
    net = 0
    sigma_back = 0


    def get_net(self,input,weight,activation_chocie):
        result = np.dot(input,np.transpose(weight))
        net = self.activation_function(activation_chocie,result)


    def activation_function(self,activation_choice,result):
        if activation_choice == 1:
            return 1/(1+math.exp(-result))
        else:
            return (1-math.exp(-result))/(1+math.exp(-result))

    def get_sigma_output_layer(self,desired,output):
        return (desired - output)*output*(1-output)


    def get_sigma(self,output,weight,sigma):
        return sigma*weight*output*(1-output)
