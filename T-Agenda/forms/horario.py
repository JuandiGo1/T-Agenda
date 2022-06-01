import tkinter as tk
from tkinter.font import BOLD, ITALIC
from utilerias.clases import Empleado
import utilerias.util as utl
import forms.ventana as v
import forms.login as lg

class ventanaHorario:
    def v_menu(self):
        self.ventana.destroy()
        if lg.emp.buscar(lg.act[0], lg.act[1]).permiso==0:
            v.Inicio(0,lg.emp.buscar(lg.act[0], lg.act[1])) 
        elif lg.emp.buscar(lg.act[0], lg.act[1]).permiso==1:
            v.Inicio(1, lg.emp.buscar(lg.act[0], lg.act[1]))
        

    def VerLunes(self):
        
        self.Tx.config(state='normal')
        self.Tx.delete("1.0","end")
        
        lg.emp.mostrarHorario("Lunes", self.Tx)
        
        self.Tx.config(state='disabled')
    
    def VerMartes(self):
        self.Tx.config(state='normal')
        self.Tx.delete("1.0","end")
        
        lg.emp.mostrarHorario("Martes", self.Tx)
        self.Tx.config(state='disabled')

    def VerMierc(self):
        self.Tx.config(state='normal')
        self.Tx.delete("1.0","end")
        lg.emp.mostrarHorario("Miercoles", self.Tx)
        self.Tx.config(state='disabled')
    
    def VerJueves(self):
        self.Tx.config(state='normal')
        file= open('empleados.txt','r')
        self.Tx.delete("1.0","end")
        lg.emp.mostrarHorario("Jueves", self.Tx)
        self.Tx.config(state='disabled')
    
    def VerViernes(self):
        self.Tx.config(state='normal')
        file= open('empleados.txt','r')
        self.Tx.delete("1.0","end")
        lg.emp.mostrarHorario("Viernes", self.Tx)
        self.Tx.config(state='disabled')

    def VerSaba(self):
        self.Tx.config(state='normal')
        file= open('empleados.txt','r')
        self.Tx.delete("1.0","end")
        lg.emp.mostrarHorario("Sabado", self.Tx)
        self.Tx.config(state='disabled')

    def VerDomi(self):
        self.Tx.config(state='normal')
        file= open('empleados.txt','r')
        self.Tx.delete("1.0","end")
        lg.emp.mostrarHorario("Domingo", self.Tx)
        self.Tx.config(state='disabled')

    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Horario')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight() 
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        #utl.centrar_ventana(self.ventana, 850, 500)                                   
        
        self.ventana.config(bg='#baf7f1')
        self.ventana.resizable(width=0, height=0)     
        
        
        #frame_sup = tk.Frame(self.ventana, bd=0, width=1000, height=100,  bg='#11998b')
        #frame_sup.grid(row=0, column=0)
        lunes = tk.Button(self.ventana, text="LUNES", font=('Arial', 20, BOLD, ITALIC ), bg='#11998b', fg='#fcfcfc', command=self.VerLunes)
        lunes.place(x=20, y=20, relwidth= 0.14, relheight= 0.1)
        
        martes = tk.Button(self.ventana, text="MARTES", font=('Arial', 20, BOLD, ITALIC ), bg='#095951', fg='#fcfcfc',command=self.VerMartes)
        martes.place(x=20, y=100, relwidth= 0.14, relheight= 0.1)
        
        miercoles = tk.Button(self.ventana, text="MIÉRCOLES", font=('Arial', 20, BOLD, ITALIC ), bg='#11998b', fg='#fcfcfc',command=self.VerMierc)
        miercoles.place(x=20, y=180, relwidth= 0.14, relheight= 0.1)
        
        jueves = tk.Button(self.ventana, text="JUEVES", font=('Arial', 20, BOLD, ITALIC ), bg='#095951', fg='#fcfcfc',command=self.VerJueves)
        jueves.place(x=20, y=260, relwidth= 0.14, relheight= 0.1)
        
        viernes = tk.Button(self.ventana, text="VIERNES", font=('Arial', 20, BOLD, ITALIC ), bg='#11998b', fg='#fcfcfc',command=self.VerViernes)
        viernes.place(x=20, y=340, relwidth= 0.14, relheight= 0.1)
        
        sabado = tk.Button(self.ventana, text="SÁBADO", font=('Arial', 20, BOLD, ITALIC ), bg='#095951', fg='#fcfcfc',command=self.VerSaba)
        sabado.place(x=20, y=420, relwidth= 0.14, relheight= 0.1)
        
        domingo = tk.Button(self.ventana, text="DOMINGO", font=('Arial', 20, BOLD, ITALIC ), bg='#11998b', fg='#fcfcfc',command=self.VerDomi)
        domingo.place(x=20, y=500, relwidth= 0.14, relheight= 0.1)

        self.Tx = tk.Text(self.ventana, height = 37, width = 70,font=('Arial', 12, BOLD ), state='disabled')
        self.Tx.place(x=240, y=20)
        self.inf = tk.Label(self.ventana, font=('Arial', 20, BOLD, ITALIC ), text= "Seleccione el dia para mostrar los \n turnos asignados", bg='#baf7f1')
        self.inf.place(x=880,y=20)
        volver= tk.Button(self.ventana, text= "VOLVER",font=('Arial', 20, BOLD, ITALIC), bg="#09872f", fg='#fcfcfc', width=15, command=self.v_menu)
        volver.place(x=20, y= 650,relwidth= 0.14, relheight= 0.1)
        #volver.grid(row=5, column=5)

        self.ventana.mainloop()


