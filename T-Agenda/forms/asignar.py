import tkinter as tk
from tkinter import W, ttk
from tkinter.font import BOLD, ITALIC
from tkinter.tix import COLUMN
import utilerias.util as utl
import forms.ventana as v
import forms.login as lg

class asigTurn():

    def v_menu(self):
        self.ventana.destroy()
        if lg.emp.buscar(lg.act[0], lg.act[1]).permiso==0:
            v.Inicio(0,lg.emp.buscar(lg.act[0], lg.act[1])) 
        elif lg.emp.buscar(lg.act[0], lg.act[1]).permiso==1:
            v.Inicio(1, lg.emp.buscar(lg.act[0], lg.act[1]))
        
    def mostrarInfo(self):
        
        self.Tx.config(state='normal')
        self.Tx.delete("1.0","end")
        print(self.cedula_tx.get())
        cedu = int(self.cedula_tx.get())
        if (lg.emp.buscarporCedula(cedu) != -1):
            self.Tx.insert(tk.END, "===== Empleado ===== \n")
            self.Tx.insert(tk.END, "Nombre: "+lg.emp.buscarporCedula(cedu).name +"\n")
            self.Tx.insert(tk.END, "Cedula: "+str(lg.emp.buscarporCedula(cedu).cedula)+"\n")
            self.Tx.insert(tk.END, "Celular: "+lg.emp.buscarporCedula(cedu).telefono+"\n")
            self.Tx.insert(tk.END, "Turno: \n")
            self.Tx.insert(tk.END, "-Dia: "+lg.emp.buscarporCedula(cedu).turno.dia +"\n")
            self.Tx.insert(tk.END, "-Inicio: "+lg.emp.buscarporCedula(cedu).turno.inicio +"\n")
            self.Tx.insert(tk.END, "-Fin: "+lg.emp.buscarporCedula(cedu).turno.fin +"\n")
            self.asig['state']= "normal"
        else:
            self.Tx.insert(tk.END, "No encontrado \n")
            self.asig['state']= "disabled"
        self.Tx.config(state='disabled')

    def asignar(self):
        cedu = int(self.cedula_tx.get())
        if (lg.emp.buscarporCedula(cedu) != -1):
            
            cadena=""
            for renglon in open('empleados.txt'):
                aux=[]
                reg = renglon.split(';')
                tur =reg[5]+";"+reg[6]+";"+reg[7]
                tunew=self.dia.get()+";"+self.inicio.get()+";"+self.fin.get()
                
                if int(reg[1])==cedu:
                    aux.append(renglon.replace(tur,tunew,1))
                else:
                    aux.append(renglon)
                for c in aux:
                    cadena+=str(c)
            a= open('empleados.txt', 'w')
            a.write(cadena)
            a.close()
            lg.emp.buscarporCedula(cedu).turno.dia = self.dia.get()
            lg.emp.buscarporCedula(cedu).turno.inicio = self.inicio.get()
            lg.emp.buscarporCedula(cedu).turno.fin = self.fin.get()
            self.infor_lbl['text']="Turno asignado exitosamente"

    def __init__(self):  
        self.ventana = tk.Tk()                             
        self.ventana.title('Asignar')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)          
        utl.centrar_ventana(self.ventana, 800, 500)

        frame_sup = tk.Frame(self.ventana, bd=0, width=800, height=100,  bg='#2dc2a1')
        frame_sup.grid(row=0, column=0)
        title_lbl = tk.Label(self.ventana, text="Asignar Turnos", font=('Arial', 30, BOLD, ITALIC ), bg='#2dc2a1', fg='#fcfcfc')
        title_lbl.grid(row=0, column=0)
        frame_inf = tk.Frame(self.ventana, bd=0, width=800, height=700,  bg='#1a6958')
        frame_inf.grid(row=1, column=0)

        #cedula
        cedula_lbl=tk.Label(frame_inf, text="Cedula", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        cedula_lbl.place(x=70, y=70)
        self.cedula_tx= tk.Entry(frame_inf,width=27)
        self.cedula_tx.place(x=70, y= 100)
        buscar= tk.Button(frame_inf, text= "Buscar", font=('Arial', 12, BOLD ), bg="#09872f", fg='#fcfcfc',width=16, command=self.
        mostrarInfo)
        buscar.place(x=70, y= 130)

        self.Tx = tk.Text(frame_inf, height = 10, width = 20, state='disabled')
        self.Tx.place(x=70, y=170)
        

        self.dia =ttk.Combobox(frame_inf, state="readonly")
        self.dia['values']= ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
        self.dia.place(x=350, y=100)
        self.dia.current(0)
        dia_lbl=tk.Label(frame_inf, text="Dia", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        dia_lbl.place(x=350, y=70)

        self.inicio =ttk.Combobox(frame_inf, state="readonly")
        self.inicio['values']= ("6 am", "7 am", "8 am", "9 am", "10 am", "11 am", "12 pm", "13 pm", "14 pm", "15 pm", "16 pm", "17 pm", "18 pm", "19 pm", "20 pm ", "21 pm", "22 pm", "23 pm")
        self.inicio.place(x=350, y=160)
        self.inicio.current(0)
        inicio_lbl=tk.Label(frame_inf, text="Hora de inicio", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        inicio_lbl.place(x=350, y=130)
        
        self.fin =ttk.Combobox(frame_inf, state="readonly")
        self.fin['values']= ("7 am", "8 am", "9 am", "10 am", "11 am", "12 pm", "13 pm", "14 pm", "15 pm", "16 pm", "17 pm", "18 pm", "19 pm", "20 pm ", "21 pm", "22 pm", "23 pm")
        self.fin.place(x=350, y=220)
        self.fin.current(0)
        fin_lbl=tk.Label(frame_inf, text="Hora de finalización", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fcfcfc')
        fin_lbl.place(x=350, y=190)

        self.asig= tk.Button(frame_inf, text= "Asignar turno", font=('Arial', 12, BOLD ), bg="#09872f", fg='#fcfcfc', width=15, command=self.asignar)
        self.asig['state']= "disabled"
        self.asig.place(x=350, y= 260)
        
        
        volver= tk.Button(frame_inf, text= "VOLVER",font=('Arial', 12, BOLD ), bg="#09872f", fg='#fcfcfc', width=15, command=self.v_menu)
        volver.place(x=630, y= 360)
        self.infor_lbl=tk.Label(frame_inf, text="", font=('Arial', 15, BOLD ),  bg='#1a6958', fg='#fff')
        self.infor_lbl.place(x=350, y=300)