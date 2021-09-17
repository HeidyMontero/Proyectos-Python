from tkinter import *
from tkinter import ttk
from tkinter import messagebox

"""
def accion():
    print(variable.get)
    messagebox.showinfo("Mensaje","Seleccionaste la respuesta 2")


ventana=Tk()
ventana.title("Seleccion")
ventana.geometry("400x400")
variable=StringVar()
etiqueta=Label(ventana,text="Seleccione opcion 1").place(x=10,y=10)
seleccion=Spinbox(ventana,values=("Opcion 1","Opcion 2")).place(x=10,y=30)
etiqueta1=Label(ventana,text="Seleccione opcion 2").place(x=10,y=50)
seleccion2=Spinbox(ventana,from_=1,to=20,textvariable=variable).place(x=10,y=70)
boton=Button(ventana,text="ejecutar",command=accion).place(x=10,y=90)
mainloop()

"""

"""
messagebox.showinfo("Mensaje", "Hola Heidy")
messagebox.showwarning("Mensaje", "Hola Heidy")
messagebox.askquestion("Mensaje", "Hola Heidy")
messagebox.askokcancel("Mensaje", "Hola Heidy")

"""
"""
ventana=Tk()
ventana.geometry("400x400")
seleccion=ttk.Combobox(ventana,width=20)
seleccion.place(x=10,y=10)

opciones=["Opcion 1","Opcion 2","Opcion 3"]
seleccion["values"]=opciones

mainloop()
"""
#----------------------------------------------------------------------
#                              MODELAR UNA FUNCION
#----------------------------------------------------------------------
import numpy as np
import math
import matplotlib.pyplot as plt

"""
x=np.array(range(200))*0.1#Creando arreglo
x1=np.array(range(200))*0.1#Creando arreglo si y solo si se planea en otra escala el x
y=np.zeros(len(x))#Variable dependente de x
z=np.zeros(len(x))#Variable dependente de x


for i in range(len(x)):
    y[i]=math.sin(x[i])#Y=f(x)=sen(x)
    z[i]=math.cos(x[i])#Z=f(x)=cos(x)
    

plt.plot(x,y)
plt.plot(x,z)
plt.show()
"""
#----------------------------------------------------------------------
"""
x=np.linspace(0,10,50)
f=lambda x: np.sin(x)
g=lambda x: np.cos(x)
plt.plot(x,f(x),"go")#y* color y tipo de traza
plt.plot(x,g(x),"ro")
plt.show()

"""
#---------------------------------------------------------------------
#             REPRESENTAR GRAFICAS CON FUNCIONES
#---------------------------------------------------------------------
def f(x):
    return np.sin(x)

def g(x):
    return np.cos(x)
    

x=np.linspace(0,10,50)
plt.plot(x,f(x),"b-")
plt.plot(x,g(x),"m-")
plt.xlabel("Tiempo(x)")
plt.ylabel("f,g(x)")
plt.savefig("Grafica.png")#Guardar imagen
plt.show()


    
    
































