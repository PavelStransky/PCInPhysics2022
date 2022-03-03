import numpy as np

def euler_1(model, y, t, dt):
    y1 = y + model(y, t) * dt
    t1 = t + dt
    return y1, t1

def ode_solve(model, initial_condition, dt=0.1, maxt=10):
    # Nultý krok
    yi = np.array(initial_condition)
    ti = 0

    y = [yi]
    t = [ti]

    while ti < maxt:
        yi1, ti1 = euler_1(model, yi, ti, dt)

        y.append(yi1)
        t.append(ti1)

        yi = yi1
        ti = ti1

    return np.array(y), np.array(t)