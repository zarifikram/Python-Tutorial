import matplotlib.pyplot as plt
import random
import numpy as np


# radius = random.randint(10, 50)
# theta = np.linspace(0, 2*np.pi, 30)

# X = radius * np.cos(theta)
# Y = radius * np.sin(theta)

# fig, ax = plt.subplots()
# ax.plot(X, Y)
# plt.show()

X = np.linspace(0, np.pi * 4, 40)
fig, axes  = plt.subplots(1, 2)
axes[0].plot(X, np.sin(X))
axes[1].plot(X, np.cos(X))
plt.show()