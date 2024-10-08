from .auxiliares import obtener_maximo, promedio, obtener_mitad_de_maximo, \
    ordenar_matriz, obtener_idx_de_mayor_poder

def mostrar_nombres_heroes(lis_nom: list):
    for n in lis_nom:
        print(n)


def mostrar_identidades_heroes(lis_iden: list):
    for identidad in lis_iden:
        if identidad != "":
            print(identidad)
        else:
            print("No Tiene identidad secreta")


def mostrar_heroe_mayor_altura(matriz_heroes: list[list]):
    altura = obtener_maximo(matriz_heroes[5])
    i = matriz_heroes[5].index(altura)

    print(f"El Heroe mas alto es {f"Nombre: {matriz_heroes[0][i][0:20]}"} midiendo {matriz_heroes[5][i]} mts de altura.")


def mostrar_heroes_mas_fuertes(matriz_heroes: list[list]) -> None:
    lista_indices = obtener_idx_de_mayor_poder(matriz_heroes[4])

    print(lista_indices)

    print(f"El/los Heroes mas fuertes son:\n")
    for indice in lista_indices:
        print(f"{matriz_heroes[0][indice]}, con un total de {matriz_heroes[4][indice]} de poder\n")


def mostrar_heroes_genero_femenino(matriz_heroes: list[list]) -> None:
    for indice in range(len(matriz_heroes[3])):
        if matriz_heroes[3][indice] == "Femenino":
            print(f"Nombre: {matriz_heroes[0][indice]}\nIdentidad: {matriz_heroes[1][indice]}\nGénero: {
                  matriz_heroes[3][indice]}\nPoder: {matriz_heroes[4][indice]}\nAltura: {matriz_heroes[5][indice]}\n\n")


# def utn_mostrar_heroes_poder_superior_promedio(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
#     poder = promedio(lis_pod)

#     for i in range(len(lis_pod)):
#         if lis_pod[i] > poder:
#             print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {
#                   lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")


# def utn_mostrar_heroes_mas_debiles(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
#     poder = obtener_mitad_de_maximo(lis_pod)

#     for i in range(len(lis_pod)):
#         if lis_pod[i] <= poder:
#             print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {
#                   lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")


# def mostrar_heroes_por_poder_asc(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt) -> None:

#     matriz_ordenada = ordenar_matriz([lis_nombres, lis_pod , lis_iden, lis_gen, lis_alt], "ASC")

#     # por cada fila voy a mostrar un mensaje
#     for fila in range(len(matriz_ordenada[0])):
#         mensaje = "\n"
#         # por cada columnda saco el valor correspondiente y lo concateno
#         for col in matriz_ordenada:
#             mensaje += str(col[fila]) + " | "
#         print(mensaje) #TODO: Formatear bien el mensaje

# def mostrar_heroes_por_poder_des(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt) -> None:

#     matriz_ordenada = ordenar_matriz([lis_nombres ,lis_pod, lis_iden, lis_gen, lis_alt], "DES")

#     # por cada fila voy a mostrar un mensaje
#     for fila in range(len(matriz_ordenada[0])):
#         mensaje = "\n"
#         # por cada columnda saco el valor correspondiente y lo concateno
#         for col in matriz_ordenada:
#             mensaje += str(col[fila]) + " | "
#         print(mensaje) #TODO: Formatear bien el mensaje

# def mostrar_heroes_por_poder_segun_usuario(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt):

#     modo = ""
    
#     while True:
#         modo = input("Por favor indique si quiere ordenar los heros de forma ascendente (ASC) o descendente (DES): ")
#         if modo == "ASC" or modo == "DES":
#             break

    
#     matriz_ordenada = ordenar_matriz([lis_nombres, lis_pod , lis_iden, lis_gen, lis_alt], modo)

#     # por cada fila voy a mostrar un mensaje
#     for fila in range(len(matriz_ordenada[0])):
#         mensaje = "\n"
#         # por cada columnda saco el valor correspondiente y lo concateno
#         for col in matriz_ordenada:
#             mensaje += str(col[fila]) + " | "
#         print(mensaje) #TODO: Formatear bien el mensaje

if __name__ == '__main__':
    utn_mostrar_nombres_heroes(
        ['Ironman', 'Batman', 'Wolverine', 'Flash', 'Spiderman', 'Remy LeBeau'])
    utn_mostrar_identidades_heroes(
        ['Tony Stark', 'Bruce Wayne', 'James Howlett', 'Barry Allen', 'Miles Morales', 'Gambito'])
