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
	ax.set_title(u"Variación temperatura con X e Y.")
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Temperatura")
	#Consideraciones de eficiencia
	xs,ys = np.meshgrid(xs,ys)
	
	#función temperatura
	ts = 140 + 30*xs**2-60*xs+120*ys**2/(8+xs**2-2*xs+4*ys**2)
	
	ax.plot_wireframe(xs,ys,ts,rstride=4,cstride=4)
	
	#curvas de nivel con gradiente de colores
	cset = ax.contour(xs,ys,ts,cmap=cm.coolwarm, offset=0)

	x0=1
	y0=0
	z0=110
	#Marco el mínimo de la función en en rojo
	ax.scatter(x0, y0, z0, c='red', s=50, alpha=0.5)

	plt.show()
	return

grafica_atrevete()





