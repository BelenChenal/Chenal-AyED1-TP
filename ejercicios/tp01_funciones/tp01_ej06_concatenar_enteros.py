#Desarrollar una función que reciba como parámetros dos números enteros positivos
#y devuelva como valor de retorno el número que resulte de concatenar ambos
#parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per-
#mite utilizar facilidades de Python no vistas en clase

def concatenar (a:int, b:int) ->int: 
    contador = 0
    aux= b
    while aux != 0:
        aux //= 10
        contador += 1
    unir= a *(10**contador) + b 


num1= (input('Ingrese primer numero '))
num2= (input('Ingrese segundo numero '))
print(concatenar(num1,num2))