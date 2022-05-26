import tkinter as tk
from tkinter.font import BOLD, ITALIC
import utilerias.util as utl
from forms.empleado import Empleados
from forms.horario import ventanaHorario
from forms.asignar import asigTurn
import utilerias.clases as cl
import utilerias.lista as cll
import forms.login as lg



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
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Menu')
          
        #Para obtener el tamaño máximo (maximizar ventana)                                    
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#E3FCBF')
        self.ventana.resizable(width=0, height=0)     
        utl.centrar_ventana(self.ventana, 800, 500)
 

        logo =utl.leer_img("./imagenes/logo.png", (300, 300))
        frame_resto = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_resto.pack(expand=tk.YES,fill=tk.BOTH)      
        #medio = tk.Label( frame_resto,bg='#fcfcfc' )
        #medio.place(x=50,y=0,relwidth=1, relheight=1)
        frame_sup = tk.Frame(frame_resto, bd=0, padx=5, pady=5,bg='#3a7ff6')
        frame_sup.place(x=0, y=0, width=800, height=100)
        title = tk.Label(frame_sup, text="Menu Principal",font=('Arial', 30, BOLD, ITALIC), fg="#fcfcfc",bg='#3a7ff6',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #frame_lateral = tk.Frame(frame_resto, bd=0, width=200, height=10000, padx=5, pady=5,bg='#3a7ff6')
        #frame_lateral.grid(row=0, column=0)
        
        self.empleado = tk.Button(self.ventana, bg = '#3a7ff6', fg="#fff",font=('Arial', 20, BOLD, ITALIC), text="Empleados",command= self.v_empleados)

        self.empleado.place(relx=0.35, rely=0.35 , relwidth= 0.3, relheight= 0.1 )
        self.agendar = tk.Button(self.ventana, bg = '#3a7ff6', fg="#fff",font=('Arial', 20, BOLD, ITALIC), text="Agendar",command= self.v_asig)
        self.agendar.place(relx=0.35, rely=0.55 , relwidth= 0.3, relheight= 0.1 )
        horario = tk.Button(self.ventana, bg = '#3a7ff6', fg="#fff",font=('Arial', 20, BOLD, ITALIC), text="Horario",command= self.v_horario)
        horario.place(relx=0.35, rely=0.75 , relwidth= 0.3, relheight= 0.1 )

      
        

        
        self.ventana.mainloop()