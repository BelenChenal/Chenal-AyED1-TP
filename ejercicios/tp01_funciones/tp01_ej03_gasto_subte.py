def calculo_descuento (base,cantidad,descuento):
    resultado = (base * cantidad) * descuento

    return resultado

def calculo_gasto_subte(cant_viajes):
    cantidad = cant_viajes 
    base_boleto = 1500
    descuento1= 0.80
    descuento2= 0.70
    descuento3= 0.60
    total= 0 
    if cant_viajes >= 1 and cant_viajes <= 20: # no tiene descuento, paga el total
        total= base_boleto * cant_viajes
    elif cant_viajes >= 21 and cant_viajes <=30: # 20% de descuento entre 21 y 30
        total= calculo_descuento(base_boleto,cantidad,descuento1)
    elif cant_viajes >= 31 and cant_viajes <= 40:# 30% de descuento entre 31 y 40
        total= calculo_descuento(base_boleto,cantidad,descuento2)
    elif cant_viajes > 40: # 40% de descuento, mas del 40
        total= calculo_descuento(base_boleto,cantidad,descuento3)

    return total 





viajes= int(input('Ingrese la cantidad de viajes realizados en el mes '))
total_mes = calculo_gasto_subte(viajes)

if total_mes == 0 :
    print('No hubo viajes para calcular')
else: 
    print(f'El gasto realizado de este mes fue de {total_mes: .2f} por {viajes} viajes')