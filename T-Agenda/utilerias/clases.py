
import string


class User:
    def __init__(self):
        self.contra = None
        self.name = None

    def login(self):
        pass

class turnos():
    def __init__(self, dia:string, inicio, fin):
        self.dia = dia
        self.inicio = inicio
        self.fin=fin

base = turnos("NA","NA","NA")

class Empleado(User):
    
    def __init__(self, name, cedula, cargos, telefono, contra, tur:turnos = base):
        self.name = name
        self.cedula = cedula
        self.telefono = telefono
        self.cargos = cargos
        self.turno = tur
        self.contra = contra
        self.permiso=0
    
    def verHorario(turno):
        pass
    
    def actualizarContra():
        pass
    
class turnos():
    def __init__(self, dia:string, inicio, fin):
        self.dia = dia
        self.inicio = inicio
        self.fin=fin

class Admin(User):
    def __init__(self, name, cedula, telefono, contra):
        self.name = name
        self.cedula = cedula
        self.telefono = telefono
        self.contra = contra

    def regEmpleado(name, cedula, cargos, telefono):
        pass
    def deleteEmpleado(cedula):
        pass
    def AsignarHorario(Empleado):
        pass


