class Vehiculo():
    def __init__(self, propietario="", marca="", modelo=""):
        self.__propietario=propietario
        self.__marca=marca
        self.__modelo=modelo
    
    @property
    def propietario(self):
        return self.__propietario

    @propietario.setter
    def propietario(self, propietario):
        self.__propietario=propietario
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca=marca
    
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo=modelo
    
    def mostrar(self):
        return("DATOS DEL VEHICULO"+"\n Propietario: "+self.propietario+"\n Marca: "+self.marca+"\n Modelo: "+self.modelo)