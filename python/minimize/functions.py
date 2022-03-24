import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm           # Colour maps for the contour graph

import minimize

def f(X):
    """ Quadratic test function """ 
    x, y = X
    return x*x + y*y


def g(X, parameters=(1, 100)):
    """ Rosenbrock test function """
    x, y = X
    a, b = parameters
    return (a - x)**2 + b * (y - x * x)**2

def w(X):
    x, y = X
    return x**4 - 2 * x**2 + x + y**2

def v(X):
    x, y = X
    return np.sin(3 * x) * np.sin(3 * y)

def minimize_and_plot(fnc, box_size=2, num_contours=100, **kwargs):
    path = minimize.minimize_metropolis(fnc, initial_condition=(0, 0), **kwargs)

    print("Position of the minimum:", path[-1])
    print(f"Minimum value of function {fnc.__name__}:", fnc(path[-1]))

    x = y = np.linspace(-box_size, box_size, 100)# Range of x and y values for the graph

    X, Y = np.meshgrid(x, y)                     # Grid for calculating values of the function
    Z = fnc([X, Y])

    plt.contourf(X, Y, Z, num_contours, cmap=cm.hot)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.colorbar(label=fnc.__name__ + '(x,y)')  # Legend for the contour graph
    plt.plot(path[:,0], path[:,1])
    plt.show()

minimize_and_plot(v, temperature=1, max_steps=100000, step_size=0.01)