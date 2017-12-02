import tkinter as tk
from tkinter import *
import math
from matplotlib import pyplot
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot,sec
from math import pi
from scipy.misc import derivative

ven_cuadratica = tk.Tk()
ven_cuadratica.withdraw() # Ocultar la pantalla
cof_cuadratico_cuadratico = StringVar()
cof_cuadratico_lineal = StringVar()
cof_cuadratico_independiente = StringVar()

def GRAFICAR_CUADRATICA():
    ven_cuadratica.withdraw()
    cofff1=int(cof_cuadratico_cuadratico.get())
    cofff2=int(cof_cuadratico_lineal.get())
    cofff3=int(cof_cuadratico_independiente.get())

    x = Symbol("x")

    # Valores del eje X que toma el gráfico.
    x = range(-50, 50)

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-50, 50)
    pyplot.ylim(-100, 100)

    f_cuadratica = lambda x: cofff1 * x**2 + cofff2 * x + cofff3
    pyplot.plot(x, [f_cuadratica(i) for i in x])
    pyplot.plot(x, [derivative(f_cuadratica, i, dx=1e-10) for i in x])
    pyplot.savefig("output.png")
    pyplot.show()
    return

def mostrar_funcion_cuadratica():
    global cof_cuadratico_cuadratico
    global cof_cuadratico_lineal
    global cof_cuadratico_independiente
    # DEFINIMOS LA VENTANA
    ven_cuadratica.deiconify()  # Mostrar la pantalla
    ven_cuadratica.title("GRAFICADOR DE FUNCIONES")
    ven_cuadratica.geometry('400x300')
    ven_cuadratica.configure(background='dark turquoise')

    # TITULO FUNCION CUADRATICA
    titulo_cuadratico = Label(ven_cuadratica,text="FUNCION CUADRATICA", font=("Agency FB", 24)).place(x=100, y=8)

    # CREAR BOTON
    boton_cuadratico = Button(ven_cuadratica, text="GRAFICAR FUNCION", fg="white", bg="brown",
                              command=GRAFICAR_CUADRATICA).place(x=170, y=250)

    # PARA INGRESAR TERMINO CUADRATICO
    text_cuadratico_cuadratico = Label(ven_cuadratica,text="Coeficiente cuadratico", font=("Agency FB", 14)).place(x=20, y=70)
    #cof_cuadratico_cuadratico = StringVar()
    caj_cuadratico_cuadratico = Entry(ven_cuadratica, textvariable=cof_cuadratico_cuadratico).place(x=200, y=75)

    # PARA INGRESAR TERMINO LINEAL
    text_cuadratico_lineal = Label(ven_cuadratica,text="Coeficiente lineal", font=("Agency FB", 14)).place(x=20, y=110)
    #cof_cuadratico_lineal = StringVar()
    caj_cuadratico_lineal = Entry(ven_cuadratica, textvariable=cof_cuadratico_lineal).place(x=200, y=115)

    # PARA INGRESAR TERMINO INDEPENDIENTE
    text_cuadratico_independiente = Label(ven_cuadratica,text="Coeficiente independiente", font=("Agency FB", 14)).place(x=20, y=150)
    #cof_cuadratico_independiente = StringVar()
    caj_cuadratico_independiente = Entry(ven_cuadratica, textvariable=cof_cuadratico_independiente).place(x=200, y=155)

    ven_cuadratica.mainloop()

mostrar_funcion_cuadratica()