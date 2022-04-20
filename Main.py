class User:
    Password = None
    User = None

    def login(self):
        pass

class Empleado(User):
    def __init__(self, name, cedula, cargos, telefono):
        self.name = name
        self.cedula = cedula
        self.telefono = telefono
        self.cargos = cargos
    
    def verHorario(turno):
        pass
    
    def actualizarContra():
        pass
    
class Admin(User):
    def regEmpleado(name, cedula, cargos, telefono):
        pass
    def deleteEmpleado(cedula):
        pass
    def AsignarHorario(Empleado):
        pass
