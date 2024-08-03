#!/usr/bin/python3.6
# -*coding:utf-8 -*

# importing libraries
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pylab as pl
from mpl_toolkits.mplot3d import Axes3D

# defining surface and axes
def fct(xx, yy):
	return np.sqrt(4-yy**2)

def fctTwo(xx, zz):
	return xx/2

plt.figure()

# syntax for 3-D plotting
ax = plt.axes(projection ='3d')

# Plot 1
x = np.linspace(-1, 5, 120)
y = np.linspace(0, 2, 120)

X, Y = np.meshgrid(x, y)
Z1 = fct(X, Y)
ax.plot_surface(X, Y, Z1, color='r', alpha=0.8, rstride=1, cstride = 1)

# Plot 2
x = 4*np.ones(100)
y = np.linspace(0, 2, 100)
z = fct(x, y)

ax.add_collection3d(pl.fill_between(y, 0, z, color='b', alpha=0.3), zs=4, zdir='x')

# Plot 3
y = np.linspace(0, 2, 100)
x = np.linspace(0, 4, 100)
z = np.sqrt(4 - x**2/4)

ax.plot3D(x, y, z, color='b')

for i in np.linspace(0, 1, 100):
	z = i*np.sqrt(4 - x**2/4)
	ax.plot3D(x, y, z, color='b', alpha=0.3)

# Plot 4
for i in np.linspace(0, 2, 100):
	y = i*np.ones(100)
	x = np.linspace(2*i, 4, 100)
	z = np.sqrt(4-i**2)*np.ones(100)
	ax.plot3D(x, y, z, color='b', alpha=0.3)

# Plot 5
x = np.linspace(0, 4, 100)
y = 0*np.ones(100)
for i in np.linspace(0, 2, 100):
	z = i*np.ones(100)
	ax.plot3D(x, y, z, color='b', alpha=0.3)

# plot 5
x = np.linspace(0, 4, 100)
z = np.linspace(0, 2, 100)
X, Z = np.meshgrid(x, z)
Y2 = fctTwo(X, Z)
ax.plot_surface(X, Y2, Z, color='r', alpha=0.7, rstride=1, cstride=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()