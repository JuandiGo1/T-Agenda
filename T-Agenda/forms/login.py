import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.ventana import Inicio
import utilerias.util as utl
import utilerias.clases as cl

admin= cl.Admin()
admin.User= "Admin"
admin.Password = "contra123"
class PanelPrincipal:
    
    def verificar(self):
        
        usu = self.usuario.get()
        password = self.password.get()        
        if(usu == admin.User and password == admin.Password) :
            self.ventana.destroy()
            Inicio()
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