import pandas as pd
import numpy as np


def normalize(df):
    labels = df['label'].tolist()
    df = df.drop('label', axis=1)
    # Normalization
    df = (df - df.mean()) / df.std()
    df.insert(0, 'label', labels)
    return df


def prepare_data():
    df_train = pd.read_csv('../../datasets/mnist_train.csv')
    df_test = pd.read_csv('../../datasets/mnist_test.csv')
    df_train = normalize(df_train)
    df_test = normalize(df_test)
    df_train.fillna(0,inplace=True)
    df_test.fillna(0, inplace=True)
    return df_train, df_test




# to take only the array without the label of array
# df_train_nolabel = df_train.iloc[:, 1:]
