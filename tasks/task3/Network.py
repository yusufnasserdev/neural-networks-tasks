from layer import *

class network():
    def __init__(self, rate, epochs, choice, bais, numoflayers, numofneurons):
        self.rate = rate
        self.epochs = epochs
        self.choice = choice
        self.bais = bais
        self.numoflayers = numoflayers
        self.numofneurons = numofneurons
        self.layers_array = []
        for i in range(numoflayers):
            if i == 0:
                if numoflayers == 1:
                    self.layers_array.append(layer(numofneurons[i], 5, bais, choice, True))
                else:
                    self.layers_array.append(layer(numofneurons[i], 5, bais, choice, False))
            else:
                if i == numoflayers - 1:
                    self.layers_array.append(layer(numofneurons[i], numofneurons[i - 1], bais, choice, True))
                else:
                    self.layers_array.append(layer(numofneurons[i], numofneurons[i - 1], bais, choice, False))

    def learning(self, train):
        for i in range(self.epochs):
            for count in range(0,len(train)):
                # forward step
                for i in range(self.numoflayers):
                    output = []
                    if count == 0:
                        output = self.layers_array[count].forward(train[count].loc[:, 1:])
                    else:
                        output = self.layers_array[count].forward(output)
                #backward step
                cnt = self.numoflayers-1
                target=[]
                if train['species'][count]=='Adelie':
                    target.append(1)
                    target.append(0)
                    target.append(0)
                elif train['species'][count]=='Gentoo':
                    target.append(0)
                    target.append(1)
                    target.append(0)
                else:
                    target.append(0)
                    target.append(0)
                    target.append(1)
                while (True):
                    if (cnt < 0):
                        break
                    output=[]
                    if cnt!=0:
                        weights = np.random.rand([self.numoflayers[cnt], (self.numoflayers[cnt - 1] + 1)])
                    else:
                        weights= np.random.rand([self.numoflayers[cnt], 5])
                    if cnt==self.numoflayers-1:
                        output,weights=self.layers_array[cnt].backword(1,1,target)
                    else:
                        output,weights=self.layers_array[cnt].backword(output,weights,target)
                    cnt -= 1
                #uodate step
                for i in range(self.numoflayers):
                    output = []
                    if count == 0:
                        output = self.layers_array[count].update(train[count].iloc[:, 1:],self.rate)
                    else:
                        output = self.layers_array[count].update(output,self.rate)
    def testing(self,test):
        cnt= 0
        for count in range(0,len(test)):
            # forward step
            for i in range(self.numoflayers):
                output = []
                if count == 0:
                    output = self.layers_array[count].forward(test[count].iloc[:, 1:])
                else:
                    output = self.layers_array[count].forward(output)
                if i==self.numoflayers-1:
                    mx=-1
                    idx=-1
                    for j in range(len(output)):
                        if(output[j]>mx):
                            mx=output[j]
                            idx=j
                    if(test['species'][count]=='Adelie' and j==0):
                        cnt+=1
                    elif(test['species'][count]=='Gentoo' and j==1):
                        cnt+1
                    elif(test['species'][count]=='Chinstrap' and j==2):
                        cnt+1
        return cnt/len(test)




