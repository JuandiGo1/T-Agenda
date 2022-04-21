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
        
                        
        label = tk.Label( self.ventana)
        label.place(x=0,y=0,relwidth=1, relheight=1)
        a = tk.Label(self.ventana, text="Contraseña", font=('Times', 14),fg="#fcfcfc",bg='#3a7ff6' , anchor="w")
        
        self.ventana.mainloop()