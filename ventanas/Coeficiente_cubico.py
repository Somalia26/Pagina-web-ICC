import tkinter as tk
from tkinter import *
import math
from matplotlib import pyplot
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot,sec
from math import pi
from scipy.misc import derivative


def GRAFICAR_CUBICA():
    ven_cubica.destroy()
    coff1 = float(cof_cubico_cubico.get())
    coff2 = float(cof_cubico_cuadratico.get())
    coff3 = float(cof_cubico_lineal.get())
    coff4 = float(cof_cubico_independiente.get())
    x = Symbol("x")

    # Valores del eje X que toma el gráfico.
    x = range(-50, 50)

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-50, 50)
    pyplot.ylim(-100, 100)

    f_cubica = lambda x: coff1 * x ** 3 + coff2 * x**2 + coff3 * x+ coff4
    pyplot.plot(x, [f_cubica(i) for i in x])
    pyplot.plot(x, [derivative(f_cubica, i, dx=1e-10) for i in x])
    pyplot.savefig("output.png")
    pyplot.show()
    return



#DEFINIMOS LA VENTANA
ven_cubica=tk.Tk()
ven_cubica.title("GRAFICADOR DE FUNCIONES")
ven_cubica.geometry('400x300')
ven_cubica.configure(background='dark turquoise')

#TITULO FUNCION CUBICA
titulo_cubica=Label(text="FUNCION CUBICA",font=("Agency FB",24)).place(x=100,y=8)

#CREAR BOTON
boton_cubica=Button(ven_cubica,text="GRAFICAR FUNCION",fg="white",bg="brown",command=GRAFICAR_CUBICA).place(x=120,y=250)

#PARA INGRESAR TERMINO CUBICO
text_cubico_cubico=Label(text="Coeficiente cubico",font=("Agency FB",14)).place(x=20,y=70)
cof_cubico_cubico=StringVar()
caj_cubico_cubico=Entry(ven_cubica,textvariable=cof_cubico_cubico).place(x=200,y=75)

#PARA INGRESAR TERMINO CUADRATICO
text_cubico_cuadratico=Label(text="Coeficiente cuadratico",font=("Agency FB",14)).place(x=20,y=110)
cof_cubico_cuadratico=StringVar()
caj_cubico_cuadratico=Entry(ven_cubica,textvariable=cof_cubico_cuadratico).place(x=200,y=115)

#PARA INGRESAR TERMINO LINEAL
text_cubico_lineal=Label(text="Coeficiente lineal",font=("Agency FB",14)).place(x=20,y=150)
cof_cubico_lineal=StringVar()
caj_cubico_lineal=Entry(ven_cubica,textvariable=cof_cubico_lineal).place(x=200,y=155)

#PARA INGRESAR TERMINO INDEPENDIENTE
text_cubico_independiente=Label(text="Coeficiente independiente",font=("Agency FB",14)).place(x=20,y=190)
cof_cubico_independiente=StringVar()
caj_cubico_independiente=Entry(ven_cubica,textvariable=cof_cubico_independiente).place(x=200,y=195)

ven_cubica.mainloop()