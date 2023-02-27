
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import * 
from numpy import *
from scipy.integrate import quad
#import matplotlib.pyplot as plt


#Nombre de los gases ideales
nombre_gis = ['Ne']

#Valores en S.I.

#Constante de Boltzman:
KB = 1.38064852*(10**(-23))

#Valor en Kg de la Masa molar gas
masas_gis = [0.0201797]

#Valor Constante R gases ideales en J*/(k*mol)
R = 8.314472

#Temperaturas en K
ts = [317.15,1117.15,786.15]

#Velocidad media, velocidad mas probable, y velocidad cuadratica media (m/s)
vm = [0.0]*(len(ts))
vmp = [0.0]*(len(ts))
vcm = [0.0]*(len(ts))

#Energia media, energia mas probable, y energia cuadratica media (m/s)
em = [0.0]*(len(ts))
emp = [0.0]*(len(ts))
ecm = [0.0]*(len(ts))



def integrandoVelocidad(v, R, T, M):
	return ((v**4)*(e**(-M*(v**2))))/(2*R*T)

def integrandoEnergia(E, KB, T, factor):
	return (e**(-E/(KB*T)))*(E**(factor))

def integrandoFuncionVelocidad(v, R, T, M):
	return (e**( (-M*(v**2))/(2*R*T)))*(v**2)

def integrandoFuncionEnergia(E, KB, T):
	return (e**( (-E/(KB*T))))*(E**(1/2))

mul_vcm = 0.0
for m in range(len(masas_gis)):
	for t in range(len(ts)):
		vm[t] = (8*R*ts[t]/masas_gis[m])**(1/2)
		vmp[t] = ((2*R*ts[t])/masas_gis[m])**(1/2)
		mul_vcm = 4*pi*((masas_gis[m]/(2*pi*ts[t]*R))**(3/2))
		lim_integral_vcm = quad(integrandoVelocidad, 0, inf, args=(R,ts[t],masas_gis[m]))
		vcm[t] = mul_vcm*(lim_integral_vcm[0]-lim_integral_vcm[1])

mul_ecm = 0.0
factor_ecm = 2.5
factor_em = 1.5
for m in range(len(masas_gis)):
	for t in range(len(ts)):
		emp[t] = (KB*ts[t])/2
		mul_ecm = 2*pi*((1/(pi*KB))**(3/2))
		lim_integral_ecm = quad(integrandoEnergia, 0, inf, args=(KB,ts[t],factor_ecm))
		lim_integral_em = quad(integrandoEnergia, 0, inf, args=(KB,ts[t],factor_em))
		ecm[t] = mul_ecm*(lim_integral_ecm[0]-lim_integral_ecm[1])
		em[t] = mul_ecm*(lim_integral_em[0]-lim_integral_em[1])


for m in range(len(masas_gis)):
	for t in range(len(ts)):
		print('Para el gas %s y la temperatura %.2f K se han calculado las siguientes velocidades -en m/s-:' % (nombre_gis[m],ts[t]))
		print('Velocidad media: %.12f'% (vm[t]))
		print('Velocidad mas probable: %.12f'% (vmp[t]))
		print('Velocidad cuadratica media: %.12f'% (vcm[t]))
		print('\n\n')

for m in range(len(masas_gis)):
	for t in range(len(ts)):
		print('Para el gas %s y la temperatura %.2f K se han calculado las siguientes energias -en J-:' % (nombre_gis[m],ts[t]))
		print('VEnergia media: %.25f' % (em[t]))
		print('Energia mas probable: %.25f' % (emp[t]))
		print('Energia cuadratica media: %.25f' % (ecm[t]))
		print('\n\n')


#Valores para la funcion de la velocidad, se escriben en un archivo .csv

#Temperaturas en K
xe = arange(-10, 10, 0.25)

ye1 = [0.0]*len(xe)
ye2 = [0.0]*len(xe)
ye3 = [0.0]*len(xe)

for i in range(len(xe)):
	mul1_vcm = ((masas_gis[0]/(2*pi*R*ts[0]))**(3/2))*4*pi
	e_int1 = quad(integrandoFuncionVelocidad, 0, xe[i], args=(R,ts[0],masas_gis[0]))
	ye1[i] = mul1_vcm * (e_int1[0]-e_int1[1])
	mul2_vcm = ((masas_gis[0]/(2*pi*R*ts[1]))**(3/2))*4*pi
	e_int2 = quad(integrandoFuncionVelocidad, 0, xe[i], args=(R,ts[1],masas_gis[0]))
	ye2[i] = mul2_vcm * (e_int2[0]-e_int2[1])
	mul3_vcm = ((masas_gis[0]/(2*pi*R*ts[2]))**(3/2))*4*pi
	e_int3 = quad(integrandoFuncionVelocidad, 0, xe[i], args=(R,ts[2],masas_gis[0]))
	ye3[i] = mul3_vcm * (e_int3[0]-e_int3[1])
"""
ae = asarray(xe)

be = asarray(ye1)
ce = asarray(ye2)
de = asarray(ye3)


#escribo los resultados en un archivo csv
savetxt("salidaXvelocidades.txt", ae, delimiter=",")
savetxt("salidaY1velocidades.txt", be, delimiter=",")
savetxt("salidaY2velocidades.txt", ce, delimiter=",")
savetxt("salidaY3velocidades.txt", de, delimiter=",")

"""

#Energias en J
xe = arange(1*(10**(-21)), 1*(10**(-19)), 0.01*(10**(-21)))

ye1 = [0.0]*len(xe)
ye2 = [0.0]*len(xe)
ye3 = [0.0]*len(xe)

for i in range(len(xe)):
	mul1_vcm = 2*pi*(((1/(KB*ts[0])))**(3/2))
	e_int1 = quad(integrandoFuncionEnergia, 0, xe[i], args=(KB,ts[0]))
	ye1[i] = mul1_vcm * (e_int1[0]-e_int1[1])
	mul2_vcm = 2*pi*(((1/(KB*ts[1])))**(3/2))
	e_int2 = quad(integrandoFuncionEnergia, 0, xe[i], args=(KB,ts[1]))
	ye2[i] = mul2_vcm * (e_int2[0]-e_int2[1])
	mul3_vcm = 2*pi*(((1/(KB*ts[2])))**(3/2))
	e_int3 = quad(integrandoFuncionEnergia, 0, xe[i], args=(KB,ts[2]))
	ye3[i] = mul3_vcm * (e_int3[0]-e_int3[1])

"""
ae = asarray(xe)

be = asarray(ye1)
ce = asarray(ye2)
de = asarray(ye3)

#escribo los resultados en un archivo csv
savetxt("salidaXenergias.txt", ae, delimiter=",")
savetxt("salidaY1energias.txt", be, delimiter=",")
savetxt("salidaY2energias.txt", ce, delimiter=",")
savetxt("salidaY3energias.txt", de, delimiter=",")
"""

		
