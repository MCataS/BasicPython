import random


def generate_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/' , '!']

    characters = mayusculas + minusculas + simbolos + numeros

    password = [] #Creo una lista vacia donde se van a poner caracteres aleatorios

    for i in range(15):#Queremos una contraseña de 15 caracteres
        character_random = random.choice(characters) #Con choice se elije un caracter al azar de la lista que le pasamos characters
        password.append(character_random)#Agrega el caracter seleccionado
    
    password = "".join(password) # Para convertir una lista en estring, deben ser comillas dobles
    return password


def run():
    password = generate_password()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()

