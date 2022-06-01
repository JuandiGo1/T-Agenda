
import tkinter as tk
from tkinter import W, ttk
from tkinter.font import BOLD, ITALIC
from tkinter.tix import COLUMN

class User:
    def __init__(self):
        self.contra = None
        self.name = None

    def login(self):
        pass

class turnos():
    def __init__(self, dia:str, inicio, fin):
        self.dia = dia
        self.inicio = inicio
        self.fin=fin

base = turnos("NA","NA","NA")
bas=[base]
class Empleado(User):
    
    def __init__(self, name, cedula, cargos, telefono, contra, tur: list[turnos] = [base]):
        self.name = name
        self.cedula = cedula
        self.telefono = telefono
        self.cargos = cargos
        self.turno = tur
        self.contra = contra
        self.permiso=0
    
    def recorTurnos(self, dia, Tx:tk.Text):
        for t in self.turno:
            if t.dia == dia:
                Tx.insert(tk.END, "============================= Empleado =============================== \n")
                Tx.insert(tk.END, "Nombre: "+self.name+"\n")
                Tx.insert(tk.END, "Cedula: "+str(self.cedula)+"\n")
                Tx.insert(tk.END, "Cargo: "+self.cargos+"\n")
                Tx.insert(tk.END, "Turno: \n")
                Tx.insert(tk.END, "- Dia: "+t.dia+"\n")
                Tx.insert(tk.END, "- Inicio: "+t.inicio +"\n")
                Tx.insert(tk.END, "- Fin: "+t.fin+"\n")
    
    def actualizarContra(self, antC, newC):
        if antC == self.contra:
            self.contra=newC
            return "Contraseña actualizada"
        else:
            return "Contraseña incorrecta"
    
class turnos():
    def __init__(self, dia:str, inicio, fin):
        self.dia = dia
        self.inicio = inicio
        self.fin=fin

class Admin(User):
    def __init__(self, name, cedula, telefono, contra):
        self.name = name
        self.cedula = cedula
        self.telefono = telefono
        self.contra = contra




