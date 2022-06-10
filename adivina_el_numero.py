import random #Modulo para trabajar con aletoriedad


def run():
    num_aleatorio = random.randint(1, 100)#Accede a la funición randit, que selecciona un número aleatorio entre en rango definido
    num_elegido = int(input("Digita un número de 1 al 100: "))#Se solicita un número
    while num_elegido != num_aleatorio:
        if num_elegido > num_aleatorio:
            print("Digita un número menor")
        else:
            print("Digita un número mayor")
        num_elegido = int(input("Digita otro número: "))#Se solicita un número de nuevo, porque de lo contrario queda validando el número ingresado inicialmente enun ciclo infinito
    print("¡Ganaste!")


if __name__ == '__main__':
    run()