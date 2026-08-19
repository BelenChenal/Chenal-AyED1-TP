def buscar_mayor(a,b,c):
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
print(f'El mayor es el {buscar}')
