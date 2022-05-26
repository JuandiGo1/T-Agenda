

import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD, ITALIC
from tkinter.tix import COLUMN
from utilerias.clases import Empleado
import utilerias.util as utl
import forms.horario as hor
import forms.ventana as v
import forms.login as log

class Empleados:
    def destruir(self):
        for element in self.ventana.winfo_children():
            element.destroy()

    def v_menu(self):
        self.ventana.destroy()
        if log.emp.buscar(log.act[0], log.act[1]).permiso==0:
            v.Inicio(0,log.emp.buscar(log.act[0], log.act[1])) 
        elif log.emp.buscar(log.act[0], log.act[1]).permiso==1:
            v.Inicio(1, log.emp.buscar(log.act[0], log.act[1]))
        

    def v_horario(self):
        self.ventana.destroy()
        hor.ventanaHorario()

    def regist(self):
        self.Tx.config(state='normal')
        file = open('empleados.txt', 'a')
        new = self.name_tx.get()+";"+self.cedula_tx.get()+";"+self.cargo_tx.get()+";"+self.cel_tx.get()+";"+self.pass_tx.get()+";dia;inicio;fin;0"
        file.write(new+"\n")
        ob= Empleado(self.name_tx.get(), int(self.cedula_tx.get()), self.cargo_tx.get(), self.cel_tx.get(), self.pass_tx.get())
        log.emp.insert(ob)
        self.Tx.insert(tk.END, "EMPLEADO REGISTRADO \n")
        self.Tx.config(state='disabled')
        self.name_tx.delete(0,tk.END)
        self.cedula_tx.delete(0,tk.END)
        self.cargo_tx.delete(0,tk.END)
        self.cel_tx.delete(0,tk.END)
        self.pass_tx.delete(0,tk.END)
        file.close
    



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
        self.name_tx= tk.Entry(frame_inf,width=20)
        self.name_tx.place(x=50, y= 90)

        #cedula
        cedula_lbl=tk.Label(frame_inf, text="Cedula", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        cedula_lbl.place(x=50, y=120)
        self.cedula_tx= tk.Entry(frame_inf,width=20)
        self.cedula_tx.place(x=50, y= 150)

        #cel
        cel_lbl=tk.Label(frame_inf, text="Celular", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        cel_lbl.place(x=50, y=180)
        self.cel_tx= tk.Entry(frame_inf,width=20)
        self.cel_tx.place(x=50, y= 210)

        #contra
        pass_lbl=tk.Label(frame_inf, text="Contraseña", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        pass_lbl.place(x=50, y=240)
        self.pass_tx= tk.Entry(frame_inf,width=20)
        self.pass_tx.config(show="*")
        self.pass_tx.place(x=50, y= 270)

        #cargo
        cargo_lbl=tk.Label(frame_inf, text="Cargo", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        cargo_lbl.place(x=50, y=300)
        self.cargo_tx= tk.Entry(frame_inf,width=20)
        self.cargo_tx.place(x=50, y= 330)

        regis = tk.Button(frame_inf, text= "Registrar", font=('Arial', 15, BOLD ), bg="#09872f", fg='#fcfcfc', width = 13, command=self.regist)
        regis.place(x=250, y= 280)



        volver= tk.Button(frame_inf, text= "VOLVER",font=('Arial', 12, BOLD ), bg="#09872f", fg='#fcfcfc', width=15, command=self.v_menu)
        volver.place(x=630, y= 360)

        self.Tx = tk.Text(frame_inf, height = 10, width = 20, state='disabled')
        self.Tx.place(x=250, y=90)
        inf_lbl = tk.Label(frame_inf, text="Información", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        inf_lbl.place(x=250, y= 50)


        self.ventana.mainloop()