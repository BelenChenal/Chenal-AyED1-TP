def buscar_mayor(a,b,c):
    """Recibe tres numeros , devuelve el mayor de ellos
        
        Pre: Los tres numeros deben ser enteros y positivos

        Post: devuelve el numero mayor entre los tres
            Si los tres son iguales, devuelve -1
    """
    if a > b:
        if a > c:
            return a
        else: 
            return c
    elif b > c:
            return b
    elif c > b:
            return c
    else:
        return -1


num1 =int(input('Ingrese primer numero'))
num2 =int(input('Ingrese segundo numero'))
num3 = int(input('Ingrese tercer numero'))
buscar= buscar_mayor(num1,num2,num3)
if buscar == -1:
     print('No hay mayor')
else: 
    print(f'El mayor es el {buscar}')
