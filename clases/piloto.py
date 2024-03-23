from datetime import datetime
import escuderia as escuderiaAUX
class Piloto:
    def __init__(self, nombre, escuderia, fechaNacimiento,campeonatos):
        self._nombre = nombre
        self._escuderia = escuderia
        self._fechaNacimiento = datetime.strptime(fechaNacimiento,'%Y-%m-%d').date()#Formato Fecha
        self._campeonatos = campeonatos

    
    #Métodos get
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def escuderia(self):
        return self._escuderia
    
    @property
    def fechaNacimiento(self):
        return self._fechaNacimiento
    
    @property
    def campeonatos(self):
        return self._campeonatos

    #Métodos setter
    @nombre.setter
    def nombre(self,newNombre):
        self.nombre = newNombre
    
    @fechaNacimiento.setter
    def fechaNacimiento(self,newfechaNacimiento):
        self.fundacion = newfechaNacimiento
    
    @escuderia.setter
    def escuderia(self,newEscuderia:escuderiaAUX):
        self.escuderia = newEscuderia

    @campeonatos.setter
    def campeonatos(self, newCampeonatos):
        self.campeonatos = newCampeonatos

    def __str__(self):
        return f"Nombre: {self.nombre}, Escuderia: {self.escuderia.nombre}, Fecha de Nacimiento: {self.fechaNacimiento}, campeonatos: {self.campeonatos}"