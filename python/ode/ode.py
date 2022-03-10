import numpy as np

def euler_1(model, y, t, dt):
    """ Eulerova metoda 1. řádu """
    y1 = y + model(y, t) * dt
    t1 = t + dt
    return y1, t1

def euler_2(model, y, t, dt):
    """ Eulerova metoda 2. řádu """
    k1 = model(y, t)
    k2 = model(y + k1 * dt, t + dt)

    y1 = y + 0.5 * (k1 + k2) * dt
    t1 = t + dt

    return y1, t1

def ode_solve(model, initial_condition, integrator=euler_1, dt=0.1, maxt=10):
    """ Numerické řešení soustavy diferenciálních rovnic
    
        Argumenty:
            model: pravá strana soustavy DR
            dt: délka kroku
            maxt: koncový čas řešení

        Výsledek:
            pole řešení, pole časů
     """
    yi = np.array(initial_condition)
    ti = 0

    y = [yi]
    t = [ti]

    while ti < maxt:
        yi1, ti1 = integrator(model, yi, ti, dt)

        y.append(yi1)
        t.append(ti1)

        yi = yi1
        ti = ti1

    return np.array(y), np.array(t)