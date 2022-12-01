import warnings

import matplotlib.pyplot as plt
import seaborn as sea
from mlxtend.plotting import plot_confusion_matrix

warnings.filterwarnings("ignore")


def generate_conf_mat(mat, classes):
    fig, ax = plot_confusion_matrix(conf_mat=mat,
                                    class_names=classes,
                                    figsize=(8, 8),
                                    cmap=plt.cm.Greens,
                                    show_absolute=True,
                                    show_normed=True,
                                    colorbar=True)

    plt.xlabel('Predictions', fontsize=15)
    plt.ylabel('Actual', fontsize=15)
    plt.title('Confusion Matrix', fontsize=15)
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
