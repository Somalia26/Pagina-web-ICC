import tkinter as tk
from tkinter import *
import math
from matplotlib import pyplot
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot,sec
from math import pi
from scipy.misc import derivative

def LOG():
    ven_log.destroy()
    coff1=float(log_cof.get())
    coff2=float(log_base.get())

    x = Symbol("x")

    # Valores del eje X que toma el gráfico.
    x = range(1, 100)

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-50, 50)
    pyplot.ylim(-100, 100)

    f_log = lambda x: coff1*math.log(x,coff2)
    pyplot.plot(x, [f_log(i) for i in x])
    pyplot.plot(x, [derivative(f_log, i, dx=1e-10) for i in x])
    pyplot.savefig("output.png")
    pyplot.show()
    return






#DEFINIMOS AL VENTANA
ven_log=tk.Tk()
ven_log.title("GRAFICADOR DE FUNCIONES")
ven_log.geometry('400x300')
ven_log.configure(background='dark turquoise')

#TITULO FUNCION LOGARITMICA
titulo_log=Label(text="FUNCION LOGARITMICA",font=("Agency FB",24)).place(x=120,y=8)

#CREAR BOTON
boton_log=Button(ven_log,text="GRAFICAR FUNCION",fg="white",bg="brown",command=LOG).place(x=150,y=250)

#PARA INGRESAR COEFICIENTE LOGARITMO
text_log_cof=Label(text="Coeficiente logaritmico",font=("Agency FB",14)).place(x=20,y=70)
log_cof=StringVar()
caj_log_cof=Entry(ven_log,textvariable=log_cof).place(x=200,y=75)

#PARA INGRESAR BASE
text_log_base=Label(text="Base",font=("Agency FB",14)).place(x=20,y=110)
log_base=StringVar()
caj_log_base=Entry(ven_log,textvariable=log_base).place(x=200,y=115)


ven_log.mainloop()