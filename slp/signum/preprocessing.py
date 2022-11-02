import pandas as pd

df = pd.read_csv('datasets/penguins.csv')
df=df.replace(to_replace="male",value=1)
df=df.replace(to_replace="female",value=0)

def split(name):
    if(name=="c1"):
        Adelietrain = df[0:30]
        Adelietest = df[30:50]
        return Adelietrain,Adelietest
    elif(name=="c2"):
        Gentootrain = df[50:80]
        Gentootest = df[80:100]
        return Gentootrain,Gentootest
    else:
        Chinstraptrain = df[100:130]
        Chinstraptest = df[130:150]
        return Chinstraptrain,Chinstraptest



