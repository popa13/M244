#!/usr/bin/python3.6
# -*coding:utf-8 -*

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors

############################################
############################################
#
#   Section 16.1 Homework Problems Fall 2023
#
############################################

choice = 0
quit = False

while quit == False:
    print("""What do you want to plot in Section 16.1?\r 
        1) Part b) of Problem 32.""")
    choice = input("Enter your choice:")
    print(choice)

    if choice == '1':
        print("Problem 32")
        x, y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3,3,20))
        P = x**2 
        Q = x * y
        
        fig, ax = plt.subplots(constrained_layout=True)
        ax.set_aspect(1)

        norm = np.linalg.norm(np.array((P, Q)), axis = 0)
        cbar = fig.colorbar(norm)
        P = P/(8*norm)
        Q = Q/(8*norm)
        ax.quiver(x, y, P, Q, units='xy', scale=0.5, color='black')#units='xy',#length=0.1"
        plt.show()
        print("----------------------------------------------------------")


    elif choice == '4':
        # Example 6: Gradient vector field
        print("Problem 26")
        feature_x = np.arange(-5.0,5.1, .05,)
        feature_y = np.arange(-5.0,5.1, .05,)

        x, y = np.meshgrid(feature_x, feature_y)
        z = 0.5 * (x**2 - y**2)
        fig, ax = plt.subplots(constrained_layout=True)
        ax.set_aspect(1)
        #ax.plot(feature_x, feature_y, c = 'k')
        #CS = ax.contourf(x, y, z, 20, cmap='jet')
        CS2 = ax.contour(x, y, z, 10, cmap='jet')

        cbar = fig.colorbar(CS2)
        #cbar.add_lines(CS2)

        feature_x = np.linspace(-5,5, 15)
        feature_y = np.linspace(-5,5, 15)

        x, y = np.meshgrid(feature_x, feature_y)
        P = x
        Q = -y
        norm = np.linalg.norm(np.array((P, Q)), axis = 0)
        P = P/(4*norm)
        Q = Q/(4*norm)
        ax.quiver(x, y, P, Q, units='xy', scale=0.5, color='black')#units='xy',

        plt.show()
        print("----------------------------------------------------------")


    else:
        print("See ya'!")
        quit = True 





