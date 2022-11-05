import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

features = ['bill_length_mm', 'bill_depth_mm',
            'flipper_length_mm', 'gender', 'body_mass_g']

df = pd.read_csv('datasets/penguins.csv')
df = df.replace(to_replace="male", value=1)
df = df.replace(to_replace="female", value=-1)

sps = df['species'].tolist()
df = df.drop('species', axis=1)

# Normalization
df = (df - df.mean()) / df.std()
df.insert(0, 'species', sps)


def report():
    for i in range(0, 5):
        for j in range(i + 1, 5):
            sea.scatterplot(data=df, x=features[i], y=features[j], hue="species")
            plt.xlabel(features[i])
            plt.ylabel(features[j])
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
