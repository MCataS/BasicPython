def run():
    mi_diccionario = {
        'llave1' : 1,
        #key: value
        'llave2' : 2,
        'llave3' : 3
    }
    # print(mi_diccionario['llave1'])#Entre las llaves no se ponen índices como en las listas, se pone la llave
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina' : 44,
        'Brasil' : 240,
        'Colombia' : 350
    }

    #print(poblacion_paises['Colombia'])#Imprime el número de población

    #Imprime todas las llaves
    # for pais in poblacion_paises.keys():
    #     print(pais)

    #Imprime todas los valores asignados a las llaves
    # for pais in poblacion_paises.values():
    #     print(pais)    

    #Imprimir llave y valor
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion)) 

if __name__ == '__main__':
    run()