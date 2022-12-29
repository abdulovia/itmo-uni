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


plt.figure(figsize=(10, 5))
x = np.arange(0, 8, 1)
plt.plot(x, x**2, label=r'$f_1(n)=n^2$')
plt.plot(x, 2**x, label=r'$f_2(n)=2^n$')
plt.xlabel(r'$n$', fontsize=14)
plt.ylabel(r'$f(n)$', fontsize=14)
plt.grid(True)
plt.legend(loc='best', fontsize=12)
plt.savefig('figure_with_legend.png')
plt.show()