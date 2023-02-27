#!/usr/bin/python
# −∗− coding: utf−8 −∗−

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from math import *

INICIO_INTERVALO = -10
FIN_INTERVALO = 10
INCREMENTO = 0.1


def grafica_atrevete():
	
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	xs = np.arange(INICIO_INTERVALO,FIN_INTERVALO,INCREMENTO)
	ys = np.arange(INICIO_INTERVALO,FIN_INTERVALO,INCREMENTO)
	xs,ys = np.meshgrid(xs,ys)
	ts = 140 + 30*xs**2-50*xs+120*ys**2/(8+xs**2-2*xs+4**ys**2)
	surf = ax.plot_wireframe(xs,ys,ts)
	#surf = ax.plot_surface(xs,ys,zs,rstride=1,cstride=1)
	plt.show()
	return

grafica_atrevete()





