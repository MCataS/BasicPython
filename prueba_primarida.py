def es_primo(numero): #3. ingresa a la función
    if numero == 1:#El número uno no es primo
        return False
    else:
        contador=0 #4. Inicia el contador en cero

        for i in range(1, numero+1):#5. Para la iteración en en rango de uno al número ingresado (Se establece más uno porque el rango toma uno menos del límite establecido)
            if i == 1 or i==numero:#6. Si la iteración es igual a uno o al mismo número
                continue#7. Continua, pues su residuo siempre será igual a cero
            if numero%i == 0:#8. Si numero dividido en la iteración tiene como residuo cero
                contador +=1#9. Suma uno al contador
        if contador == 0:#10. si el contador es igual a cero
            return True#Retorne verdadero
        else:#sino
            return False#Retorne falso


def run():
    numero = int(input("Escribe un número: ")) #1. Solicita el número a validar
    if es_primo(numero): #2. Recibe lo que retorna la función es_primo y valida #11. si la función retorna verdadero (lo establece por defecto)
        print("Es primo") #12.Imprime es primo
    else:#13. Sino
        print("No es primo")#Imprime no es primo


if __name__ == "__main__":
    run()