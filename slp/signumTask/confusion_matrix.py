import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_confusion_matrix


def gimme_conf_mat(tp, tn, fp, fn):
    conf_matrix = np.array([[tp, fp], [fn, tn]])

    fig, ax = plot_confusion_matrix(conf_mat=conf_matrix, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actual', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.savefig('conf_mat.png')
