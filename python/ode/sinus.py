import matplotlib.pyplot as plt
import numpy as np
import ode

# Parametry
maxt = 10
dt = 0.01

# Počáteční podmínky
y0 = 0
v0 = 1

def model(y, t):
    x, v = y
    return np.array([v, -x])

y, t = ode.ode_solve(model, [y0, v0], ode.euler_2, dt, maxt)

plt.plot(t, y[:,0], label=f"Řešení DR s dt={dt}")
plt.plot(t, np.sin(t), label="sin(t)")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()