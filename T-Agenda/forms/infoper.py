from logging import root
import tkinter as tk
from tkinter import Image, Tk, ttk
from tkinter.font import BOLD, ITALIC
from tkinter.tix import COLUMN
from turtle import right
from utilerias.clases import Empleado
import utilerias.util as utl
import forms.horario as hor
import forms.ventana as v
import forms.login as log
from PIL import Image, ImageTk

class Personales:

     
    
    def __init__(self, user:Empleado=None):  
        self.user = user 
        self.ventana = tk.Tk()                             
        self.ventana.title('INFO PERSONAL')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#B8FFF9')
        self.ventana.resizable(width=0, height=0)          
        utl.centrar_ventana(self.ventana, 800, 500)
        frame_sup = tk.Frame(self.ventana, bd=0, width=800, height=100,  bg='#2dc2a1')
        frame_sup.grid(row=0, column=0)
        title_lbl = tk.Label(self.ventana, text="Info Personal", font=('Arial', 30, BOLD, ITALIC ), 
        bg='#2dc2a1', fg='#fcfcfc')

        title_lbl.grid(row=0, column=0)
        frame_inf = tk.Frame(self.ventana, bd=0, width=800, height=700,  bg='#1a6958')
        frame_inf.grid(row=1, column=0)

        name_lbl=tk.Label(frame_inf, text=f"Nombre: {self.user.name}", font=('Arial', 20, BOLD, ITALIC),
          bg='#1a6958', fg='#fcfcfc')
        name_lbl.place(x=70, y=70)
        cedula_lbl=tk.Label(frame_inf, text=f"Cedula: {self.user.cedula}", font=('Arial', 20, BOLD, ITALIC),
          bg='#1a6958', fg='#fcfcfc')
        cedula_lbl.place(x=70, y=130)
        tel_lbl=tk.Label(frame_inf, text=f"Celular: {self.user.telefono}", font=('Arial', 20, BOLD, ITALIC),
          bg='#1a6958', fg='#fcfcfc')
        tel_lbl.place(x=70, y=190)

        cargo_lbl=tk.Label(frame_inf, text=f"Cargo: {self.user.cargos}", font=('Arial', 20, BOLD, ITALIC),
          bg='#1a6958', fg='#fcfcfc')
        cargo_lbl.place(x=70, y=250)

        chang_lbl=tk.Label(frame_inf, text=f"Cambiar contraseña", font=('Arial', 20, BOLD, ITALIC),
          bg='#1a6958', fg='#fcfcfc')
        chang_lbl.place(x=400, y=70)

        ant_lbl=tk.Label(frame_inf, text=f"Antigua contraseña:", font=('Arial', 13, BOLD, ITALIC),
          bg='#1a6958', fg='#fcfcfc')
        ant_lbl.place(x=400, y=130)
        self.ant= tk.Entry(frame_inf,width=27)
        self.ant.place(x=400, y=160)
        new_lbl=tk.Label(frame_inf, text=f"Nueva contraseña:", font=('Arial', 13, BOLD, ITALIC),
          bg='#1a6958', fg='#fcfcfc')
        new_lbl.place(x=400, y=190)
        self.new= tk.Entry(frame_inf,width=27)
        self.new.place(x=400, y=220)

        self.cambiar = tk.Button(frame_inf, text= "Cambiar", font=('Arial', 12, BOLD ), 
        bg="#09872f", fg='#fcfcfc',width=16)
        self.cambiar.place(x=400, y=250)




        

        self.ventana.mainloop()