


class Fecha:
    dia= ""
    mes=""
    anio=""
    

    def __init__(self,cadena):
        d= int(cadena[0:2])
        if d>0 and d<=31:
            if cadena[2] == "/" and cadena[5] == "/":
                m=int(cadena[3:5])
                if m>0 and m<=12:
                    a = int(cadena[6:10])
                    if a>1900 and a<2023:

                        self.dia = d
                        self.mes = m
                        self.anio = a
                        
                    else:
                        print("El anio esta fuera de rango")
                else:
                    print("Mes fuera de rango")
            else: 
              print("Falto una diagonal")
        else:
            print("Dia fuera de rango") 

    

#if __name__=='__main__':
    #date= input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
    #f= Fecha(date)
        
    #print("Fin")


        