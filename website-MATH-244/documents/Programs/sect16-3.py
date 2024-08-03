import numpy as np 
import matplotlib.colors as col
import matplotlib.pyplot as plt


choice = 0
quit = False

while quit == False:
	print("""What do you want to plot?\r 
	    1) Gravitational Field.\r
	    2) The vector field from example 2.\r
	    3) The vector field from example 3.""")
	choice = input("Enter your choice:")
	print(choice)

	if choice == '1':
		m = 1
		M = 4
		G = 1
		l = 3
		x, y = np.meshgrid(np.arange(0.25, 3, 0.25), np.arange(0.25, 3,0.25))

		P = -m*M*G*x/(np.sqrt(x**2+y**2))**l
		Q = -m*M*G*y/(np.sqrt(x**2+y**2))**l 
		lengths = np.sqrt(np.square(P) + np.square(Q))
		max_abs = np.max(lengths) / 25
		print(max_abs)
		min_abs = np.min(lengths)
		P = P / lengths 
		Q = Q / lengths

		norm = col.Normalize(vmin=min_abs, vmax=max_abs, clip=False)
		cmap = col.Colormap(lengths)
		ax = plt.subplot()

		ax.quiver(x, y, P, Q, [lengths], norm = norm)

		t = np.arange(0, 1.05, 0.05)
		ax.plot(1.1 + 1.50*t, 1.1 + 1.50*t, 'orange', linewidth=3.5)

		x = 1.1 + 1.50*np.cos(3*np.pi / 2 + t * np.pi / 2)
		y = 2.6 + 1.5*np.sin(3*np.pi / 2 + t * np.pi / 2)
		ax.plot(x, y, 'blue', linewidth=3.5)

		ax.plot([1.1], [1.1], 'o', color='green')
		ax.plot([2.6], [2.6], 'o', color='red')

		plt.show()
		print("----------------------------------------------------------")

	elif choice == '2':
		x, y = np.meshgrid(np.arange(-4, 4, 0.25), np.arange(-4, 4,0.25))

		P = (x - y)
		Q = (x - 2)
		lengths = np.sqrt(np.square(P) + np.square(Q))
		max_abs = np.max(lengths) / 25
		print(max_abs)
		min_abs = np.min(lengths)
		P = P / lengths 
		Q = Q / lengths

		norm = col.Normalize(vmin=min_abs, vmax=max_abs, clip=False)
		cmap = col.Colormap(lengths)
		ax = plt.subplot()

		ax.quiver(x, y, P, Q)
		plt.show()
		print("----------------------------------------------------------")

	elif choice == '3':
		x, y = np.meshgrid(np.arange(-4, 4, 0.25), np.arange(-4, 4,0.25))

		P = 3 + 2*x*y
		Q = x**2 - 3*y**2 
		lengths = np.sqrt(np.square(P) + np.square(Q))
		max_abs = np.max(lengths) / 25
		print(max_abs)
		min_abs = np.min(lengths)
		P = P / lengths 
		Q = Q / lengths

		norm = col.Normalize(vmin=min_abs, vmax=max_abs, clip=False)
		cmap = col.Colormap(lengths)
		ax = plt.subplot()

		ax.quiver(x, y, P, Q)
		plt.show()
		print("----------------------------------------------------------")

	quit = True



