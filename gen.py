#!/usr/bin/python

import sys
import Tkinter as tk
import tktable as tkt
from numpy import *
import math
import random


#variables globales
sa_x=[]
sa_y=[]
sa_v=[]
sa_w=[]
x_entabla=[0,0,0,0]
y_entabla=[0,0,0,0]
w_entabla=[0,0,0,0]
v_entabla=[0,0,0,0]
z_entabla=[0,0,0,0,0]
porcentaje_z=[0,0,0,0]
aleatorios_tabla=[0,0,0,0]
z_acumulado=[0,0,0,0]
igual=[]
signo=["" for x in range(5)]
z=[]
maximos=[]
minimos=[]
Bits_Precision=[]
mjs=[]
poblacion=[]
veredicto=[0,0,0,0]

raiz=tk.Tk()
raiz.title("Algoritmos geneticos")




def Minimizar():
	print "hola"

def ImprimeArreglos():
	print "EN X: "
	for i in range(len(sa_x)):
		print sa_x[i].get(),
	print ""
	print "EN Y: "
	for i in range(len(sa_y)):
		print sa_y[i].get(),
	print ""
	print "EN V: "
	for i in range(len(sa_v)):
		print sa_v[i].get(),
	print ""
	print "EN W: "
	for i in range(len(sa_w)):
		print sa_w[i].get(),
	print ""
	print "EN SIGNOS: "
	print signo
	print "EN INDEPENDIENTE: "
	for i in range(len(igual)):
		print igual[i].get(),
	print ""
	print "Funcion objetivo"
	for i in range(len(z)):
		print z[i].get(),
	print ""

	print "En minimos"
	for i in range(len(minimos)):
		print minimos[i]
	print ""
	print "En maximos"
	for i in range(len(maximos)):
		print maximos[i]
	print ""
	print "En MJS"
	for i in range(len(mjs)):
		print mjs[i]
	print ""
	print "En Poblacion"
	for i in range(len(poblacion)):
		print poblacion[i]
	print ""
	print "En Tabla x"
	for i in range(len(x_entabla)):
		print x_entabla[i]
	print ""
	print "En Tabla y"
	for i in range(len(y_entabla)):
		print y_entabla[i]
	print ""
	print "En Tabla w"
	for i in range(len(w_entabla)):
		print w_entabla[i]
	print ""
	print "En Tabla v"
	for i in range(len(v_entabla)):
		print v_entabla[i]
	print ""
	print "En Tabla z"
	for i in range(len(z_entabla)):
		print z_entabla[i]
	print ""
	print "Porcentaje en z"
	for i in range(len(porcentaje_z)):
		print porcentaje_z[i]
	print ""
	print "Z acumulativo"
	for i in range(len(z_acumulado)):
		print z_acumulado[i]
	print ""
	print "Aleatorios"
	for i in range(len(aleatorios_tabla)):
		print aleatorios_tabla[i]
	print ""
	print ""
	print "Nueva poblacion"
	for i in range(len(veredicto)):
		print veredicto[i]
	print "Numero de bits de precision"
	for i in range(len(Bits_Precision)):
		print Bits_Precision[i].get()
	print ""

	#print sa_y
	#print sa_v
	#print sa_w
	#print igual
	#print signo

