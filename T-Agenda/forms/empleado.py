
 
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


class editEm(tk.Frame):



    def mostrarInfo(self):
        self.Tx.config(state='normal')
        self.Tx.delete("1.0","end")
        print(self.cedula_tx.get())
        cedu = int(self.cedula_tx.get())
        if (log.emp.buscarporCedula(cedu) != -1):
            self.Tx.insert(tk.END, "===== Empleado ===== \n")
            self.Tx.insert(tk.END, "Nombre: "+log.emp.buscarporCedula(cedu).name +"\n")
            self.Tx.insert(tk.END, "Cedula: "+str(log.emp.buscarporCedula(cedu).cedula)+"\n")
            self.Tx.insert(tk.END, "Celular: "+log.emp.buscarporCedula(cedu).telefono+"\n")
            self.Tx.insert(tk.END, "Cargo: "+log.emp.buscarporCedula(cedu).cargos)
            self.modif['state']= "normal"
            self.elim['state']= "normal"
        else:
            self.Tx.insert(tk.END, "No encontrado \n")
            self.modif['state']= "disabled"
            self.elim['state']= "disabled"
        self.Tx.config(state='disabled')


    def edit(self):
        cedu = int(self.cedula_tx.get())
        if self.new.get() == "":
            self.infor_lbl.config(text="Ingrese el nuevo valor")
        else:
            if self.campo.get()=="Nombre":
                nameNew=self.new.get()
                cadena=""
                for line in open('empleados.txt'):
                    
                    reg = line.split(";")
                    aux=[]
                    if int(reg[1])== cedu:
                        nameViejo= log.emp.buscarporCedula(cedu).name
                        log.emp.buscarporCedula(cedu).name= nameNew
                        aux.append(line.replace(nameViejo, nameNew,1))
                    else:
                        aux.append(line)
                    for c in aux:
                        cadena+=str(c)
                self.infor_lbl.config(text="Nombre modificado \n correctamente")
                a= open('empleados.txt', 'w')
                a.write(cadena)           
                a.close()
            elif self.campo.get()=="Celular":
                newCel=self.new.get()
                cadena=""
                for line in open('empleados.txt'):
                    
                    reg = line.split(";")
                    aux=[]
                    if int(reg[1])== cedu:
                        celViejo= log.emp.buscarporCedula(cedu).telefono
                        log.emp.buscarporCedula(cedu).telefono= newCel
                        aux.append(line.replace(str(celViejo), str(newCel),1))

                    else:
                        aux.append(line)
                    for c in aux:
                        cadena+=str(c)

                a= open('empleados.txt', 'w')
                a.write(cadena)
                
                a.close()
                
                self.infor_lbl.config(text="Celular modificado \n correctamente")

            elif self.campo.get()=="Contraseña":
                newPass=self.new.get()
                cadena=""
                for line in open('empleados.txt'):
                    
                    reg = line.split(";")
                    aux=[]
                    if int(reg[1])== cedu:
                        passViejo= log.emp.buscarporCedula(cedu).contra
                        log.emp.buscarporCedula(cedu).telefono= newPass
                        aux.append(line.replace(passViejo, newPass,1))

                    else:
                        aux.append(line)
                    for c in aux:
                        cadena+=str(c)

                a= open('empleados.txt', 'w')
                a.write(cadena)
                
                a.close()
                
                self.infor_lbl.config(text="Contraseña modificada \n correctamente")

            elif self.campo.get()=="Cargo":
                newCar=self.new.get()
                cadena=""
                for line in open('empleados.txt'):
                    
                    reg = line.split(";")
                    aux=[]
                    if int(reg[1])== cedu:
                        carViejo= log.emp.buscarporCedula(cedu).cargos
                        log.emp.buscarporCedula(cedu).cargos= newCar
                        aux.append(line.replace(carViejo, newCar,1))

                    else:
                        aux.append(line)
                    for c in aux:
                        cadena+=str(c)

                a= open('empleados.txt', 'w')
                a.write(cadena)
                
                a.close()
                
                self.infor_lbl.config(text="Cargo modificado \n correctamente")

    def elimEm(self):
        cedu = int(self.cedula_tx.get())
        cadena=""
        for line in open('empleados.txt'):
            
            reg = line.split(';')
            aux=[]
            if int(reg[1])!=cedu:
                aux.append(line)
            for c in aux:
                 cadena+=str(c)
        a= open('empleados.txt', 'w')
        a.write(cadena)
        a.close()
        cadena1=""
        for line in open('file.txt'):
            
            reg = line.split(';')
            aux=[]
            if int(reg[0])!=cedu:
                aux.append(line)
            for c in aux:
                 cadena1+=str(c)
        a= open('file.txt', 'w')
        a.write(cadena1)
        a.close()
        self.infor_lbl.config(text="Empleado eliminado \n correctamente")
        self.cedula_tx.delete(0,tk.END)
        self.Tx.config(state='normal')
        self.Tx.delete("1.0","end")
        self.Tx.config(state='disabled')
        


    def v_menu(self):
        self.frame_inf.destroy()
        self.frame_sup.destroy()

        
        opciones(self.root, self.op1, self.op2, self.op3)



    def __init__(self,root:Tk) :
        
        self.root=root
        self.op1 =utl.leer_img("./imagenes/add.png", (45, 45))
        self.op2 =utl.leer_img("./imagenes/edit.png", (45, 45))
        self.op3 =utl.leer_img("./imagenes/delete.png", (45, 45))
        self.frame_sup = tk.Frame(root, bd=0, width=800, height=100,  bg='#2dc2a1')
        self.frame_sup.grid(row=0, column=0)
        title_lbl = tk.Label(root, text="Editar Empleados", font=('Arial', 30, BOLD, ITALIC ),
         bg='#2dc2a1', fg='#fcfcfc')

        title_lbl.grid(row=0, column=0)
        self.frame_inf = tk.Frame(root, bd=0, width=800, height=700,  bg='#1a6958')
        self.frame_inf.grid(row=1, column=0)

        #cedula
        cedula_lbl=tk.Label(self.frame_inf, text="Cedula", font=('Arial', 15, BOLD ),  bg='#1a6958',
         fg='#fcfcfc')

        cedula_lbl.place(x=70, y=70)
        self.cedula_tx= tk.Entry(self.frame_inf,width=27)
        self.cedula_tx.place(x=70, y= 100)
        buscar= tk.Button(self.frame_inf, text= "Buscar", font=('Arial', 12, BOLD ), bg="#09872f",
         fg='#fcfcfc',width=16, command=self.
        mostrarInfo)
        buscar.place(x=70, y= 130)

        self.Tx = tk.Text(self.frame_inf, height = 10, width = 20, state='disabled')
        self.Tx.place(x=70, y=170)
        

        
        
        new_lbl=tk.Label(self.frame_inf, text="Nuevo valor", font=('Arial', 15, BOLD ),  bg='#1a6958', 
        fg='#fcfcfc')
        new_lbl.place(x=350, y=150)

        self.new =ttk.Entry(self.frame_inf, width=27)
        self.new.place(x=350, y=180)

        self.campo =ttk.Combobox(self.frame_inf, state="readonly")
        self.campo['values']= ("Nombre", "Celular", "Contraseña", "Cargo")
       
        campo_lbl=tk.Label(self.frame_inf, text="Campo a modificar", font=('Arial', 15, BOLD ), 
         bg='#1a6958', fg='#fcfcfc')
        campo_lbl.place(x=350, y=70)

        self.campo.place(x=350, y=100)
        self.campo.current(0)
        

        self.modif= tk.Button(self.frame_inf, text= "Modificar", font=('Arial', 12, BOLD ),
         bg="#09872f", fg='#fcfcfc', width=15, command=self.edit)
        self.modif['state']= "disabled"
        self.modif.place(x=350, y= 250)

        self.elim= tk.Button(self.frame_inf, text= "Eliminar", font=('Arial', 12, BOLD ),
         bg="#09872f", fg='#fcfcfc', width=15, command=self.elimEm)
        self.elim['state']= "disabled"
        self.elim.place(x=350, y= 300)
        
        
        volver= tk.Button(root, text= "VOLVER",font=('Arial', 12, BOLD ),
         bg="#09872f", fg='#fcfcfc', width=15, command=self.v_menu)

        volver.place(x=630, y= 460)
        self.infor_lbl=tk.Label(self.frame_inf, text="", font=('Arial', 15, BOLD ),  
        bg='#1a6958', fg='#fff')
        self.infor_lbl.place(x=350, y=350)

