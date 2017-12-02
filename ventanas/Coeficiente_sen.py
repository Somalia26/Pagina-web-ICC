import tkinter as tk
from tkinter import *
import math
from matplotlib import pyplot
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot,sec
from math import pi
from scipy.misc import derivative

def GRAFICAR_SEN():
    ven_sen.destroy()
    coff1 = float(sen_amplitud.get())
    coff2 = float(sen_periodo.get())
    coff3 = float(sen_desface.get())
    x = Symbol("x")

    # Valores del eje X que toma el gráfico.
    x = range(-50, 50)

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-50, 50)
    pyplot.ylim(-100, 100)

    f_sen = lambda x: coff1*math.sin(coff2*x+coff3)
    pyplot.plot(x, [f_sen(i) for i in x])
    pyplot.plot(x, [derivative(f_sen, i, dx=1e-10) for i in x])
    pyplot.savefig("output.png")
    pyplot.show()
    return


#DEFINIMOS LA VENTANA
ven_sen=tk.Tk()
ven_sen.title("GRAFICADOR DE FUNCIONES")
ven_sen.geometry('400x300')
ven_sen.configure(background='dark turquoise')

#TITULO FUNCION SENO
titulo_sen=Label(text="FUNCION SENO",font=("Agency FB",24)).place(x=120,y=8)

#CREAR BOTON
boton_sen=Button(ven_sen,text="GRAFICAR FUNCION",fg="white",bg="brown",command=GRAFICAR_SEN).place(x=150,y=250)

#PARA INGRESAR AMPLITUD
text_sen_amplitud=Label(text="Amplitud",font=("Agency FB",14)).place(x=20,y=70)
sen_amplitud=StringVar()
caj_sen_amplitud=Entry(ven_sen,textvariable=sen_amplitud).place(x=200,y=75)

#PARA INGRESAR PERIODO
text_sen_periodo=Label(text="Periodo",font=("Agency FB",14)).place(x=20,y=110)
sen_periodo=StringVar()
caj_sen_periodo=Entry(ven_sen,textvariable=sen_periodo).place(x=200,y=115)

#PARA INGRESAR DESFACE
text_sen_desface=Label(text="Desface",font=("Agency FB",14)).place(x=20,y=150)
sen_desface=StringVar()
caj_sen_desface=Entry(ven_sen,textvariable=sen_desface).place(x=200,y=155)


ven_sen.mainloop()