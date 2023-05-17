# other imports
import numpy
import matplotlib.pyplot as plt
import numpy as np

# import the package
import forcelayout as fl

radius = 20

theta = np.linspace(0, 2*np.math.pi, 30)

x = np.cos(theta) * radius
y = np.sin(theta) * radius
x = x.reshape((30, 1))
y = y.reshape((30, 1))

ds = np.append(x, y, axis = 1)
# ds[4] = [10, 5]


# Need to use the brute force algorithm on a dataset this small
# (not recommended for larger datasets)
layout = fl.draw_spring_layout(dataset=ds, algorithm=fl.SpringForce, iterations = 4, algorithm_highlights = True)


from forcelayout.draw import DrawLayout
dl = DrawLayout(ds, layout)

dl.draw_animated()
plt.show()

