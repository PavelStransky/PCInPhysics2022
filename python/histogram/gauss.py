from gettext import npgettext


import numpy as np

def gaussian_distribution(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

def generator_hit_and_miss():
    while True:
        x = 12 * np.random.random() - 6
        y = 0.5 * np.random.random()

        if y < gaussian_distribution(x):
            return x

def generator_clt():
    return sum(np.random.rand(12)) - 6

