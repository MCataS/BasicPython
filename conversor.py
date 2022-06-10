# pesos = input("Ingrese el valor en pesos CO: ")
# pesos = float(pesos)
# valor_dolar = 3761.77
# dolares = pesos / valor_dolar #Si se requiere de dólares a pesos, la operación es una multiplicación.
# #Redondear un flotante... (variable, número de decimales luego del punto)
# dolares = round(dolares, 2)
# print("Cuentas con ", dolares, "dólares")
# #Otra manera de imprimir
# dolares = str(dolares)
# print("Tiene $" + dolares + " dólares")

def operacion (valor_dolar):
    pesos = float(input("Ingrese el valor en pesos:"))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print("Cuentas con ", dolares, "dolares")

menu = """
Conversor de Monedas 💲
Seleccione una opción, (digite el número)
1. Pesos Argentinos
2. Pesos Colombianos
3. Pesos Mexicanos
"""

moneda = int(input(menu))

if moneda == 1:
    operacion(11.21)
    
elif moneda == 2:
    operacion(3743.34)

elif moneda == 3:
    operacion(3779.87)

else:
    print("Ingrese un valor numérico 1, 2 o 3")


