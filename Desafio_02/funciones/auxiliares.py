def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def mostrar_nombre(lis_nom: list, i: int) -> str:
    return lis_nom[i]

def obtener_idx_de_mayor_poder(lis_num: list) -> float:
    numero = None
    indices_de_mayor_poder = []

    for indice in range(len(lis_num)):
        num = lis_num[indice]
        print("Poder: " + str(lis_num[indice]))

        if not numero or numero < num:
            numero = num
            indices_de_mayor_poder = []
            print("Reseteo la lista " + str(numero))
            print(indices_de_mayor_poder)
            indices_de_mayor_poder.append(indice)
        elif numero == num:
            indices_de_mayor_poder.append(indice)

    return indices_de_mayor_poder

def obtener_maximo(lis_num: list) -> float:
    numero = None

    for num in lis_num:
        if not numero or numero < num:
            numero = num
    
    return float(numero)

def promedio(lis_num: list) -> float:
    sum = 0

    for n in lis_num:
        sum += n

    return sum/len(lis_num)

def obtener_mitad_de_maximo(lis_num: list) -> float:
    maximo = obtener_maximo(lis_num)

    return maximo/2

def ordenar_matriz(matriz: list[list], modo: str) -> list[list]:
    # Uso el último valor de la primera columna de la matriz como pivote
    pivot = matriz[1][-1]

    # Tengo que inicializar la matriz con su largo total sino explota al querer operar la lista
    mas_chicos = [[] for _ in range(len(matriz))]
    mas_grandes = [[] for _ in range(len(matriz))]

    # Itero la columna de poder de la matriz, si es mas alto o mas bajo
    # del pivot lo guardo donde corresponda y también hago un for para que
    # guarde cada columna

    for i in range(len(matriz[1]) - 1):  # No incluir el último (que es el pivote)
        if (modo == 'ASC' and matriz[1][i] <= pivot) or (modo == 'DES' and matriz[1][i] > pivot):
            for col in range(len(matriz)):
                mas_chicos[col].append(matriz[col][i])
        else:
            for col in range(len(matriz)):
                mas_grandes[col].append(matriz[col][i])

    # Llamo a la funcion de nuevo si hay poderes mas chicos.
    if mas_chicos[0]:
        sorted_menores = ordenar_matriz(mas_chicos, modo)
    else:
        sorted_menores = mas_chicos

    # Llamo a la funcion de nuevo si hay poderes mas grandes.
    if mas_grandes[0]:
        sorted_mayores = ordenar_matriz(mas_grandes, modo)
    else:
        sorted_mayores = mas_grandes

    # Concateno los resultados y devuelvo una matriz modificada
    resultado = [[] for _ in range(len(matriz))]
    for col in range(len(matriz)):
        resultado[col] = sorted_menores[col] + [matriz[col][-1]] + sorted_mayores[col]

    return resultado
