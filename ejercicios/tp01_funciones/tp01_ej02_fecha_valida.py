def validacion_fecha(dia:int,mes:int,anio:int)-> bool:
    """Recibe un dia, mes y año, valida si los numeros ingresados son correctos y positivos

            Pre: dia, mes y anio deben ser numeros enteros y positivos
            
            Post: devuelve True si la fecha es valida (se consideraron los meses con 30 y 31 dias,año bisiesto
            y rango del año )
                  devuelve False si anio y mes/dia en caso contrario  """
    anio_valido = False
    bisiesto= False
    mes_dia = False
# 1- validar si anio es bisiesto o no 
    if anio >= 1 and anio <= 2026:
        anio_valido = True
        if (anio % 4 == 0 and anio % 100 !=0 )or (anio % 400 == 0): 
            bisiesto = True
                #es bisiesto
        else: 
            bisiesto = False   
        # 2- si no es bisiesto, validar los meses
    if mes > 0 and mes < 13:
        if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia > 0 and dia < 31) :
                 mes_dia= True
            #mes y dia correcto
        if (mes == 1 or mes ==3 or mes ==5 or mes == 7 or mes ==8 or mes ==10 or mes ==12) and (dia > 0 and dia <= 31):
                mes_dia= True
            #mes y dia correcto
        if mes == 2 and bisiesto == True: # 3- si es bisiesto, validar los dias
                if dia > 0 and dia <= 29:
                    mes_dia= True
        elif mes == 2 and bisiesto == False:
             if dia > 0 and dia <=28:
                  mes_dia = True

    if mes_dia == True and anio_valido == True:
        return True 
    else: 
        return False             
    

dia = int(input('Ingrese un dia'))
mes= int(input('Ingrese el mes'))
anio = int(input('Ingrese el año'))

validar = validacion_fecha(dia,mes,anio)

if validar == True:
     print('La fecha es valida')
else: 
     print('La fecha es invalida')

        


