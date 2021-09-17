"""
from tkinter import *
from tkinter import ttk

def recolectar():
    
    if x.get()==1:
      print("Su nombre es:"+nombre.get(),"Su telefono es: ",telefono.get(),"Es mujer")
            
    elif x.get()==2:
      print("Su nombre es:"+nombre.get(),"Su telefono es: ",telefono.get(),"Es hombre")   
    

ventana=Tk()
nombre=StringVar()
telefono=IntVar()
x=IntVar()

ventana.title("Ejemplo cajas de texto")
ventana.geometry("400x200")
etiqueta1=Label(ventana,text="Ingrese nombre: ").place(x=10, y=10)
nombre_de_caja=Entry(ventana,textvariable=nombre).place(x=160,y=10)

etiqueta2=Label(ventana,text="Ingrese telefono: ").place(x=10, y=50)
nombre_de_caja2=Entry(ventana,text=telefono).place(x=170,y=50)

etiqueta3=Label(ventana,text="Ingrese sexo: ").place(x=10, y=90)
RB1=Radiobutton(ventana,text="Mujer",value=1,variable=x).place(x=170,y=90)
RB2=Radiobutton(ventana,text="Hombre",value=2,variable=x).place(x=100,y=90)

boton=Button(ventana,text="Guardar",command=recolectar).place(x=170,y=130)

ventana.mainloop()
"""


#Formulario RadioButton
from tkinter import *
from tkinter import ttk

def accion():
    if x.get()==1:
       print("Es mujer")

    elif x.get()==2:
        print("Es hombre")
        
    
        
    
ventana=Tk()
x=IntVar()

ventana.title("Formulario")
ventana.geometry("400x200")

RB1=Radiobutton(ventana,text="Mujer",value=1,variable=x).place(x=10,y=10)
RB2=Radiobutton(ventana,text="Hombre",value=2,variable=x).place(x=10,y=30)

boton=Button(ventana,text="Guardar",command=accion).place(x=10,y=50)

ventana.mainloop()

