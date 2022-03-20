from Fecha import Fecha 
from Nombre import Nombre
from RFC import RFC


class Persona:
    nombre=""
    fecha=""
    rfc=""
    #_init_. constructor de la clase, en este caso Persona.
    def __init__(self,nombre, fecha):
        self.nombre= Nombre(nombre)
        self.fecha= Fecha(fecha)
        self.rfc= RFC(nombre, fecha)

    def nombre_completo(self):
        return self.nombre.split()

    



if __name__ == '__main__':
        date= input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa")
        persona1= Persona('Angelica Acevedo Cervantes', date, 'AA0412C')
        
        print(persona1.nombre_completo())