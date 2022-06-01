from math import perm
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.ventana import *
import utilerias.util as utl
import utilerias.clases as cl
from utilerias import lista as cll



emp = cll.CLL()
adm =cll.CLL()
act = []

def leerArchivo():
    archivo = open("empleados.txt", "r")
    
    for line in archivo:
        #reg= archivo.readline()
        archtur = open("file.txt", "r")
        vect = line.split(";")
        ax= []
        for renglon in archtur:
            reg= renglon.split(";")

            if(int(vect[1])==int(reg[0])):
                
                tur1 = cl.turnos(reg[1], reg[2], reg[3])
                tur2 = cl.turnos(reg[4], reg[5], reg[6])
                tur3 = cl.turnos(reg[7], reg[8], reg[9])
                tur4 = cl.turnos(reg[10], reg[11], reg[12])
                tur5 = cl.turnos(reg[13], reg[14], reg[15])
                tur6 = cl.turnos(reg[16], reg[17], reg[18])
                tur7 = cl.turnos(reg[19], reg[20], reg[21])
                ax= [tur1, tur2, tur3, tur4, tur5, tur6, tur7]
        archtur.close()
        
        objeto = cl.Empleado(vect[0], int(vect[1]), vect[2], vect[3], vect[4], ax)
        
        if int(vect[8])==1:
            objeto.permiso=1
        print(objeto.permiso)
        
        emp.insert(objeto)

    archivo.close()
    


leerArchivo()

class PanelPrincipal:
    
    def verificar(self):
        
        usu = self.usuario.get()
        password = self.password.get()
        
        act.append(usu)
        act.append(password)
          
        if(emp.buscar(usu, password) != None) :
            self.ventana.destroy()
            
            if emp.buscar(usu, password).permiso==0:
                Inicio(0,emp.buscar(usu, password)) 
            elif emp.buscar(usu, password).permiso==1:
                Inicio(1, emp.buscar(usu, password))
      
        else:
            messagebox.showerror(message="Credenciales incorrectas",title="Mensaje")     
    

                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Login')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()   
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        
        utl.centrar_ventana(self.ventana, 800, 500)
        #Aca logo de la app
        logo =utl.leer_img("./imagenes/logo.png", (300, 300))
                        
        frame_logo = tk.Frame(self.ventana, bd=0, width=50, relief=tk.SOLID, padx=5, pady=5,bg='#fcfcfc')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='#fcfcfc' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#3a7ff6')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)

        # frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#fcfcfc",bg='#3a7ff6',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#3a7ff6')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="User", font=('Times', 14) ,fg="#fcfcfc",bg='#3a7ff6', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#fcfcfc",bg='#3a7ff6' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Acceder",font=('Times', 15,BOLD),bg='#00ffa6', bd=0,fg="#fff", command= self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20) 
        inicio.bind("<Return>", (lambda event: self.verificar()))

        self.ventana.mainloop()

