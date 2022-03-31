from Fecha import Fecha
from Nombre import Nombre

#El constructor definio el rfc

class RFC:
    # sumando1=""
    # sumando2=""
    nombre=""
    fecha=""
    rfc=""

    def __init__(self,nombre,fecha):
        self.nombre=Nombre(nombre)
        self.fecha=Fecha(fecha)
        self.rfc = self.buscador_de_letras() + self.buscador_de_numeros()
       



    def buscador_de_letras(self):
        auxiliar=self.nombre.nombre[0]
        auxiliar2=self.nombre.apellidopaterno[0:2] #busca hasta el limite que pongas -1
        auxiliar3=self.nombre.apellidomaterno[0]

        resultado=auxiliar2+auxiliar3+auxiliar
        return resultado

    def buscador_de_numeros(self):
        auxiliar=self.fecha.dia
        auxiliar2=self.fecha.mes
        auxiliar3=self.fecha.anio
        aux4=auxiliar3[2:4]
        resultado=aux4+auxiliar2+auxiliar
        return resultado

    def regresar_rfc(self):
        # self.rfc= self.sumando1+self.sumando2
        return self.rfc


