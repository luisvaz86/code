#!/usr/bin/python
# −∗− coding: utf−8 −∗−

from math import *
import matplotlib.pyplot as plt
import csv
import numpy

#declaración variable simbolica R
a= 0.531937827
b= 0.0000597459
NMOLES = 0.002494901


def calculaxBoyle(Bp,Cp,Dp,p):
	x = 0.0
	x = Bp+ Cp*2*p + Dp*3*(p**2)
	return x
	
def conviertePav(R, p , T, Bp,Cp,Dp):
	x = 0.0
	x = (1 + Bp*p + Cp*(p**2) + Dp*(p**3) )/(R*T*p)
	return x
        
def conv_float(f):
	n = 0.0
	try:
		n=float(f)
	except ValueError:
		pass
	return n
	
	
def hallaBoyle(Bp,Cp,Dp,pv):
	
	x = [0.0] * len(pv)
	for i in range (0,len(pv)):
		x[i] = calculaxBoyle( Bp, Cp, Dp, pv[i] )
		print('Para la presion P %5.7f. se obtiene un x de Boyle de %5.7f.'%(pv[i],x[i]))
	return x


n_f = 18
n_c = 18
#Valor de R
R = 8.3144
		
ps= []

plimit = 490000
pinicio = 142500
contador = 0

while (pinicio < plimit):
	ps[contador] = pinicio
	pinicio = pinicio + 5000
	contador = contador +1
	
vs = [0.0] * len(ps)

for i in range(len(ps)):
	ps[i]=ps[i]+(i+1)*multiplicador_p


try:
	
	#descomentar una u otra linea segun se quieran leer diferentes temperaturas y coeficientes del viliar cargas una sisoterma su otras
	with open('isotermastecnicas2.csv', 'rU') as data:
		reader = csv.reader(data,csv.QUOTE_NONNUMERIC)
		datos = list(reader)
		#longitud del array según la entrada por eficiencia
		n_f = len(datos)
		contador_f = 0
		print('Num Fil leidas %d'%(len(datos)))
		val = [0.0] * len(datos)
		for x in datos:
			print('Num col leidas %d'%(len(x)))
	
			#resultados leidos por csv
			val[contador_f] = [0.0] * len(x)
			contador_c = 0
			for y in x:
				val[contador_f][contador_c] = conv_float(y)
				contador_c+=1
			contador_f+=1
	print('\nValores leídos: ')
	print(val)
			
			
except ValueError:
	print 'Error leyendo'
finally:
    data.close()


plt.figure()
ax = plt.subplot(111)


#resultados ejes y e x de ajuste de isotermas, dimensiones inicializadas
pvRT = [0.0] * n_f
x_virial = [0.0] * n_f
	
for i in range(n_f):
	pvRT[i] = [0.0] * len(ps)
	x_virial[i] = [0.0] * len(ps)
	ecboyle = [0.0] * len(ps)

#i número de y que se evalúan
#j numero presiones
for i in range (0, n_f):
		for j in range (0,len(ps)):
			
			#calculo los volumenes correspondientes a las presiones
			v_cal = conviertePav( R, ps[j], val[i][0], val[i][4], val[i][5],val[i][6] )
			
			#calculo x e y del ajuste
			pvRT[i][j] = (ps[j]*v_cal)/(R*val[i][0])
			x_virial[i][j] = 1 + val[i][4]*ps[j] + val[i][5]*(ps[j]**2) + val[i][6]*(ps[j]**3) 

#llamadas funciones y representacion
#Se puede llamar a cualquiera, todo está calculado y cargado previamente

#llamadas para T boyle
bs = hallaBoyle(val[5][4], val[0][5],val[0][6],ps)	
plt.plot(bs,x_virial[0],'r*')
print('T boyle para T = %f'%val[13][0])
plt.title('Curva de Boyle del gas Metano CH4')

#llamadas para isotermas
plt.plot(ps, x_virial[0] , 'b*',ps, x_virial[1] , 'g-', ps, x_virial[2] , 'ro',ps, x_virial[3] , 'b.', ps,x_virial[4], 'go', ps, x_virial[5], 'r.', ps,x_virial[6], 'bo')
print('Temperaturas T = %f %f %f %f %f %f %f'%(val[0][0],val[1][0],val[2][0],val[3][0],val[4][0],val[5][0],val[6][0]))
plt.grid(True)
#plt.title('Isotermas del gas Metano CH4')
plt.legend()
plt.show()

a = numpy.asarray(val)
#escribo los resultados en un archivo csv
numpy.savetxt("salidaisotermas1.csv", a, delimiter=",")
b = numpy.asarray(x_virial)
c = numpy.asarray(pvRT)
#escribo los resultados en un archivo csv
numpy.savetxt("salidaisotermas2.csv", b, delimiter=",")
numpy.savetxt("salidaisotermas3.csv", c, delimiter=",")

	








