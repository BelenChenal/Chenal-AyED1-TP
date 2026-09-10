 
#verifica es oblongo,
oblongo=lambda x: ((((1+(4*x))**0.5)-1)/2)%1 == 0 
#verifica si es triangular , es la misma estructura que el oblongo,
#porque un numero es trangular si su doble 2 * x es un numero oblongo
#para que me tome la raiz cuadrada completamente y python entienda mis(), se aplica el 8 * x (4*2=8)
triangular = lambda x: (((((1+8*x)**0.5)-1)/2))%1 == 0  
print(oblongo(6))
print(triangular(10))