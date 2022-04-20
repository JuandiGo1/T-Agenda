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
class turno:


    turnoAsignado= 0
    cargoAsignado = "Ninguno"

    def __init__(self):
        self.tunoAsignado= 0
        self.cargoAsignado= "Ninguno"



class Horario:
    dias = "Ninguno"
    horas = 0  

    def__init__(self):
        self.dias = "Ninguno"
        self.horas = 0

class posicion:

    #Aqui ocuparemos la API de google maps para obtener la posicion del usuario 
    # y guardaremos esta posicion en una variable llamada coordenadas
    coordenadas = posision_usuario 

    def compararCoordenadas():
        #esta funcion nos va a servir para comparar la ubicacion del usuario
        #con la ubicacion del usuario utilizando la api de google 


class puntaje:


    puntual = verdadero

    def __init__(self):
        self.puntual = verdadero
