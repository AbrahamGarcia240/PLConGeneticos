#!/usr/bin/python

import sys
import Tkinter as tk
import tktable as tkt
from numpy import *
import math


#variables globales
sa_x=[]
sa_y=[]
sa_v=[]
sa_w=[]
igual=[]
signo=["" for x in range(5)]
z=[]
maximos=[]
minimos=[]
Bits_Precision=[]
mjs=[]

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
	
	############INICIO ALGORITMO################
	#Obtengo los maximos y minimos de cada variable
	for i in range(len(z)):
		if z[i].get()!="":
			minimos.append(Minimo(i))
			maximos.append(Maximo(i))
			mjs.append(Calcula_mj(i,minimos[i],maximos[i]))
	ImprimeArreglos()
	

def Calcula_mj(idVariable,minimo,maximo):
	print "minimo: ",minimo,
	print "maximo: ",maximo
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


