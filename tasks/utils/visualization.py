import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt

from mlxtend.plotting import plot_confusion_matrix

import warnings

warnings.filterwarnings("ignore")


def generate_conf_mat(tp, tn, fp, fn):
    conf_matrix = np.array([[tp, fp], [fn, tn]])

    fig, ax = plot_confusion_matrix(conf_mat=conf_matrix,
                                    figsize=(6, 6),
                                    cmap=plt.cm.Greens,
                                    show_absolute=True,
                                    show_normed=True,
                                    colorbar=True)

    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actual', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.savefig('conf_mat.png')


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
