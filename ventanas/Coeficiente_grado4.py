import tkinter as tk
from tkinter import *
import math
from matplotlib import pyplot
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot,sec
from math import pi
from scipy.misc import derivative

def GRAFICAR_GRAD4():
    ven_grad4.destroy()
    coff1 = int(cof_grad4_term4.get())
    coff2 = int(cof_grad4_cubico.get())
    coff3 = int(cof_grad4_cuadratico.get())
    coff4 = int(cof_grad4_lineal.get())
    coff5 = int(cof_grad4_independiente.get())

    x = Symbol("x")

    # Valores del eje X que toma el gráfico.
    x = range(-50, 50)

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-50, 50)
    pyplot.ylim(-100, 100)

    f_cuarta = lambda x: coff1 * x ** 4 + coff2 * x**3 + coff3 * x**2+ coff4**x +coff5
    pyplot.plot(x, [f_cuarta(i) for i in x])
    pyplot.plot(x, [derivative(f_cuarta, i, dx=1e-10) for i in x])
    pyplot.savefig("output.png")
    pyplot.show()
    return




#DEFINIMOS LA VENTANA
ven_grad4=tk.Tk()
ven_grad4.title("GRAFICADOR DE FUNCIONES")
ven_grad4.geometry('400x300')
ven_grad4.configure(background='dark turquoise')

#TITULO FUNCION DE GRADO 4
titulo_grad4=Label(text="FUNCION DE GRADO 4",font=("Agency FB",24)).place(x=100,y=8)

#CREAR BOTON
boton_grad4=Button(ven_grad4,text="GRAFICAR FUNCION",fg="white",bg="brown",command=GRAFICAR_GRAD4).place(x=120,y=270)

#PARA INGRESAR TERMINO DE GRADO 4
text_grad4_term4=Label(text="Coeficiente de grado 4",font=("Agency FB",14)).place(x=20,y=70)
cof_grad4_term4=StringVar()
caj_grad4_term4=Entry(ven_grad4,textvariable=cof_grad4_term4).place(x=200,y=75)

#PARA INGRESAR TERMINO CUBICO
text_grad4_cubico=Label(text="Coeficiente cubico",font=("Agency FB",14)).place(x=20,y=110)
cof_grad4_cubico=StringVar()
caj_grad4_cubico=Entry(ven_grad4,textvariable=cof_grad4_cubico).place(x=200,y=115)

#PARA INGRESAR TERMINO CUADRATICO
text_grad4_cuadratico=Label(text="Coeficiente cuadratico",font=("Agency FB",14)).place(x=20,y=150)
cof_grad4_cuadratico=StringVar()
caj_grad4_cuadratico=Entry(ven_grad4,textvariable=cof_grad4_cuadratico).place(x=200,y=155)

#PARA INGRESAR TERMINO LINEAL
text_grad4_lineal=Label(text="Coeficiente lineal",font=("Agency FB",14)).place(x=20,y=190)
cof_grad4_lineal=StringVar()
caj_grad4_lineal=Entry(ven_grad4,textvariable=cof_grad4_lineal).place(x=200,y=195)

#PARA INGRESAR TERMINO INDEPENDIENTE
text_grad4_independiente=Label(text="Coeficiente independiente",font=("Agency FB",14)).place(x=20,y=230)
cof_grad4_independiente=StringVar()
caj_grad4_independiente=Entry(ven_grad4,textvariable=cof_grad4_independiente).place(x=200,y=235)

ven_grad4.mainloop()