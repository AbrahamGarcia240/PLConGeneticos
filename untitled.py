#!/usr/bin/python

import sys
import Tkinter as tk

def hacer_click():
	try:
		_valor=int(entrada_texto.get())
		_valor=_valor*10
		print _valor
		etiqueta_salida.config(text=_valor)
	except ValueError:
		etiqueta_salida.config(text="Introduce un numero y lo multiplicare por 10")



def abre_ventana():
	otra_ventana=tk.Toplevel()
	raiz.withdraw()

raiz =tk.Tk()
raiz.title("Mi primera app")

#vp-> Ventana principal

vp=tk.Frame(raiz)
vp.grid(column=0, row=0,padx=(50,50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

etiqueta=tk.Label(vp,text="Escribe algo")
etiqueta.grid(column=1,row=1)
boton=tk.Button(vp,text="Enviar",command=hacer_click)
boton.grid(column=1, row=2)
valor=""
entrada_texto=tk.Entry(vp,width=10,textvariable=valor)
entrada_texto.grid(column=2, row=1)

etiqueta_salida=tk.Label(vp,text=" ")
etiqueta_salida.grid(column=2,row=2)

boton_ventana=tk.Button(vp,text="Abrir una nueva ventana", command=abre_ventana)
boton_ventana.grid(column=3,row=2)



raiz.mainloop()


