import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

############################################################################################
# First example of the sphere
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.set_xlim3d(-1.1, 1.1)
ax.set_ylim3d(-1.1,1.1)
ax.set_zlim3d(-1.1, 1.1)

parametrization = 3

if parametrization == 1:
	#Parametrization with cartesian...
	param = np.linspace(-1, 1, 35) 
	N = len(param)
	x, y = np.meshgrid(param, param)
	Ztop = np.zeros_like(x)
	for i in np.arange(1, N, 1):
		u = param[i]
		for j in np.arange(1, N, 1):
			v = param[j]
			n = u**2 + v**2 
			v = param[j]
			if n <= 1:
				Ztop[i, j] = np.sqrt(1 - n)
			else:
				Ztop[i, j] = np.nan
	Zbottom = -Ztop  
	ax.plot_surface(x, y, Ztop, color='r', alpha=.75)
	ax.plot_surface(x, y, Zbottom, color='r', alpha=.5)
	ax.set_zlim(-1.1, 1.1)
	plt.show()
if parametrization == 2:
	# Parametrization with polar...
	param = np.linspace(0, 2*np.pi, 25) 
	radius = np.linspace(0, 1, 25)
	THETA, RADIUS = np.meshgrid(param, radius)
	x = RADIUS * np.cos(THETA)
	y = RADIUS * np.sin(THETA)
	Ztop = np.sqrt(1 - RADIUS**2)
	Zbottom = -Ztop
	ax.plot_surface(x, y, Ztop, color='r', alpha=1)
	ax.plot_surface(x, y, Zbottom, color='r', alpha=1)
else:
	# Parametrization with Spherical...
	paramLo = np.linspace(0, 2*np.pi,25)
	paramLa = np.linspace(0, np.pi,25)

	theta, phi = np.meshgrid(paramLo, paramLa)
	x = np.cos(theta)*np.sin(phi)
	y = np.sin(theta)*np.sin(phi)
	z = np.cos(phi)
	ax.plot_surface(x, y, z, color='r', alpha=1)

plt.show()

#############################################################################################

#############################################################################################
# Exercise 7
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

param = np.linspace(-1, 1, 25)
u, v = np.meshgrid(param, param)
X = u**2 
Y = v**2
Z = u + v 

ax.plot_surface(X, Y, Z, color = 'r', alpha=1)

# Display curve u = u_0
"""paramU = np.linspace(-1,1, 10)
for u in paramU:
	v = np.linspace(-1, 1, 25)
	X = u**2 * np.ones_like(v)
	Y = v**2 
	Z = u + v
	ax.plot(X, Y, Z, color='b')"""

# Display curve v = v_0
"""paramV = np.linspace(-1, 1,10)
for v in paramV:
	u = np.linspace(-1, 1, 25)
	X = u**2 
	Y = v**2 * np.ones_like(u)
	Z = u + v 
	ax.plot(X, Y, Z, color='g')"""

plt.show()

############################################################################################
# Exercise 37

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

u = np.linspace(0, 2, 25)
v = np.linspace(0, 2*np.pi, 25)
U, V = np.meshgrid(u, v) 

X = U**2
Y = 2*U*np.sin(V)
Z = U*np.cos(V)
ax.plot_surface(X, Y, Z, color='r')

u = np.linspace(-1,1,25)
v = np.linspace(-1, 1, 25)
U, V = np.meshgrid(u, v)
X = 1 + 2*U  
Y = 2*V
Z = 1 + U 
ax.plot_surface(X, Y, Z, color='b', alpha=0.75)

plt.show()
