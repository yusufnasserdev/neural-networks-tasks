from layer import *
class network():
    def __init__(self,rate,epochs,choice,bais,numoflayers,numofneurons):
        self.rate=rate
        self.epochs=epochs
        self.choice=choice
        self.bais=bais
        self.numoflayers=numoflayers
        self.numofneurons=numofneurons
        self.layers_array=[]
        for i in range(numoflayers):
            if i==0:
                if numofneurons==1:
                    self.layers_array[i] = layer(numofneurons[i], 5, bais, choice,True)
                else:
                    self.layers_array[i] = layer(numofneurons[i], 5, bais, choice, False)
            else:
                if i==numofneurons-1:
                    self.layers_array[i] = layer(numofneurons[i], numofneurons[i-1], bais, choice, True)
                else:
                    self.layers_array[i] = layer(numofneurons[i], numofneurons[i - 1], bais, choice, False)

    def learning(self,train):
        for i in range(self.epochs):
            for count in len(train):
                pass



