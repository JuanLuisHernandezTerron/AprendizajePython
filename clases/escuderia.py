from piloto import Piloto as pilotoClass
from datetime import datetime
class Escuderia:
    def __init__(self, nombre, base, fundacion):
        self._nombre = nombre
        self._base = base
        self._fundacion = datetime.strptime(fundacion,'%Y-%m-%d').date()#Formato Fecha
        self._pilotos = []

    #Método getter
    @property
    def nombre(self):
        return self._nombre
    @property
    def base(self):
        return self._base
    
    @property
    def fundacion(self):
        return self._fundacion
    
    @property
    def pilotos(self):
        return self._pilotos

    #Métodos Setters
    @nombre.setter
    def nombre(self,newNombre):
        self._nombre = newNombre

    @base.setter
    def base(self,newbase):
        self._base = newbase
    
    @fundacion.setter
    def fundacion(self,newfundacion):
        self._fundacion = newfundacion
    
    @pilotos.setter
    def set_pilotos(self,newPiloto:pilotoClass):
        self._pilotos.append(newPiloto)



    def __str__(self):
        return f"Nombre: {self.nombre}, base: {self.base}, Fundacion: {self.fundacion}, pilotos: {[pilotos.nombre for pilotos in self.pilotos]}"
    
    
    
    


