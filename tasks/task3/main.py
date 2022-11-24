
import pandas as pd
import numpy as np
from Forward import *
"""

df_train = pd.read_csv('penguins.csv')

# to take only the array without the label of array
df_train_nolabel = df_train.iloc[:, 1:]

df_train_array = df_train_nolabel.to_numpy()
print(df_train_array.shape)
print('-----------------------------------------------')
x1,x2 = forward(df_train_array, df_train_array.shape[0], df_train_array.shape[1], 10)
print(x1.shape)
print(x2.shape)

# print(np.array(x2).shape)
#print(sigomoid(x2[0]))
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
x3,x4 = forward(x2, x2.shape[0], x2.shape[1], 7)
print(x3.shape)
print(x4.shape)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
x5,x6 = forward(x4, x4.shape[0], x4.shape[1], 4)
print(x5.shape)
print(x6.shape)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
x7,x8 = forward(x6, x6.shape[0], x6.shape[1], 6)

print(x7.shape)
print(x8.shape)

"""


