import matplotlib.pyplot as plt

# Parametry
maxt = 100
dt = 0.001

# Počáteční podmínky
y0 = 0
v0 = 1

# Výsledek
y = [y0]
v = [v0]
t = [0]

# Nultý krok
yi = y0
vi = v0
ti = 0

while ti < maxt:
    yi1 = yi + vi * dt
    vi1 = vi - yi * dt
    ti1 = ti + dt

    y.append(yi1)
    v.append(vi1)
    t.append(ti1)

    yi = yi1
    vi = vi1
    ti = ti1

plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')
plt.show()