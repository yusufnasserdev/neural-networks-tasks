import matplotlib.pyplot as plt
import seaborn as sea


def visualize(train1, train2, x1, x2, w0, w1, w2):
    plt.figure('fig1')
    df0 = train1
    df1 = train2
    print(type(df0))
    df2 = df0.append(df1)
    sea.scatterplot(data=df2, x=x1, y=x2, hue="species")
    plt.xlabel(x1)
    plt.ylabel(x2)
    plt.plot(df2[x1], ((-w1 / w2) * df2[x1] - w0 / w2), color='k')
    plt.show()
