#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
from scipy import *
from sympy import *

x = symbols('x')
y = symbols('y')

f= 140 + 30*x**2-60*x+120*y**2/(8+x**2-2*x+4*y**2)

#Primera derivada de f con respecto de x:
f1x = diff(f,x,1)

#Primera derivada de f con respecto de y:
f1y = diff(f,y,1)

print '\n\t\t*********************************************************************************************'
print '\n\t\t*    Atrevete 1.1. Calculo de la temperatura minima de una funcion de dos variables   *******'
print '\n\t\t*********************************************************************************************'
print '\n\n\tDerivada parcial de x respecto de f: ', f1x
print '\n\n\tDerivada parcial de y respecto de f: ', f1y

print '\n\n\tResolviendo sistema de ecuaciones de la derivada con respecto de x e y. Sustituyendo x e y en f para calcular t....'

#Los puntos x0, y0 son la solución del sistema formado por las primeras derivadas de f con respecto de x e y:
solucionf1x_f2y = solve([f1x,f1y],[x,y])



x0 = solucionf1x_f2y[0][0]

y0 = solucionf1x_f2y[0][1]

#LPara conocer z0, sustituyo x0 e y0 en f:
t0 = f.subs( [ (x, solucionf1x_f2y[0][0]) , (y, solucionf1x_f2y[0][1])])

print '\n\n\tCompletado. Punto critico de la funcion P(x, y, T) = P(%d,%d,%d) ' % (x0, y0, t0)

#Calculo las segundas derivadas para la matriz hessiana: 

f2xx = diff(f,x,2)
f2yy = diff(f,y,2)
f2yx = diff(f1y,x,1)
f2xy= diff(f1x,y,1)

#Determinante matriz hessiana:

f2xx_x0y0 = f2xx.subs( [ (x, x0) , (y, y0)])

f2yy_x0y0 = f2yy.subs( [ (x, x0) , (y, y0)])

det_hess = f2xx.subs( [ (x, x0) , (y, y0)])*f2yy.subs( [ (x, x0) , (y, y0)])-f2yx.subs( [ (x, x0) , (y, y0)])*f2xy.subs( [ (x, x0) , (y, y0)])


print '\n\n\tDeterminante matriz hessiana > 0 (%d) --> Hay un maximo o minimo relativo.' % (det_hess)

print '\n\n\tSegunda derivada de f con respecto de x e y son positivas (%d,%d)--> Hay un minimo relativo, en este caso parece absoluto.' % (f2xx_x0y0, f2yy_x0y0 )

print '\n\n\t----> La temperatura minima es, por tanto %d grados centigrados.' % t0


