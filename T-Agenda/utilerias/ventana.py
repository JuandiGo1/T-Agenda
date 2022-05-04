import tkinter as tk
from tkinter.font import BOLD
import utilerias.util as utl

class Inicio:
    
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Menu')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()  
        #Para obtener el tamaño máximo (maximizar ventana)                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)      

        logo =utl.leer_img("./imagenes/logo.png", (300, 300))
        frame_resto = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_resto.pack(expand=tk.YES,fill=tk.BOTH)      
        #medio = tk.Label( frame_resto,bg='#fcfcfc' )
        #medio.place(x=50,y=0,relwidth=1, relheight=1)
        frame_sup = tk.Frame(frame_resto, bd=0, padx=5, pady=5,bg='#879fed')
        frame_sup.place(x=0, y=0, width=1400, height=100)
        title = tk.Label(frame_sup, text="Menu Principal",font=('Times', 30, BOLD), fg="#fcfcfc",bg='#3a7ff6',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #frame_lateral = tk.Frame(frame_resto, bd=0, width=200, height=10000, padx=5, pady=5,bg='#3a7ff6')
        #frame_lateral.grid(row=0, column=0)
        
        empleado = tk.Button(self.ventana,text="Empleados",font=('Times', 15,BOLD),bg='#879fed', bd=0,fg="#fff")

        empleado.place(relx=0.35, rely=0.3 , relwidth= 0.25, relheight= 0.1 )
        
        





        
        self.ventana.mainloop()