class regEm(tk.Frame):
    def regist(self):
        if(self.name_tx.get()=="" or self.cedula_tx.get()=="" or self.cargo_tx.get()=="" or 
        self.cel_tx.get()=="" or self.pass_tx.get()==""):

            self.Tx.config(state='normal')
            self.Tx.delete("1.0","end")
            self.Tx.insert(tk.END, "FALTAN CAMPOS \n")
            self.Tx.config(state='disabled')
        else:
            self.Tx.config(state='normal')
            file = open('empleados.txt', 'a')
            arc = open('file.txt', 'a')
            new = self.name_tx.get()+";"+self.cedula_tx.get()+";"+self.cargo_tx.get()+";"+self.cel_tx.get()+";"+self.pass_tx.get()+";dia;inicio;fin;0"

            n2 = self.cedula_tx.get()+";d0;i0;f0;d1;i1;f1;d2;i2;f2;d3;i3;f3;d4;i4;f4;d5;i5;f5;d6;i6;f6;"

            file.write(new+"\n")
            arc.write(n2+"\n")
            ob= Empleado(self.name_tx.get(), int(self.cedula_tx.get()), self.cargo_tx.get(),
             self.cel_tx.get(), self.pass_tx.get())
            log.emp.insert(ob)
            self.Tx.delete("1.0","end")
            self.Tx.insert(tk.END, "EMPLEADO REGISTRADO \n")
            self.Tx.config(state='disabled')
            self.name_tx.delete(0,tk.END)
            self.cedula_tx.delete(0,tk.END)
            self.cargo_tx.delete(0,tk.END)
            self.cel_tx.delete(0,tk.END)
            self.pass_tx.delete(0,tk.END)
            file.close()
            arc.close()

    def v_menu(self):
        self.frame_inf.destroy()
        self.frame_sup.destroy()

        
        opciones(self.root, self.op1, self.op2, self.op3)



    def __init__(self,root:Tk, user:Empleado=None) :
        self.user=user
        self.root=root
        self.op1 =utl.leer_img("./imagenes/add.png", (45, 45))
        self.op2 =utl.leer_img("./imagenes/edit.png", (45, 45))
        self.op3 =utl.leer_img("./imagenes/delete.png", (45, 45))
        self.frame_sup = tk.Frame(root, bd=0, width=800, height=100,  bg='#2dc2a1')
        self.frame_sup.grid(row=0, column=0)
        title_lbl = tk.Label(root, text="Registro de Empleados", font=('Arial', 30, BOLD, ITALIC ), 
        bg='#2dc2a1', fg='#fcfcfc')
        title_lbl.grid(row=0, column=0)
        self.frame_inf = tk.Frame(root, bd=0, width=800, height=700,  bg='#1a6958')
        self.frame_inf.grid(row=1, column=0)

        #Nombre
        name_lbl=tk.Label(self.frame_inf, text="Nombre", font=('Arial', 15, BOLD ),  
        bg='#1a6958', fg='#fcfcfc')

        name_lbl.place(x=50, y=50)
        self.name_tx= tk.Entry(self.frame_inf,width=20)
        self.name_tx.place(x=50, y= 90)

        #cedula
        cedula_lbl=tk.Label(self.frame_inf, text="Cedula", font=('Arial', 15, BOLD ),  
        bg='#1a6958', fg='#fcfcfc')

        cedula_lbl.place(x=50, y=120)
        self.cedula_tx= tk.Entry(self.frame_inf,width=20)
        self.cedula_tx.place(x=50, y= 150)

        #cel
        cel_lbl=tk.Label(self.frame_inf, text="Celular", font=('Arial', 15, BOLD ),  
        bg='#1a6958', fg='#fcfcfc')

        cel_lbl.place(x=50, y=180)
        self.cel_tx= tk.Entry(self.frame_inf,width=20)
        self.cel_tx.place(x=50, y= 210)

        #contra
        pass_lbl=tk.Label(self.frame_inf, text="Contraseña", font=('Arial', 15, BOLD ), 
         bg='#1a6958', fg='#fcfcfc')

        pass_lbl.place(x=50, y=240)
        self.pass_tx= tk.Entry(self.frame_inf,width=20)
        self.pass_tx.config(show="*")
        self.pass_tx.place(x=50, y= 270)

        #cargo
        cargo_lbl=tk.Label(self.frame_inf, text="Cargo", font=('Arial', 15, BOLD ),  
        bg='#1a6958', fg='#fcfcfc')

        cargo_lbl.place(x=50, y=300)
        self.cargo_tx= tk.Entry(self.frame_inf,width=20)
        self.cargo_tx.place(x=50, y= 330)

        regis = tk.Button(self.frame_inf, text= "Registrar", font=('Arial', 15, BOLD ),
         bg="#09872f", fg='#fcfcfc', width = 13, command=self.regist)
        regis.place(x=250, y= 280)

        volver= tk.Button(root, text= "VOLVER",font=('Arial', 12, BOLD ), 
        bg="#09872f", fg='#fcfcfc', width=15, command=self.v_menu)
        volver.place(x=630, y= 460)
        

        self.Tx = tk.Text(self.frame_inf, height = 10, width = 20, state='disabled')
        self.Tx.place(x=250, y=90)
        inf_lbl = tk.Label(self.frame_inf, text="Información", font=('Arial', 15, BOLD ),  
        bg='#1a6958', fg='#fcfcfc')
        inf_lbl.place(x=250, y= 50)




