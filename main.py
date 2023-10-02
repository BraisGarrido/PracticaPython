from Persona import Persona
from Coche import Coche

def main():
    p1=Persona("Pepe", 17, "123456789D")
    print(p1.mostrar())

    c1=Coche("", "audi", "a1", "1234DCK", 2500)
    c1.propietario=p1.nombre

    p2=Persona("Maria", 20, "987654321P")
    c1.propietario=p2.nombre

    c1.bajarPrecio(2200)
    c1.bajarPrecio(500)
    print(c1.mostrar())
main()