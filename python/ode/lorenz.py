import matplotlib.pyplot as plt
import numpy as np
import ode

from scipy.integrate import odeint

# Parametry
maxt = 100
dt = 0.01

# Počáteční podmínky
x0 = 1
y0 = 1
z0 = 1

sigma = 10
rho = 28
beta = 8 / 3

def lorenz(w, t):
    x, y, z = w

    return np.array([
        sigma * (y - x),
        x * (rho - z) - y,
        x * y - beta * z
    ])

# Řešení pomocí naprogramovaného integrátoru diferenciálních rovnic
# w, ts = ode.ode_solve(lorenz, [x0, y0, z0], ode.euler_2, dt, maxt)

# Řešení pomocí knihovny scipy
ts = np.arange(0, maxt, dt)
w = odeint(lorenz, [x0, y0, z0], ts)

plt.plot(w[:,0], w[:,2], label=f"Řešení DR s dt={dt}")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()