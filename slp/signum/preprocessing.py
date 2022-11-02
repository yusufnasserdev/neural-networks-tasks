import pandas as pd

df = pd.read_csv('datasets/penguins.csv')
df = df.replace(to_replace="male", value=1)
df = df.replace(to_replace="female", value=0)


def split(name):
    if name == "c1":
        adelietrain = df[0:30]
        adelietest = df[30:50]
        return adelietrain, adelietest
    elif name == "c2":
        gentootrain = df[50:80]
        gentootest = df[80:100]
        return gentootrain, gentootest
    else:
        chinstraptrain = df[100:130]
        chinstraptest = df[130:150]
        return chinstraptrain, chinstraptest
