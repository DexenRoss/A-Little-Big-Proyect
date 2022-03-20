


class Nombre:

    nombre1= ""
    nombre2= ""
    apellidoP=""
    apellidoM=""

    def __init__(self,cadena):
        aux = cadena.split()
        if len(aux) == 4:
            self.nombre1 = aux[0]
            self.nombre2 = aux[1]
            self.apellidoP = aux[2]
            self.apellidoM = aux[3]
        else:
            self.nombre1 = aux[0]
            self.apellidoP = aux[1]
            self.apellidoM = aux[2]

#     def dar_nombre(self):
#         full_name= self.nombre1 + self.nombre2 + self.apellidoP + self.apellidoM
#         return full_name
# if __name__=='__main__':
#       nombre = Nombre("Osca Caballero Jimenez")
#       print(nombre.dar_nombre())

    