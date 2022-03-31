from Fecha import Fecha
from Nombre import Nombre
from RFC import RFC

#Eliminamos el metodo agregar_persona()
#Buscar:persona() lo metimos al main al igual que la creacion del arreglo de parsonas
#Hicimos la opcion 3, la de imprimir la lista de personas

class Persona:
    nombre= ""
    fecha=""
    rfc=""

    #__init__. constructor de la clase, en este caso Persona.
    def __init__(self, nombre, fecha):
        self.nombre=Nombre(nombre)
        self.fecha=Fecha(fecha) #es la fecha que se asigna en el main
        self.rfc=RFC(nombre,fecha)
        

    def nombre_completo(self):
        return self.nombre


    # def buscar_persona(self,name1):
    #     if self.personas==[]:
    #         print('LA LISTA ESTA VACIA:')

    #     else:
    #         for i in range(self.personas):
    #             if name1==self.nombre.juntar_nombre():
    #                 print('SE ENCONTRO A LA PERSONA Y SU RFC ES:')
    #                 print(self.regresar_rfc())


if __name__ == '__main__':
    personas=[]
    opcion=1

    while opcion!=0:
        print('INGRESA LA OPCION QUE DESEAS:')
        print('0.Salir')
        print('1.Ingresar a la persona')
        print('2.Buscar a la persona')
        print('3.Imprimir la lista completa')
        opcion=int(input('OPCION:'))
        if opcion==1:
            name1=input('INGRESA EL NOMBRE DE LA PERSONA: ')
            date1=input('INGRESA LA FECHA QUE DESEE EN FORMATO (dd/mm/aaaa): ')
            persona2= Persona(name1,date1)
            personas.append(persona2)
            print("lA PERSONA HA SIDO REGISTRADA EXITOSAMENTE")
        elif opcion==2:
            bandera = 0
            name2=input('INGRESA EL NOMBRE QUE QUIERA BUSCAR:')
            for i in personas:
                if i.nombre.juntar_nombre().find(name2.upper())!=-1:  
                    print('SE ENCONTRO A LA PERSONA Y SU RFC ES:')
                    print(i.rfc.regresar_rfc())
                    bandera=1
            if bandera ==0:
                print("ESA PERSONA NO EXISTE")
        elif opcion==3:
            for i in personas:
                print(i.nombre.juntar_nombre())
