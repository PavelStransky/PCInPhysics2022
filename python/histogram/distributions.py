import numpy as np
import matplotlib.pyplot as plt

from histogram import histogram

def plot_histogram(data, title="", **kwargs):
    """ Plots data and compares them with theoretic distributionFunction, if specified """
    x, h = histogram(data, **kwargs)

    plt.plot(x, h, label="Histogram")
    plt.title(title)
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\rho$")
    plt.ylim(0)
    plt.show()

def uniform(num_values=100000, num_bins=100):
    """ Histogram of the uniform distribution """
    data = np.random.random(num_values)
    plot_histogram(data, r"Rovnoměrné rozdělení na $\langle0,1\rangle$", num_bins=num_bins, min_value=0, max_value=1, normalize=False)

uniform(100, 100)
