def run():
    # for contador in range(1000):
    #     if contador % 2 != 0: #Si a contador lo divido en 2 y su resto es diferente de cero
    #         continue #se salta y no ejecuta lo que esta debajo de continue y se pasa a la siguiente vuelta en el ciclo.
    #     print(contador)
        
    # for i in range(2000):
    #     print(i)
    #     if i == 678: #Si i toma ese valor, se termina la ejecución del ciclo
    #         break

#Ejemplo recorriendo un string
    texto = input("Escribe una frase: ")
    for letra in texto:
        #print(letra) SI lo dejo asi, imprime la primera O que encuentra
        if letra == "o": #Si en el texto se encuentra una "o", se termina la ejecución del ciclo
            break
        print(letra) # SI dejo el print aqui imprime hasta la letra antes de la "o"

if __name__ == "__main__":
    run()