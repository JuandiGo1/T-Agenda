

import tkinter as tk
from tkinter.font import BOLD, ITALIC
from tkinter.tix import COLUMN
import utilerias.util as utl
import forms.horario as hor
import forms.ventana as v

class Empleados:
    def destruir(self):
        for element in self.ventana.winfo_children():
            element.destroy()

    def v_menu(self):
        self.ventana.destroy()
        v.Inicio()

    def v_horario(self):
        self.ventana.destroy()
        hor.ventanaHorario()
    



    def __init__(self):  
        self.ventana = tk.Tk()                             
        self.ventana.title('EMPLEADOS')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)          
        utl.centrar_ventana(self.ventana, 800, 500)

        frame_sup = tk.Frame(self.ventana, bd=0, width=800, height=100,  bg='#2dc2a1')
        frame_sup.grid(row=0, column=0)
        title_lbl = tk.Label(self.ventana, text="Registro de Empleados", font=('Arial', 30, BOLD, ITALIC ), bg='#2dc2a1', fg='#fcfcfc')
        title_lbl.grid(row=0, column=0)
        frame_inf = tk.Frame(self.ventana, bd=0, width=800, height=700,  bg='#1a6958')
        frame_inf.grid(row=1, column=0)

        #Nombre
        name_lbl=tk.Label(frame_inf, text="Nombre", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        name_lbl.place(x=50, y=50)
        name_tx= tk.Entry(frame_inf,width=20)
        name_tx.place(x=50, y= 90)

        #cedula
        cedula_lbl=tk.Label(frame_inf, text="Cedula", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        cedula_lbl.place(x=50, y=120)
        cedula_tx= tk.Entry(frame_inf,width=20)
        cedula_tx.place(x=50, y= 150)

        #cel
        cel_lbl=tk.Label(frame_inf, text="Celular", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        cel_lbl.place(x=50, y=180)
        cel_tx= tk.Entry(frame_inf,width=20)
        cel_tx.place(x=50, y= 210)

        #contra
        pass_lbl=tk.Label(frame_inf, text="Contraseña", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        pass_lbl.place(x=50, y=240)
        pass_tx= tk.Entry(frame_inf,width=20)
        pass_tx.config(show="*")
        pass_tx.place(x=50, y= 270)

        regis = tk.Button(frame_inf, text= "Registrar", font=('Arial', 15, BOLD ), bg="#09872f", fg='#fcfcfc')
        regis.place(x=50, y= 300)

        IR = tk.Button(frame_inf, text= "Ir", font=('Arial', 15, BOLD ), bg="#09872f", fg='#fcfcfc', command=self.v_horario)
        IR.place(x=250, y= 300)

        volver= tk.Button(frame_inf, text= "VOLVER",font=('Arial', 12, BOLD ), bg="#09872f", fg='#fcfcfc', width=15, command=self.v_menu)
        volver.place(x=630, y= 360)
        
        
        
        self.ventana.mainloop()