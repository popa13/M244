import numpy as np 
import matplotlib.pyplot as plt

############################################
############################################
#
#   Midterm 03
#
############################################

choice = 0
quit = False

while quit == False:
    print("""What do you want to plot?\r 
        1) Question 2 a).\r
        2) Question 2 b).\r
        3) Newton's Law of Gravitation.\r
        4) Gradient field from Example 6.""")
    choice = input("Enter your choice:")
    print(choice)

    if choice == '1':
        # Example 1
        print("Question 2a")
        x, y = np.meshgrid(np.linspace(-5, 5, 15), np.linspace(-5,5, 15))
        P = x
        Q = x + 2
        
        plt.quiver(x, y, P, Q)
        plt.show()
        print("----------------------------------------------------------")

    elif choice == '2':
        # Example 2
        print("Question 2b")
        x, y = np.meshgrid(np.linspace(-5, 5, 15), np.linspace(-5,5, 15))
        P = x - y
        Q = x
        
        plt.quiver(x, y, P, Q)
        plt.show()
        print("----------------------------------------------------------")

    else:
        print("See ya'!")
        quit = True 