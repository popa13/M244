#!/usr/bin/python3.6
	# -*coding:utf-8 -*

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# section 16.6, number 12.
"""param = np.linspace(-3.14, 3.14, 100)
u, v = np.meshgrid(param, param)
X = np.cos(u)
Y = np.sin(u)*np.sin(v)
Z = np.cos(v)


# Display the mesh
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.plot_surface(X, Y, Z, color = 'r', alpha = 0.3)#, rstride = 2, cstride = 2)

# Display curve u = constant
for i in np.linspace(-3.14, 3.14, 20):
	u = i*np.ones(50)
	v = np.linspace(-3.14, 3.14, 50)
	X = np.cos(u)
	Y = np.sin(u)*np.sin(v)
	Z = np.cos(v)
	ax.plot(X, Y, Z, color='b')

# Display curve v = constant
for j in np.linspace(-3.14, 3.14, 20):
	v = j*np.ones(50) 
	u = np.linspace(-3.14, 3.14, 50)
	X = np.cos(u)
	Y = np.sin(u)*np.sin(v)
	Z = np.cos(v)
	ax.plot(X, Y, Z, color='g')"""

# Section 16.6, exo 26.
"""paramU = np.linspace(0, 1, 100)
paramV = np.linspace(-3.14, 3.14, 100)
u, v = np.meshgrid(paramU, paramV)
X = u*np.cos(v)
Y = u*np.sin(v)
Z = (u/3)*np.cos(v)

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.set_xlabel('$x$', fontsize=20)
ax.set_ylabel('$y$', fontsize = 20)
ax.set_zlabel('$z$', fontsize = 20)
ax.plot_surface(X, Y, Z, color = 'r', alpha = 0.5)

# Curve when u = constant
for i in np.linspace(0, 1, 10):
	u = i*np.ones(50)
	v = np.linspace(-3.14, 3.14, 50)
	X = u*np.cos(v)
	Y = u*np.sin(v)
	Z = (u/3)*np.cos(v)
	ax.plot(X, Y, Z, color='r')

# Curve when v = constant
for j in np.linspace(-3.14, 3.14, 10):
	v = j*np.ones(50) 
	u = np.linspace(0, 1, 50)
	X = u*np.cos(v)
	Y = u*np.sin(v)
	Z = (u/3)*np.cos(v)
	ax.plot(X, Y, Z, color='r')"""

# Section 16.6, number 38
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlim3d(-5, 1)
ax.set_ylim3d(-3, 3)
ax.set_zlim3d(-3, 3)
ax.set_xlabel('$x$', fontsize=20)
ax.set_ylabel('$y$', fontsize = 20)
ax.set_zlabel('$z$', fontsize = 20)

ax.scatter(-1, -1, -1, color='g')

paramU = np.linspace(-3, 3, 100)
paramV = np.linspace(-3, 3, 100)
u, v = np.meshgrid(paramU, paramV)
X = 1-u**2 - v**2
Y = -v
Z = -u
ax.plot_surface(X, Y, Z, color = 'r', alpha=0.5)

paramU = np.linspace(-0.5, 0.5, 100)
paramV = np.linspace(-0.5, 0.5, 100)
u, v = np.meshgrid(paramU, paramV)
X = -1 - 2*u - 2*v 
Y = -1 - v 
Z = -1 - u
ax.plot_surface(X, Y, Z, color='b', alpha=0.5)

plt.show()