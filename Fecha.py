class Fecha:
    dia=""
    mes=""
    anio=""

    #recibe la cadena de la fecha
    def __init__(self,fecha):
        #asignamos los valores
        day=fecha[0:2]
        month=fecha[3:5]
        year=fecha[6:10]
        if len(fecha)>9:
            if fecha[2]=="/" and fecha[5]=="/":
                if day >="01" and day<="31":
                
                    if month >="01" and month<="12":
                        
                        if year >="1955" and year<="2022":
                            self.dia=day
                            self.mes=month
                            self.anio=year
                        else:
                            print('INGRESA UNA ANIO DENTRO DEL RANGO!!')
                    else:
                        print('INGRESA UN MES EXISTENTE DENTRO DEL RANGO!!')
                else:
                    print('INGRESA UN DIA DENTRO DEL RANGO!! ')
            else:
                print('FALTA EL "/"!!')
        else:
            print("LA FECHA NO ESTA EN EL FORMATO INDICADO dd/mm/aaaa")

        