def Maximizar():
	############INICIO ALGORITMO################
	#Obtengo los maximos y minimos de cada variable asi como sus mjs
	for i in range(len(z)):
		if z[i].get()!="":
			minimos.append(Minimo(i))
			maximos.append(Maximo(i))
			mjs.append(Calcula_mj(minimos[i],maximos[i]))
	
	#creo 4 vectores de poblacion
	
	for i in range(4):
		poblacion.append(NuevoVector())
		SeleccionNatural(i) ##i

	#obtengo los valores de los vectores que sobrevivieron para la tabla
	for i in range(4):
		Variable_enTabla(i)
		Evalua_Z_enTabla(i)

	Sumatoria_Z()
	Porcientos()
	AcumulativoZ()
	Aleatorios()
	for i in range(4): #Para cada vector de la poblacion
		SegundaSeleccion(i) #Checo cuales vectores sobreviven para mutaciones y cruzas y cuales no
	ImprimeArreglos()#Imprimo los valores que llevo hasta el momento


	#OBTENER VALOR DE Z PARA LA TABLA

	#Configuraciones basicas
	otra_ventana=tk.Toplevel()
	vent=tk.Frame(otra_ventana)
	raiz.withdraw()
	vent.grid(column=0, row=0,padx=(50,50), pady=(10,10))
	vent.columnconfigure(0,weight=1)
	vent.rowconfigure(0,weight=1)


	Boton_salir=tk.Button(vent,text="Salir", command=fin)
	Boton_salir.grid(column=1,row=1)
	
	Tabla=tkt.Table(vent,rows=5,cols=5)
	Tabla.grid(column=1, row=3)
	otra_ventana.mainloop()
	#vs=tk.Frame(otra_ventana)

def SegundaSeleccion(idVector):
	acumulador=0
	ordenados=z_acumulado
	ordenados.sort()
	print ordenados[3],
	print "<",
	print aleatorios_tabla[idVector]
	if ordenados[3]<aleatorios_tabla[idVector]:
		veredicto[idVector]="Hijo/Mutacion"
	else:
		#Buscar dentro de que rango esta el aleatorio y guardar el valor del rango
		"""
			Si el mayor inmediato es 0.9 entonces guarda en acumulador 0.9
		"""
		if aleatorios_tabla[idVector]<ordenados[3]:
			acumulador=ordenados[3]
		if aleatorios_tabla[idVector]<ordenados[2]:
			acumulador=ordenados[2]
		if aleatorios_tabla[idVector]<ordenados[1]:
			acumulador=ordenados[1]
		if aleatorios_tabla[idVector]<ordenados[0]:
			acumulador=ordenados[0]
		#ahora que se dentro de que rango esta, busco a que vector corresponde
		#el valor de acumulador
		for i in range(len(z_acumulado)):
			if z_acumulado[i]==acumulador:
				veredicto[idVector]=i

def Aleatorios():
	for i in range(4):
		aleatorios_tabla[i]=random.uniform(0, 1)

def AcumulativoZ():
	z_acumulado[0]=0
	for i in range(1,4):
		z_acumulado[i]=z_acumulado[i-1]+porcentaje_z[i]

def Porcientos():
	for i in range(4):
		porcentaje_z[i]=float(z_entabla[i])/float(z_entabla[4])

def Sumatoria_Z():
	acumulador=0
	for i in range(len(z_entabla)-1):
		acumulador+=float(z_entabla[i])
	z_entabla[4]=acumulador

def Evalua_Z_enTabla(idVector):
	acumulador=0
	if z[0].get()!="":
		#print x_entabla[idVector]
		acumulador+=int(z[0].get())*float(x_entabla[idVector])
	if z[1].get()!="":
		#print z[1].get()
		acumulador+=int(z[1].get())*float(y_entabla[idVector])
	if z[2].get()!="":
		#print z[2].get()
		acumulador+=int(z[2].get())*float(w_entabla[idVector])
	if z[3].get()!="":
		#print z[3].get()
		acumulador+=int(z[3].get())*float(v_entabla[idVector])
	z_entabla[idVector]=acumulador

