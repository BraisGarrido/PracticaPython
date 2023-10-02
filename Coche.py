from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, propietario="", marca="", modelo="", matricula="", precioVenta=0):
        super().__init__(propietario, marca, modelo)
        self.__matricula=matricula
        self.__precioVenta=precioVenta
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula=matricula
    
    @property
    def precioVenta(self):
        return self.__precioVenta
    
    @precioVenta.setter
    def precioVenta(self, precioVenta):
        self.__precioVenta=precioVenta
    
    def mostrar(self):
        return (super().mostrar()+"\n Matricula: "+self.matricula+"\n Precio venta: "+str(self.precioVenta))
    
    def bajarPrecio(self, cantidad):
        if self.precioVenta > 0:
            if cantidad > 0:
                self.__precioVenta=self.precioVenta-cantidad
            else:
                print("La cantidad debe ser mayor a 0")
        else:
            print("El precio de venta no puede ser inferior a 0")