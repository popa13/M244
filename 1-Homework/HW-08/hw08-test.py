import numpy as np
import matplotlib.colors as col
import matplotlib.pyplot as plt
import matplotlib.cm as cm

X = np.arange(-2.5, 2.5, 0.15)
Y = np.arange(-2.5, 2.5, 0.15)
U_dash, V_dash = np.meshgrid(X, Y)

U = U_dash * U_dash
V = U_dash * V_dash

angles = np.arctan2(V, U)
lengths = np.sqrt(np.square(U) + np.square(V))
max_abs = np.max(lengths)
min_abs = np.min(lengths)

norm = col.Normalize(vmin=min_abs, vmax=max_abs, clip=False)
cmap = col.Colormap(lengths)

ax = plt.subplot()
U = U / lengths 
V = V / lengths

q = ax.quiver(X, Y, U, V, [lengths], norm=norm)

t = np.arange(0, 2*3.2, 0.1)
x = 2*np.cos(t)
y = 2*np.sin(t)
ax.plot(x, y)

plt.show()