def Variable_enTabla(idVector):
	strings=[]
	acumulador=0
	for i in range(len(z)):
		if z[i].get()!="":
			#obtener x,y,w,v del vector
			strings.append(poblacion[idVector][acumulador:acumulador+int(mjs[i])])
			acumulador+=int(mjs[i])
	if len(minimos)>0 and len(strings)>0 and len(maximos)>0 and len(mjs)>0:
		x_entabla[idVector]=float(minimos[0])+int(strings[0],2)*((float(maximos[0])-float(minimos[0])))/(2**int(mjs[0])-1)
	if len(minimos)>1 and len(strings)>1 and len(maximos)>1 and len(mjs)>1:
		y_entabla[idVector]=float(minimos[1])+int(strings[1],2)*((float(maximos[1])-float(minimos[1])))/(2**int(mjs[1])-1)
	if len(minimos)>2 and len(strings)>2 and len(maximos)>2 and len(mjs)>2:
		w_entabla[idVector]=float(minimos[2])+int(strings[2],2)*((float(maximos[2])-float(minimos[2])))/(2**int(mjs[2])-1)
	if len(minimos)>3 and len(strings)>3 and len(maximos)>3 and len(mjs)>3:
		v_entabla[idVector]=float(minimos[3])+int(strings[3],2)*((float(maximos[3])-float(minimos[3])))/(2**int(mjs[3])-1)



def SeleccionNatural(idVector):
	vivio=0
	while not vivio==len(igual):
		vivio=0
		strings=[]
		acumulador=0
		#print poblacion[idVector]
		for i in range(len(z)):
			if z[i].get()!="":
				#obtener x,y,w,v del vector
				strings.append(poblacion[idVector][acumulador:acumulador+int(mjs[i])])
				acumulador+=int(mjs[i])
		#print "Variables",
		#print strings

		sobrevive=0
		valor=0
		for i in range(len(igual)):
			#evaluo el polinomio
			if len(strings)>0:
				#print "entre a 0"
				if sa_x[i].get()!="" and strings[0]!="" and minimos[0]!="" and mjs[0]!="":
					#print  int(sa_x[i].get()),
					#print "*",
					#print  int(strings[0],2)

					valor_procedimiento=float(minimos[0])+int(strings[0],2)*((float(maximos[0])-float(minimos[0])))/(2**int(mjs[0])-1)
					#print "valor procedimiento:",
					#print valor_procedimiento
					valor+=int(sa_x[i].get())*valor_procedimiento
			if len(strings)>1:
				#print "entre a 1"
				if sa_y[i].get()!="" and strings[1]!="" and minimos[1]!="" and mjs[1]!="":
					#print  int(sa_y[i].get()),
					#print "*",
					#print  int(strings[1],2)
					valor_procedimiento=float(minimos[1])+int(strings[1],2)*((float(maximos[1])-float(minimos[1])))/(2**int(mjs[1])-1)
					#print "valor procedimiento:",
					#print valor_procedimiento
					valor+=int(sa_y[i].get())*valor_procedimiento
			if len(strings)>2:
				#print "entre a 2"
				if sa_w[i].get()!="" and strings[2]!="" and minimos[2]!="" and mjs[2]!="":
					#print  int(sa_w[i].get()),
					#print "*",
					#print  int(strings[2],2)
					valor_procedimiento=float(minimos[2])+int(strings[2],2)*((float(maximos[2])-float(minimos[2])))/(2**int(mjs[2])-1)
					#print "valor procedimiento:",
					#print valor_procedimiento
					valor+=int(sa_w[i].get())*valor_procedimiento
			if len(strings)>3:
				#print "entre a 3"
				if sa_v[i].get()!="" and strings[3]!="" and minimos[3]!="" and mjs[3]!="":
					#print  int(sa_v[i].get()),
					#print "*",
					#print  int(strings[3],2)
					valor_procedimiento=float(minimos[3])+int(strings[3],2)*((float(maximos[3])-float(minimos[3])))/(2**int(mjs[3])-1)
					#print "valor procedimiento:",
					#print valor_procedimiento
					valor+=int(sa_v[i].get())*valor_procedimiento
			#print "VALOR:",
			#print valor
		
			#checo el signo 
			if signo[i]=="<=":
				#print signo[i],
				#print igual[i].get()
				if valor <= int(igual[i].get()):
					sobrevive=1
			elif signo[i]==">=":
				#print signo[i],
				#print igual[i].get()
				if valor>=int(igual[i].get()):
					sobrevive=1
			else:
				#print signo[i],
				#print igual[i].get()
				if valor==int(igual[i].get()):
					sobrevive=1
			if sobrevive==1:
				#print "sobrevive"
				sobrevive=0
				vivio+=1
			else:
				break
				#print "muere!"

		if vivio==len(igual):
			return poblacion[idVector]
		else:
			poblacion[idVector]=NuevoVector()
	

