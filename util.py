
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import matplotlib as mpl
import pandas as pd
from sklearn.metrics import pairwise_distances_argmin


def make_ellipses(mog, ax):
    colors = ['purple','blue','aqua','green','olive']
    for n, color in enumerate(colors):
        covariances = mog.sigma_arr[n]
        v, w = np.linalg.eigh(covariances)
        u = w[0] / np.linalg.norm(w[0])
        angle = np.arctan2(u[1], u[0])
        angle = 180 * angle / np.pi  # convert to degrees
        v = 3. * np.sqrt(2.) * np.sqrt(v)
        mean=mog.mean_arr[n]
        mean=mean.reshape(2,1)      
        ell = mpl.patches.Ellipse(mean, v[0], v[1],
                                  180 + angle, color=color)
        ell.set_clip_box(ax.bbox)
        ell.set_alpha(0.3)
        ax.add_artist(ell)
        ax.set_aspect('equal', 'datalim')
        

def plot_2D(mog,X):

    h = plt.subplot(111, aspect='equal')
    make_ellipses(mog, h)
    colors = ['purple','blue','aqua','green','olive']
    labels = pairwise_distances_argmin(X, mog.mean_arr)
    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels, marker='x')
    mean = np.asarray(mog.mean_arr)
    plt.scatter(mean[:,0],mean[:,1],c=colors, marker='x')
    plt.xlim(-7, 2)
    plt.ylim(-7, 7)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()

