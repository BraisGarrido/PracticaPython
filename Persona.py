class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        self.__dni=dni
    
    def mostrar(self):
        return("DATOS DE LA PERSONA"+"\n Nombre: "+self.nombre+"\n Edad: "+str(self.edad)+"\n Dni: "+self.dni)

    def esMayorEdad(self):
        if self.edad < 18:
            print("El usuario "+self.nombre+" tiene "+str(self.edad)+" años. Es menor de edad")
        else:
            print("El usuario "+self.nombre+" tiene "+str(self.edad)+" años. Es mayror de edad")