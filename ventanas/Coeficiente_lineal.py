import tkinter as tk
from tkinter import *
import math
from matplotlib import pyplot
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot,sec
from math import pi
from scipy.misc import derivative

ven_lineal = tk.Tk()
ven_lineal.withdraw() # Ocultar la pantalla
cof_lineal = StringVar()
cof_independiente = StringVar()

def GRAFICAR():
    ven_lineal.destroy()
    coff1=float('0'+cof_lineal.get())
    coff2=float('0'+cof_independiente.get())

    x = Symbol("x")

    # Valores del eje X que toma el gráfico.
    x = range(-100, 100)

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-100, 100)
    pyplot.ylim(-100, 100)

    f_lineal = lambda x: coff1 * x + coff2
    pyplot.plot(x, [f_lineal(i) for i in x])
    pyplot.plot(x, [derivative(f_lineal, i, dx=1e-10) for i in x])
    pyplot.savefig("output.png")
    pyplot.show()
    return


def mostrar_funcion_lineal ():
    # DEFINIMOS AL VENTANA
    ven_lineal.deiconify() # Mostrar la pantalla
    ven_lineal.title("GRAFICADOR DE FUNCIONES")
    ven_lineal.geometry('400x300')
    ven_lineal.configure(background='dark turquoise')

    # TITULO FUNCION LINEAL
    titulo_lineal = Label(ven_lineal,text="FUNCION LINEAL", font=("Agency FB", 24)).place(x=120, y=8)

    # CREAR BOTON
    boton_lineal = Button(ven_lineal, text="GRAFICAR FUNCION", fg="white", bg="brown", command=GRAFICAR).place(x=170, y=250)

    # PARA INGRESAR TERMINO LINEAL
    text_lineal = Label(ven_lineal,text="Coeficiente lineal", font=("Agency FB", 14)).place(x=20, y=70)
    #cof_lineal = StringVar()
    caj_lineal = Entry(ven_lineal, textvariable=cof_lineal).place(x=200, y=75)

    # PARA INGRESAR TERMINO INDEPENDIENTE
    text_independiente = Label(ven_lineal,text="Coeficiente independiente", font=("Agency FB", 14)).place(x=20, y=110)
    #cof_independiente = StringVar()
    caj_independiente = Entry(ven_lineal, textvariable=cof_independiente).place(x=200, y=115)

    ven_lineal.mainloop()
