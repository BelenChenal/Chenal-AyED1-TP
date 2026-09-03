def vuelto_billete(importe: int, dinero:int) ->None:
    """ Calcula el cambio y muestra los billetes a devolver

        Pre: los numeros son enteros positivos
        Post: muestra por pantalla la cantidad de billetes a devolver 
             si no, muestra un error por falta de denominaciones
    """
    cantidad = 0
    vuelto = 0
    billetes = [5000,1000,500,200,100,50,10]
    if dinero < importe:
        print('Dinero insuficiente')
    else: 
        vuelto= dinero - importe
        if vuelto % 10 !=0:
            print('Error, falta de billetes con denominaciones adecuadas')
        else: 
            for i in billetes:
                cantidad = vuelto // i
                vuelto %= i 
                if cantidad > 0:
                    print(f'{cantidad} billetes de ${i}')
