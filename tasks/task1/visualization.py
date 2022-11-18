import matplotlib.pyplot as plt
import seaborn as sea
import warnings

warnings.filterwarnings("ignore")


def visualize(test1, test2, x1, x2, w0, w1, w2):
    plt.figure('fig1')
    df0 = test1
    df1 = test2
    df2 = df0.append(df1)
    sea.scatterplot(data=df2, x=x1, y=x2, hue="species")
    plt.xlabel(x1)
    plt.ylabel(x2)
    plt.plot(df2[x1], ((-w1 / w2) * df2[x1] - w0 / w2), color='k')
    plt.show()