def NuevoVector():
	aux=0
	vector=[]

	for i in range(len(z)):
		if z[i].get()!="":
			#print "mjs: ",
			#print mjs[i]
			aux=random.randrange((2**int(mjs[i])))
			#print "Aux",
			#print bin(aux)[2:]
			if len(bin(aux)[2:])!=int(mjs[i]):
				#print "entre"
				ceros=int(mjs[i])-len(bin(aux)[2:])
				for l in range(ceros):
					vector.append("0")
			vector.append(bin(aux)[2:])
	string_vector=''.join(vector)
	return string_vector
	#print "Nuevo vector",
	
	#print vector

	#for i in range(len(vector)):
	#	print vector[i],
	#print ""
	#primero genero un numero aleatorio por cada variable
	


def Calcula_mj(minimo,maximo):
	aux=maximo-minimo
	aux*=10**int(Bits_Precision[0].get())
	auxb=aux
	aux=round(math.log(aux)/math.log(2))

	#verificamos que cumplan las condifciones#
	if 2**(aux-1)<=auxb and (2**aux)-1>=auxb:
		return aux
	else:
		aux+=1
	return aux


def Maximo(idVariable):
	maximo=-99999
	if idVariable==0:
		for i in range(len(sa_x)):
			if int(sa_x[i].get())>=maximo:
				maximo=int(sa_x[i].get())
	elif idVariable==1:
		for i in range(len(sa_y)):
			if int(sa_y[i].get())>=maximo:
				maximo=int(sa_y[i].get())
	elif idVariable==2:
		for i in range(len(sa_w)):
			if int(sa_w[i].get())>=maximo:
				maximo=int(sa_w[i].get())
	elif idVariable==3:
		for i in range(len(sa_v)):
			if int(sa_v[i].get())>=maximo:
				maximo=int(sa_v[i].get())
	return maximo

def Minimo(idVariable):
	minimo=99999
	if idVariable==0:
		for i in range(len(sa_x)):
			if int(sa_x[i].get())<minimo:
				minimo=int(sa_x[i].get())
	elif idVariable==1:
		for i in range(len(sa_y)):
			if int(sa_y[i].get())<minimo:
				minimo=int(sa_y[i].get())
	elif idVariable==2:
		for i in range(len(sa_w)):
			if int(sa_w[i].get())<minimo:
				minimo=int(sa_w[i].get())
	elif idVariable==3:
		for i in range(len(sa_v)):
			if int(sa_v[i].get())<minimo:
				minimo=int(sa_v[i].get())
	return minimo

def fin():
	raiz.destroy()

