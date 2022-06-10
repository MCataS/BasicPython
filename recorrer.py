def run():
    # nombre = input("Escribe tu nombre: ")
    # for letra in nombre:#Para cada letra en nombre
    #     print(letra)#Imprime cada letra
    frase = input("Escribe una frase: ")
    for caracter in frase:#caracter o letra, puede tener cualquier nombre
        print(caracter.upper())

if __name__ == "__main__":
    run()