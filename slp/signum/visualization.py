import matplotlib.pyplot as plt
import main
import pandas as pd

plt.figure('fig1')
df0 = main.train1
df1 = main.train2
# df2 = df[df.cluster == 2]

plt.scatter(df0[main.x1], df0[main.x2], color='green')
plt.scatter(df1[main.x1], df1[main.x2], color='blue')

plt.xlabel(main.x1)
plt.ylabel(main.x2)
plt.show()
x1a = 0
x1b = (-main.w0) / main.w2
x2a = (-main.w0) / main.w1
x2b = 0
print(x1b)
print(x2a)
point1 = [x1a, x1b]
point2 = [x2a, x2b]

x_values = [point1[0], point2[0]]

y_values = [point1[1], point2[1]]
plt.plot(x_values, y_values)
plt.show()
