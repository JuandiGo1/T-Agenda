import tkinter as tk
from tkinter.font import BOLD, ITALIC
from typing import Optional
import utilerias.util as utl
from forms.empleado import Empleados
from forms.horario import ventanaHorario
from forms.asignar import asigTurn
import utilerias.clases as cl
import utilerias.lista as cll
from forms import login as log
from utilerias.clases import Empleado
from tkinter import PhotoImage
from PIL import Image,ImageTk
import forms.infoper as per




class Inicio:
    def v_empleados(self):
        self.ventana.destroy()
        Empleados()
    def v_horario(self):
        self.ventana.destroy()
        ventanaHorario()
    def v_asig(self):
        self.ventana.destroy()
        asigTurn()
    def logOut(self):
        self.ventana.destroy()
        log.PanelPrincipal()
    def inf(self):
        self.ventana.destroy()
        per.Personales(self.user)
                                      
    def __init__(self, permis=None, user:Empleado=None):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Menu')
        self.permis = permis   
        self.user = user                     
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#E3FCBF')
        self.ventana.resizable(width=0, height=0)     
        utl.centrar_ventana(self.ventana, 800, 500)
 

        logo =utl.leer_img("./imagenes/logo.png", (300, 300))
        img = Image.open("./imagenes/salir.png")
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        frame_resto = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#E8F9FD')
        frame_resto.pack(expand=tk.YES,fill=tk.BOTH)      
        #medio = tk.Label( frame_resto,bg='#fcfcfc' )
        #medio.place(x=50,y=0,relwidth=1, relheight=1)
        frame_sup = tk.Frame(frame_resto, bd=0, padx=5, pady=5,bg='#3a7ff6')
        frame_sup.place(x=0, y=0, width=800, height=100)
        title = tk.Label(frame_sup, text="Menu Principal",font=('Arial', 30, BOLD, ITALIC),
         fg="#fcfcfc",bg='#3a7ff6',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        log_out= tk.Button(self.ventana,image=img,  relief="flat", overrelief="raised",bg="#E8F9FD",
         command=self.logOut)

        log_out.place(x=730, y=433 )
        self.empleado = tk.Button(self.ventana, bg = '#3a7ff6', fg="#fff",font=('Arial', 20, BOLD, ITALIC),
         text="Empleados",command= self.v_empleados)
        
        self.agendar = tk.Button(self.ventana, bg = '#3a7ff6', fg="#fff",font=('Arial', 20, BOLD, ITALIC), 
        text="Agendar",command= self.v_asig)

        self.datos = tk.Button(self.ventana, bg = '#3a7ff6', fg="#fff",font=('Arial', 20, BOLD, ITALIC), 
        text="Inf Personal", command=self.inf)
        
        horario = tk.Button(self.ventana, bg = '#3a7ff6', fg="#fff",font=('Arial', 20, BOLD, ITALIC),
         text="Horario",command= self.v_horario)

        if self.permis==0:
            self.datos.place(relx=0.35, rely=0.35 , relwidth= 0.3, relheight= 0.1 )
            self.empleado.config(state='disabled')
            self.agendar.config(state='disabled')
            horario.place(relx=0.35, rely=0.55 , relwidth= 0.3, relheight= 0.1 )
        else:
            self.empleado.place(relx=0.35, rely=0.35 , relwidth= 0.3, relheight= 0.1 )
            self.agendar.place(relx=0.35, rely=0.55 , relwidth= 0.3, relheight= 0.1 )
            self.empleado.config(state='normal')
            self.agendar.config(state='normal')
            horario.place(relx=0.35, rely=0.75 , relwidth= 0.3, relheight= 0.1 )
        
        if user!=None:
            usuario_lbl= tk.Label(self.ventana, bg = '#E8F9FD', fg="#3a7ff6",font=('Arial', 17, BOLD, ITALIC),
             text=f"Bienvenido {self.user.name}.")

            usuario_lbl.place(x=5, y=110, relwidth= 0.3, relheight= 0.1)
      
        

        
        self.ventana.mainloop()