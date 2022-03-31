class Nombre:
    nombre=""
    apellidopaterno=""
    apellidomaterno=""
    nombre_completo=""

    def __init__(self,name):
        aux=name.upper().split(" ")
        self.nombre= aux[0]
        self.apellidopaterno=aux[1]
        self.apellidomaterno=aux[2]

    def juntar_nombre(self):
        self.nombre_completo=self.nombre+" "+self.apellidopaterno+" "+self.apellidomaterno
        return self.nombre_completo

    