def agrega_condicion():
	global tkvar
	global choices
	try:
		contador.set(contador.get()+1)
		numCondiciones=contador.get()

		if numCondiciones<10:
			Label_x=tk.Label(vp,text="X+")
			Label_x.grid(column=6, row=numCondiciones)

			Label_y=tk.Label(vp,text="Y+")
			Label_y.grid(column=8, row=numCondiciones)

			Label_w=tk.Label(vp,text="W+")
			Label_w.grid(column=10, row=numCondiciones)

			Label_v=tk.Label(vp,text="V")
			Label_v.grid(column=12, row=numCondiciones)

			#Textareas
			sax=tk.StringVar()
			sa_x.append(sax)
			Text_x=tk.Entry(vp,width=6,textvariable=sax)
			Text_x.grid(column=5,row=numCondiciones)
			say=tk.StringVar()
			sa_y.append(say)
			Texto_y=tk.Entry(vp,width=6,textvariable=say)
			Texto_y.grid(column=7,row=numCondiciones)
			saw=tk.StringVar()
			sa_w.append(saw)
			Text_w=tk.Entry(vp,width=6,textvariable=saw)
			Text_w.grid(column=9,row=numCondiciones)
			sav=tk.StringVar()
			sa_v.append(sav)
			Text_v=tk.Entry(vp,width=6,textvariable=sav)
			Text_v.grid(column=11,row=numCondiciones)

			##print sa_x[0].get()
			##print sa_x[1].get()
			
			
			tkvar=tk.StringVar(raiz)
			choices={'>=','<=','='}
			tkvar.set('=')
			popupMenu=tk.OptionMenu(vp,tkvar,*choices)
			popupMenu.grid(column=13, row=numCondiciones)
			tkvar.trace('w', change_drop)

			iguals=tk.StringVar()
			igual.append(iguals)
			Text_igual=tk.Entry(vp,width=6,textvariable=iguals)
			Text_igual.grid(column=14,row=numCondiciones)
			#vp.pack()

	except IndexError:
			print "No se permiten mas de 5 condiciones"

def change_drop(*args):
	global tkvar
	global choices
	signo[contador.get()-5]=tkvar.get()


###############################INICIA MAIN##########################

contador=tk.IntVar() #lleva el numero de condiciones que se han usado -4
#ventana principal
vp=tk.Frame(raiz)
#configuraciones base para la ventana principal
vp.grid(column=0, row=0,padx=(50,50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)


#se anaden los elementos base


#labels
Label_titulo=tk.Label(vp, text="Solucionador de problemas de P.L. mediante algoritmos geneticos")
#Label_titulo.grid(column=3,row=1)
Label_z=tk.Label(vp,text="Z=")
Label_z.grid(column=4, row=2)

Label_x=tk.Label(vp,text="X+")
Label_x.grid(column=6, row=2)

Label_y=tk.Label(vp,text="Y+")
Label_y.grid(column=8, row=2)

Label_w=tk.Label(vp,text="W+")
Label_w.grid(column=10, row=2)

Label_v=tk.Label(vp,text="V")
Label_v.grid(column=12, row=2)




#Textareas
x_main=tk.StringVar()
z.append(x_main)
Text_x=tk.Entry(vp,width=6,textvariable=x_main)
Text_x.grid(column=5,row=2)

y_main=tk.StringVar()
z.append(y_main)
Text_y=tk.Entry(vp,width=6,textvariable=y_main)
Text_y.grid(column=7,row=2)

w_main=tk.StringVar()
z.append(w_main)
Text_w=tk.Entry(vp,width=6,textvariable=w_main)
Text_w.grid(column=9,row=2)

v_main=tk.StringVar()
z.append(v_main)
Text_v=tk.Entry(vp,width=6,textvariable=v_main)
Text_v.grid(column=11,row=2)


#botones
contador.set(4)
boton_Agregar=tk.Button(vp,text="Agregar", command=agrega_condicion)
boton_Agregar.grid(column=1,row=11)

boton_Min=tk.Button(vp,text="Minimizar", command=Minimizar)
boton_Min.grid(column=2, row=11)

boton_Max=tk.Button(vp,text="Maximizar", command=Maximizar)
boton_Max.grid(column=3, row=11)



#texto a lado de Z

Label_Texto=tk.Label(vp,text="Funcion objetivo: ")
Label_Texto.grid(column=1, row=2, columnspan=2)
Label_Texto=tk.Label(vp,text="Calculadora de algoritmos geneticos V1.0")
Label_Texto.grid(column=5, row=1, columnspan=6)

#bits de precision
Label_Bits=tk.Label(vp,text="Numero de bits de precision: ")
Label_Bits.grid(column=1, row=10, columnspan=2)
bits=tk.StringVar()
Bits_Precision.append(bits)
Text_Bits=tk.Entry(vp,width=6,textvariable=bits)
Text_Bits.grid(column=3,row=10)

raiz.mainloop()