class opciones(tk.Frame):

    def v_menu(self):
        self.root.destroy()
        if log.emp.buscar(log.act[0], log.act[1]).permiso==0:
            v.Inicio(0,log.emp.buscar(log.act[0], log.act[1])) 
        elif log.emp.buscar(log.act[0], log.act[1]).permiso==1:
            v.Inicio(1, log.emp.buscar(log.act[0], log.act[1]))

    def registro(self):
        self.frame_sup.destroy()
        regEm(self.root)

    def editar(self):
        self.frame_sup.destroy()
        editEm(self.root)

    def __init__(self, root:Tk, op1:ImageTk.PhotoImage, op2:ImageTk.PhotoImage, op3: ImageTk.PhotoImage):
        self.root=root
        self.frame_sup = tk.Frame(root, bd=0, width=800, height=100,  bg='#baf7f1')
        self.frame_sup.place(relheight=1, relwidth=1)
        if op1 !=0:
            regis = tk.Button(self.frame_sup, text= "Registrar Empleado", font=('Arial', 20, BOLD, ITALIC ), 
            bg="#11998b", fg='#fcfcfc', compound="right" ,image=op1, overrelief="flat",
            command=self.registro)
            regis.place(relx=0.30, rely=0.15,relwidth= 0.4, relheight= 0.15)

            mod = tk.Button(self.frame_sup, text= "Editar/Eliminar  ", font=('Arial', 20, BOLD, ITALIC ), 
            bg="#11998b", fg='#fcfcfc', image=op2, compound="right", overrelief="flat",
            command=self.editar)
            mod.place(relx=0.30, rely=0.40,relwidth= 0.4, relheight= 0.15)

            volver = tk.Button(self.frame_sup, text= "Volver", font=('Arial',20, BOLD, ITALIC), 
            bg="#11998b", fg='#fcfcfc', image=op3, compound="right", overrelief="flat",
            command=self.v_menu)
            volver.place(relx=0.30, rely=0.65,relwidth= 0.4, relheight= 0.15)
        else:
            regis = tk.Button(self.frame_sup, text= "Registrar Empleado", font=('Arial', 20, BOLD, ITALIC ), 
            bg="#11998b", fg='#fcfcfc', overrelief="flat",
            command=self.registro)
            regis.place(relx=0.30, rely=0.15,relwidth= 0.4, relheight= 0.15)

            mod = tk.Button(self.frame_sup, text= "Editar/Eliminar  ", font=('Arial', 20, BOLD, ITALIC ), 
            bg="#11998b", fg='#fcfcfc', overrelief="flat",
            command=self.editar)
            mod.place(relx=0.30, rely=0.40,relwidth= 0.4, relheight= 0.15)

            volver = tk.Button(self.frame_sup, text= "Volver", font=('Arial',20, BOLD, ITALIC), 
            bg="#11998b", fg='#fcfcfc', overrelief="flat",
            command=self.v_menu)
            volver.place(relx=0.30, rely=0.65,relwidth= 0.4, relheight= 0.15)
        

        

class Empleados:

     
    
    def __init__(self):  
        
        self.ventana = tk.Tk()                             
        self.ventana.title('EMPLEADOS')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#B8FFF9')
        self.ventana.resizable(width=0, height=0)          
        utl.centrar_ventana(self.ventana, 800, 500)
        self.op1 =utl.leer_img("./imagenes/add.png", (45, 45))
        self.op2 =utl.leer_img("./imagenes/edit.png", (45, 45))
        self.op3 =utl.leer_img("./imagenes/delete.png", (45, 45))
        opciones(self.ventana, self.op1, self.op2, self.op3)

        

        self.ventana.mainloop()


