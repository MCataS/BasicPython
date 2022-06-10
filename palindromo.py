def palindromo(palabra):
    palabra = palabra.replace(" ","")#5. Elimina los espacios
    palabra = palabra.lower()#6. Pasa los carácteres a minúscula
    palabra_invertida = palabra[::-1]#7. Invierte la frase ingresada y la almacena en palabra_invertida
    if palabra ==palabra_invertida:#8. Compara la frase inicial y la invertida sin espacios
        return True#9. La función retorna un boleano
    else:
        return False#9. La función retorna un boleano


def run():
    palabra = input("Escribe una palabra o frase: ")#3. Solicita el ingreso de la palabra o frase
    es_palindromo = palindromo(palabra)#4. Invoca la función palidromo para validar, dando como parámetro la palabra o frase
    if es_palindromo == True: #10. Con el retorno de la función palindromo valida
        print("Es palindromo")#11. Imprime
    else:
        print("No es palindromo")#11. Imprime


if __name__ == "__main__":#1. Al ingresar, el código inicia la ejecución desde aqui
    run()#2. Invoca a la función run