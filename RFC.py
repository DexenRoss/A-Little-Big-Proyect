from Fecha import Fecha
from Nombre import Nombre

class RFC:
    nombre=""
    fecha=""
    rfc=""

    def __init__(self,nombre,fecha):
        self.nombre = Nombre(nombre)
        self.fecha = Fecha(fecha)
        self.rfc = sacar_iniciales() + sacar_digitos()
        

    def sacar_iniciales(self):
        n1 = self.nombre.nombre1[0]
        ap = self.nombre.apellidoP[0:1]
        am = self.nombre.apellidoM[0]
        parte_cadena= ap + am + n1
        return parte_cadena

    def sacar_digitos(self):
        d = str(self.fecha.dia)
        m = str(self.fecha.mes)
        a = str(self.fecha.anio)
        parte_digitos = d + m + a
        return parte_digitos


