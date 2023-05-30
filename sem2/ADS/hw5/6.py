y, x, theta = [0], [0, 1, 2, 3], 0.2
for k in range(1, len(x)):
    y += [y[k-1] + theta*(x[k]-y[k-1])]
print(*y)