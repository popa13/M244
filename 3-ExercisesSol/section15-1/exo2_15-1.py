#!/usr/bin/python3.6
# -*coding:utf-8 -*

# importing libraries
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pylab as pl
from mpl_toolkits.mplot3d import Axes3D

def fct(x,y):
	return 1-x*y**2

def RieSum00(xinf, xsup, yinf, ysup, m, n):
	print("Lower right corners")
	dx = (xsup - xinf)/m
	dy = (ysup - yinf)/n

	somme = 0
	for i in np.linspace(1,m, m):
		for j in np.linspace(0, n-1, n):
			x = xinf + i*dx
			y = yinf + j*dy
			print("(" + str(x) + "," + str(y) + ")")
			somme = somme + fct(x, y)

	print("Approximate value = " + str(somme*dx*dy))
	print("--------------------------------------------")

	return somme*dx*dy

def RieSum01(xinf, xsup, yinf, ysup, m, n):
	print("Upper left corners")
	dx = (xsup - xinf)/m
	dy = (ysup - yinf)/n

	somme = 0
	for i in np.linspace(0,m-1, m):
		for j in np.linspace(1, n, n):
			x = xinf + i*dx
			y = yinf + j*dy
			print("(" + str(x) + "," + str(y) + ")")
			somme = somme + fct(x, y)

	print("Approximate value = " + str(somme*dx*dy))
	print("-------------------------------------------")

RieSum00(0, 4, -1, 2, 2, 3)
RieSum01(0, 4, -1, 2, 2, 3)

