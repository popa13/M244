#!/usr/bin/python3.6
# -*coding:utf-8 -*

import numpy as np 
import matplotlib.pyplot as plt

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
        1) The vector field of Problem 4.\r
        2) The vector field of Problem 6.\r
        3) The vector field of Problem 8.\r
        4) The vector Field of Problem 26.""")
    choice = input("Enter your choice:")
    print(choice)

    if choice == '1':
        # Problem 4
        print("Problem 4")
        x, y = np.meshgrid([-3, -1.5, 0, 1.5, 3], [-3, -1.5, 0, 1.5, 3])
        
        P = y
        Q = x + y
        plt.quiver(x, y, P, Q, width=0.005)

        text = """begin{tabular}{c||c|c|c|c|c} 
        $y, x$ & $-3$ & $-1.5$ & $0$ & $1.5$ & $3$ hlinehline 
        """
        for i in (-3, -1.5, 0, 1.5, 3):
            text += "$" + str(i) + "$ & "
            for j in (-3, -1.5, 0, 1.5, 3):
                if j != 3:
                    text += " $leftlangle " + str(j) + ", " + str(i + j) + " rightrangle$ &"
                else:
                    text += " $leftlangle " + str(j) + ", " + str(i + j) + " rightrangle$"
            text += "hlinehline\n"
        print(text)


        #end = 4
        #division = 5
        #red_vectors = []
        #print(np.linspace(0, end, division))
        #for k in np.linspace(0, end, division):
        #    for j in np.linspace(0, end, division):
        #        red_vectors.append((int(3*k), int(3*j)))

        #print(red_vectors)

        #for i, j in red_vectors:
        #    plt.quiver(x[i, j], y[i, j], P[i, j], Q[i, j], color='red', scale_units='xy', angles='xy', linewidth=0.01, scale=5)

        plt.xlim(-4, 4)
        plt.ylim(-4, 4)
        plt.show()
        print("----------------------------------------------------------")

    elif choice == '2':
        # Example 2
        print("Problem 6")

        x, y = np.meshgrid([-3, -1.5, 0, 1.5, 3], [-3, -1.5, 0, 1.5, 3])
        
        P = y / (np.sqrt(x * x + y * y))
        Q = - x / (np.sqrt(x * x + y * y))
        plt.quiver(x, y, P, Q, width=0.005)

        text = """begin{tabular}{c||c|c|c|c|c} 
        $y, x$ & $-3$ & $-1.5$ & $0$ & $1.5$ & $3$ hlinehline 
        """
        for i in (-3, -1.5, 0, 1.5, 3):
            text += "$" + str(i) + "$ & "
            for j in (-3, -1.5, 0, 1.5, 3):
                d = np.sqrt(j * j + i * i)
                if j != 3:
                    text += " $leftlangle " + "{0:.2f}".format(j/d) + ", " + "{0:.2f}".format(-i / d) + " rightrangle$ &"
                elif j == 0 and i == 0:
                    text += " $notexists &"
                else:
                    text += " $leftlangle " + "{0:.2f}".format(j/d) + ", " + "{0:.2f}".format(-i / d) + " rightrangle$"
            text += "hlinehline\n"
        print(text)
        plt.show()
        print("----------------------------------------------------------")


    elif choice == '3':
        # Newton's Law of Gravitation
        print("Problem 8")
        x, y, z = np.meshgrid(np.linspace(-5,5, 5), np.linspace(-5,5, 5), np.linspace(-5,5, 5))
        P = -0.4*z
        Q = 0
        R = 0
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.quiver(x, y, z, P, Q, R, color = 'black') #length=0.1"
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





