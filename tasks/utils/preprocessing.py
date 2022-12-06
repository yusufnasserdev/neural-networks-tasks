import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

features = ['bill_length_mm', 'bill_depth_mm',
            'flipper_length_mm', 'gender', 'body_mass_g']


def prepare_data():
    df = pd.read_csv('../datasets/penguins.csv')
    df = df.replace(to_replace="male", value=1)
    df = df.replace(to_replace="female", value=-1)
    sps = df['species'].tolist()
    df = df.drop('species', axis=1)
    # Normalization
    df = (df - df.mean()) / df.std()
    df.insert(0, 'species', sps)
    return df


def split(name, df):
    if name == "Adelie":
        adelie_train = df[0:30]
        adelie_test = df[30:50]
        return adelie_train, adelie_test
    elif name == "Gentoo":
        gentoo_train = df[50:80]
        gentoo_test = df[80:100]
        return gentoo_train, gentoo_test
    elif name == "Chinstrap":
        chinstrap_train = df[100:130]
        chinstrap_test = df[130:150]
        return chinstrap_train, chinstrap_test


def normalize(df):
    labels = df['label'].tolist()
    df = df.drop('label', axis=1)
    # Normalization
    df = df / 255
    df.insert(0, 'label', labels)
    return df


def prepare_mnist_data():
    df_train = pd.read_csv('../datasets/mnist_train.csv')
    df_test = pd.read_csv('../datasets/mnist_test.csv')
    df_train = normalize(df_train)
    df_test = normalize(df_test)
    df_train.fillna(0, inplace=True)
    df_test.fillna(0, inplace=True)
    return df_train, df_test


def report(df):
    for i in range(0, 5):
        for j in range(i + 1, 5):
            sea.scatterplot(data=df, x=features[i], y=features[j], hue="species")
            plt.xlabel(features[i])
            plt.ylabel(features[j])
            plt.show()
