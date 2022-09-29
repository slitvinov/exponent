import math
import matplotlib.pylab as plt
import numpy as np
import random


def sample():
	x = 0
	while True:
		Y1 = Y = random.uniform(0, 1)
		odd = True
		while True:
			Yp = random.uniform(0, 1)
			if Y <= Yp:
				if odd:
					return Y1 + x
				else:
					x += 1
					break
			else:
				Y = Yp
				odd = not odd


hi = 4
T = 10000
S = [sample() for i in range(T)]
X = np.linspace(0, hi, 100)
plt.hist(S, 20, range=[0, hi], density=True, fill=False, color='k')
plt.plot(X, [math.exp(-x) for x in X], '-k')
plt.show()
