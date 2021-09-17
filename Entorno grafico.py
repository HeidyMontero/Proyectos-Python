"""
from tkinter import *
from tkinter import ttk
import time 

def accion():
    print("Ejecutando la accion correspondiente a este boton")

def tiempo():
    ventana.iconify()
    time.sleep(5)
    ventana.deiconify()




ventana=Tk()
ventana.title(" Heidy ")
ventana.geometry("400x400")#Dimension de la ventana en pixeceles
ventana.configure(bg="beige")

etiqueta=Label(ventana,text="Hola mundo",bg="Yellow")
etiqueta.pack()

boton=Button(ventana,text="Minimizar",command=ventana.iconify,fg="blue")
boton.pack(side=RIGHT)

boton1=Button(ventana,text="Desactivar",command=ventana.quit,fg="red")
boton1.pack() #.Pack cuando no hay coordenadas x=200, y=8000

boton2=Button(ventana,text="Imprimir",command=accion)
boton2.pack()

boton3=Button(ventana,text="Tiempo",command=tiempo)
boton3.pack()

ventana.mainloop()

"""

from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("UWU HEIDY UWU")
ventana.geometry("400x400")#Dimension de la ventana en pixeceles
boton=Button(ventana,text="Nombre de boton").place(x=100,y=2)

