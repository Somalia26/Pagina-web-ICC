from tkinter import *
import tkinter as tk
from tkinter import *
import math
from matplotlib import pyplot
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot,sec
from math import pi
from scipy.misc import derivative
import sys
import os

# Llamada de Coeficiente_lineal.py
from Coeficiente_lineal import mostrar_funcion_lineal
#from Coeficiente_cuadratico import mostrar_funcion_cuadratica

def Ir_a_ven1():
    ven.withdraw()
    ven1=tk.Toplevel()
    ven1.title("graficador")
    ven1.geometry("400x600")
    ven1.configure(bg="black")

#ETIQEUTA DE SELECCIONE UNA FUNCION
    eti_funciones = tk.Label(ven1, text="SELECCIONA UNA FUNCIÓN:", bg="green", fg="white")
    eti_funciones.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)


#ETIQUETA DE FUNCIONES POLINOMICAS
    eti_funciones_poli = tk.Label(ven1, text="FUNCIONES POLINOMICAS:", bg="blue", fg="white")
    eti_funciones_poli.pack(padx=50, pady=10, ipadx=5, ipady=5, fill=tk.X)

#BOTON FUNCION LINEAL
    boton_fun_lineal = tk.Button(ven1, text="FUNCION LINEAL", fg="white", bg="brown",command=mostrar_funcion_lineal).place(x=143, y=95)

#BOTON FUNCION CUDRATICA
    boton_fun_cuadratica = tk.Button(ven1, text="FUNCION CUADRATICA", fg="white", bg="brown").place(x=143, y=125)

#BOTON FUNCION CUBICA
    boton_fun_cubica = tk.Button(ven1, text="FUNCION CUBICA", fg="white", bg="brown").place(x=143, y=155)

#BOTON FUNCION DE GRADO 4
    boton_fun_grad4 = tk.Button(ven1, text="FUNCION DE GRADO 4", fg="white", bg="brown").place(x=143, y=185)


#ETIQUETA DE FUNCIONES TRIGONOMETRICAS
    eti_funciones_trig = tk.Label(ven1, text="FUNCIONES TRIGONOMETRICAS:", bg="blue", fg="white")
    eti_funciones_trig.pack(padx=50, pady=150, ipadx=5, ipady=5, fill=tk.X)

#BOTON FUNCION SENO
    boton_fun_sen = tk.Button(ven1, text="FUNCION SENO", fg="white", bg="purple").place(x=143, y=285)

#BOTON FUNCION COSENO
    boton_fun_cos = tk.Button(ven1, text="FUNCION COSENO", fg="white", bg="purple").place(x=143, y=315)

#BOTON FUNCION TANGENTE
    #boton_fun_tan = tk.Button(ven1, text="FUNCION TANGENTE", fg="white", bg="purple").place(x=143, y=345)


#ETIQUETA DE FUNCION LOGARITMICA
    eti_funcione_log = tk.Label(ven1, text="FUNCIONE LOGARITMICA:", bg="blue", fg="white")
    eti_funcione_log.pack(padx=50, pady=0, ipadx=5, ipady=5, fill=tk.X)

#BOTON FUNCION LOGARITMICA
    boton_fun_log = tk.Button(ven1, text="FUNCION LOGARITMICA", fg="white", bg="orange").place(x=143, y=470)



ven=tk.Tk()
ven.title("GRAFICADOR DE FUNCIONES")
ven.geometry('300x300')
ven.configure(background='dark turquoise')

#image=tk.PhotoImage(file="Poliedro.gif")
#image=image.subsample(1,1)
#label=tk.Label(image=image)
#label.place(x=0,y=0,relwidth=1.0,relheight=1.0)

etq=tk.Label(ven,text="GRAFICADOR DE FUNCIONES", fg="white",bg="brown")
etq.pack(fill=tk.X)

etq1=tk.Label(ven,text="OBJETIVO", fg="black",bg="tan2")
etq1.pack(padx=10,pady=10,fill=tk.X)

etq2=tk.Label(ven,text="Este programa esta dirigido a los estudiantes \n que estan iniciando con el tema de funciones \n y asimismo con las derivadas.\n Disfruten el programa! ", fg="white",bg="black",padx=50,pady=50)
etq2.pack(padx=10,pady=10,fill=tk.X)

boton=tk.Button(ven,text="INICIAR",fg="white",bg="brown",command=Ir_a_ven1)
boton.pack(padx=10,pady=10)

ven.mainloop()


