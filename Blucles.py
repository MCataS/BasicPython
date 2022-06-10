def run(): #Siempre se debe definir una función principal
    LIMITE = 1000 #Una variable en mayúscula, no es variable, es una constante

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a", contador, "es igual a: ", potencia_2)
        #También puede imprimirse print("2 elevado a" + str(contador() + "es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__": #Punto de entrada
    run()
