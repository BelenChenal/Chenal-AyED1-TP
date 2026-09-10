#Desarrollar una función que reciba como parámetros dos números enteros positivos
#y devuelva como valor de retorno el número que resulte de concatenar ambos
#parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per-
#mite utilizar facilidades de Python no vistas en clase

def concatenar (a:str, b:str) ->str: 
    lista= [a,b]
    unir = "".join(lista)

    return unir


num1= (input('Ingrese primer numero'))
num2= (input('Ingrese segundo numero'))
print(concatenar(num1,num2))