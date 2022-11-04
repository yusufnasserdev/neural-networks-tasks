import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/penguins.csv')
df = df.replace(to_replace="male", value=1)
df = df.replace(to_replace="female", value=0)
"""
sea.scatterplot(data=df,x=x1,y=x2,hue="species")
plt.xlabel(x1)
plt.ylabel(x2)
"""
def report():
    for i in df:
        for j in df:
            if (i == j):
                continue
        sea.scatterplot(data=df, x=i,y = j, hue = "species")
        plt.xlabel(i)
        plt.ylabel(j)
        plt.show()



def split(name):
    if name == "Adelie":
        adelietrain = df[0:30]
        adelietest = df[30:50]
        return adelietrain, adelietest
    elif name == "Gentoo":
        gentootrain = df[50:80]
        gentootest = df[80:100]
        return gentootrain, gentootest
    else:
        chinstraptrain = df[100:130]
        chinstraptest = df[130:150]
        return chinstraptrain, chinstraptest
