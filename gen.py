#!/usr/bin/python

import sys
import Tkinter as tk
from numpy import *


#variables para guardar las condiciones
sa_x=[]
sa_y=[]
sa_v=[]
sa_w=[]
igual=[]
signo=["" for x in range(5)]
z=[]

raiz=tk.Tk()
raiz.title("Algoritmos geneticos")
tkvar=tk.StringVar(raiz)
choices={'>=','<=','='}
tkvar.set('=')



def Minimizar():

	for i in range(len(sa_x)):
		print sa_x[i].get(),
	print ""
	for i in range(len(sa_y)):
		print sa_y[i].get(),
	print ""
	for i in range(len(sa_v)):
		print sa_v[i].get(),
	print ""
	for i in range(len(sa_w)):
		print sa_w[i].get(),
	print ""
	for i in range(len(igual)):
		print igual[i].get(),
	print ""
	print signo
	for i in range(len(z)):
		print z[i].get(),
	print ""

	#print sa_y
	#print sa_v
	#print sa_w
	#print igual
	#print signo


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
			
			

			popupMenu=tk.OptionMenu(vp,tkvar,*choices)
			popupMenu.grid(column=10, row=numCondiciones)
			tkvar.trace('w', change_drop)

			iguals=tk.StringVar()
			igual.append(iguals)
			Text_igual=tk.Entry(vp,width=6,textvariable=iguals)
			Text_igual.grid(column=11,row=numCondiciones)
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
boton_Agregar.grid(column=1,row=10)

boton_Min=tk.Button(vp,text="Minimizar", command=Minimizar)
boton_Min.grid(column=2, row=10)



#texto a lado de Z

Label_Texto=tk.Label(vp,text="Funcion objetivo: ")
Label_Texto.grid(column=1, row=2, columnspan=2)
Label_Texto=tk.Label(vp,text="Calculadora de algoritmos geneticos V1.0")
Label_Texto.grid(column=5, row=1, columnspan=6)



raiz.mainloop()


