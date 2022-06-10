i= 0 #Iniciar en cero para realizar el conteo apropiado 
suma = 0
while i < 100: #Mientras i sea menor de 100 ejecute lo siguente
    i = i + 2 #i es igual a su valor más dos, también se puede poner i += 2
    suma = suma + i
    print(i) #Imprima i
print("El resultado de la suma de los números pares del 0 a 100 es:",suma)
    #Al regresar al while, i vale 2, como es menor que 100, entra, le suma otros dos (queda valiendo cuatro) y lo imprime y asi sucesivamente.