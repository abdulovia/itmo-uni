m = [4, 3, -1, 0.3, 0, 9, 11, 2, -3]
n = len(m)
a = m
for i in range(1, len(a)):
  for j in range(len(a)-i):
    if a[j]>a[j+1]:
      a[j], a[j+1] = a[j+1], a[j]
print(a)
b = m
b.sort()
print(b)

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
x = np.arange(0, 10, 0.1)
plt.plot(x, x**0, label=r'$f_1(n)=1$')
plt.plot([1, 2, 4, 8], [0, 1, 2, 3], label=r'$f_2(n)=\log n$')
plt.xlabel(r'$n$', fontsize=14)
plt.ylabel(r'$f(n)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show()