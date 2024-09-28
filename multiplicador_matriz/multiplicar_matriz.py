matriz_ejemplo_a = [[1, 2, 3, 4, 5], [4, 3, 2, 1, 0]]
matriz_ejemplo_b = [[2, 2], [3, 3], [4, 4], [5, 5], [0, 0]]


# Con esta debería fallar la validación.
matriz_ejemplo_c = [[0, 3, 8], [2, 2, 23]]

# Función auxiliar 1
def validar_multiplicacion_de_matrices(matriz_a: list[list], matriz_b: list[list]):
    # Número de columnas de A
    columnas_a = len(matriz_a[0])
    # Número de filas de B
    filas_b = len(matriz_b)
    
    return columnas_a == filas_b



def multiplicador_de_matrices(matriz_a: list[list], matriz_b: list[list]) -> list[list]:
    """_summary_ Función que permite multiplicar dos matrices

    Args:
        matriz_a (list[list]): _description_ primer matriz a multiplicar
        matriz_b (list[list]): _description_ segunda matriz a multiplicar

    Returns:
        list[list]: _description_
    """

    es_posible_multiplicar = validar_multiplicacion_de_matrices(matriz_a, matriz_b)

    if not es_posible_multiplicar:
        print("No es posible hacer el producto de las matrices ya que no se cumple la relación entre filas y columnas.")
        return

    cantidad_filas_a = len(matriz_a)
    cantidad_filas_b = len(matriz_b)
    cantidad_col_a = len(matriz_a[0])
    cantidad_col_b = len(matriz_b[0])
    
    # Matrix vacia que voy a usar para el resultado
    matriz_resultante = []

    # Itero cada fila de A
    for i in range(cantidad_filas_a):
        # creo una nueva fila para la matriz
        fila = []
        
        # Itero cada columna en B
        for j in range(cantidad_col_b):
            # Por cada columna de B guardo un 0 en la fila
            fila.append(0)
        
        # uso append para agregar a la matriz la fila
        matriz_resultante.append(fila)

    # Mostrar la matriz resultante
    #print("Matriz armada: " + str(matriz_resultante))

    # 1 Itero las fials de A y multiplico por las columnas de B
    for idx_filas_a in range(cantidad_filas_a):
        for idx_col_b in range(cantidad_col_b):
            
            # Itero col de A para sacar cada valor de la matriz (es el largo máximo a iterar, también podría iterar filas de B)
            for idx_col_a in range(cantidad_col_a):
                matriz_resultante[idx_filas_a][idx_col_b] += matriz_a[idx_filas_a][idx_col_a] * matriz_b[idx_col_a][idx_col_b]
    
    return matriz_resultante


matriz_resultante_final = multiplicador_de_matrices(matriz_ejemplo_a, matriz_ejemplo_b)

print(matriz_resultante_final)
