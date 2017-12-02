import tkinter as tk
from tkinter import *
import math
from matplotlib import pyplot
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot,sec
from math import pi
from scipy.misc import derivative


def GRAFICAR_COS():
    ven_cos.destroy()
    coff1 = float(cos_amplitud.get())
    coff2 = float(cos_periodo.get())
    coff3 = float(cos_desface.get())
    x = Symbol("x")

    # Valores del eje X que toma el gráfico.
    x = range(-100, 100)

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-100, 100)
    pyplot.ylim(-100, 100)

    f_cos = lambda x: coff1*math.cos(0.1*coff2*x+coff3)
    pyplot.plot(x, [f_cos(i) for i in x])
    pyplot.plot(x, [derivative(f_cos, i, dx=1e-10) for i in x])
    pyplot.savefig("output.png")
    pyplot.show()
    return




#DEFINIMOS LA VENTANA
ven_cos=tk.Tk()
ven_cos.title("GRAFICADOR DE FUNCIONES")
ven_cos.geometry('400x300')
ven_cos.configure(background='dark turquoise')

#TITULO FUNCION SENO
titulo_cos=Label(text="FUNCION COSENO",font=("Agency FB",24)).place(x=120,y=8)

#CREAR BOTON
boton_cos=Button(ven_cos,text="GRAFICAR FUNCION",fg="white",bg="brown",command=GRAFICAR_COS).place(x=140,y=250)

#PARA INGRESAR AMPLITUD
text_cos_amplitud=Label(text="Amplitud",font=("Agency FB",14)).place(x=20,y=70)
cos_amplitud=StringVar()
caj_cos_amplitud=Entry(ven_cos,textvariable=cos_amplitud).place(x=200,y=75)

#PARA INGRESAR PERIODO
text_cos_periodo=Label(text="Periodo",font=("Agency FB",14)).place(x=20,y=110)
cos_periodo=StringVar()
caj_cos_periodo=Entry(ven_cos,textvariable=cos_periodo).place(x=200,y=115)

#PARA INGRESAR DESFACE
text_cos_desface=Label(text="Desface",font=("Agency FB",14)).place(x=20,y=150)
cos_desface=StringVar()
caj_cos_desface=Entry(ven_cos,textvariable=cos_desface).place(x=200,y=155)


ven_cos.mainloop()