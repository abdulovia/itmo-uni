x = [-1.983, -1.544, -1.106, -0.667, -0.229, 0.209, 0.648, 1.087, 1.525, 1.964]
p = [0.02, 0.055, 0.14, 0.11, 0.19, 0.165, 0.16, 0.085, 0.055, 0.02]
xn = 0
for i in range(10):
    xn += x[i]*p[i]
print(xn)
sn = 0
for i in range(10):
    sn += x[i]**2*p[i]-xn**2
print(sn)
xn4, xn3, xn2 = 0, 0, 0
for i in range(10):
    xn4 += x[i]**4*p[i]
    xn3 += x[i]**3*p[i]
    xn2 += x[i]**2*p[i]
delta = xn4 - 4*xn3*xn+8*xn2*xn**2-4*xn**4-xn2**2
print(delta)