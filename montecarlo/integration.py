import numpy as np

def f(x):
    return np.exp(-x) * np.sin(x)

def g(x):
    return np.sin(x**2) / np.sqrt(1 + x**4)

def integrate(f, a, b, n=10000):
    x = np.random.uniform(a, b, n)
    i = (b - a) * np.average(f(x))
    return i

def integrateh(n=10000):
    hits = 0
    result = 0

    for _ in range(n):
        x, y, v, w = np.random.uniform(0, 1, 4)

        if(x - 0.5)**2 + (y - 0.5)**2 + (v - 0.5)**2 + (w - 0.5)**2 <= 0.25:
            hits += 1
            result += np.sin(np.sqrt(np.log(x + y + v + w + 2)))

    volume = hits / n
    result = result / hits * volume

    print(f"I3 = {result} (number of hits: {hits}, volume of the integration region: {volume})")

def heart(phi):
    return np.sin(phi)**3, (13 * np.cos(phi) - 5 * np.cos(2 * phi) -2 * np.cos(3 * phi) - np.cos(4 * phi)) / 16

def integrateHeart(n=10000):
    hits = 0
    result = 0

    bounds = 1.1

    for _ in range(n):
        x, y = np.random.uniform(-bounds, bounds, 2)

        phi = np.arctan2(y, x)
        bx, by = heart(phi)
        if x*x + y*y < bx*bx + by*by:
            hits += 1
            result += np.exp((x**2 + y**2) / 2)

    volume = (2 * bounds)**2 * hits / n
    result = result / hits * volume / (2 * np.pi)

    print(f"Iheart = {result} (number of hits: {hits}, volume of the integration region: {volume})")

#print(integrate(f, 0, 2*np.pi, n=100000000))
#print(integrate(g, 0, np.sqrt(10*np.pi), n=100000000))
#integrateh(n=1000000)

#integrateHeart(1000000)