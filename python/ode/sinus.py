# Parametry
maxt = 10
dt = 0.1

# Počáteční podmínky
y0 = 0
v0 = 1

# Výsledek
y = [y0]
v = [v0]

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

    yi = yi1
    vi = vi1
    ti = ti1

print(y)
