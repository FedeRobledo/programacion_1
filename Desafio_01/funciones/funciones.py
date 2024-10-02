from .auxiliares import obtener_maximo, promedio, obtener_mitad_de_maximo, \
    ordenar_matriz


def utn_mostrar_nombres_heroes(lis_nom: list):
    for n in lis_nom:
        print(n)


def utn_mostrar_identidades_heroes(lis_iden: list):
    for e in lis_iden:
        print(e)


def utn_mostrar_heroe_mayor_altura(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    altura = obtener_maximo(lis_alt)
    i = lis_alt.index(altura)

    print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {
          lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}")


def utn_mostrar_heroes_mas_fuertes(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    poder = obtener_maximo(lis_pod)

    for i in range(len(lis_pod)):
        if float(lis_pod[i]) == poder:
            print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {
                  lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")


def utn_filtrar_heroes_genero(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list, gen: str):
    for i in range(len(lis_gen)):
        if lis_gen[i] == gen:
            print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {
                  lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")


def utn_mostrar_heroes_poder_superior_promedio(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    poder = promedio(lis_pod)

    for i in range(len(lis_pod)):
        if lis_pod[i] > poder:
            print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {
                  lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")


def utn_mostrar_heroes_mas_debiles(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    poder = obtener_mitad_de_maximo(lis_pod)

    for i in range(len(lis_pod)):
        if lis_pod[i] <= poder:
            print(f"Nombre: {lis_nombres[i]}\nIdentidad: {lis_iden[i]}\nGénero: {
                  lis_gen[i]}\nPoder: {lis_pod[i]}\nAltura: {lis_alt[i]}\n\n")


def mostrar_heroes_por_poder_asc(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt) -> None:

    matriz_ordenada = ordenar_matriz([lis_nombres, lis_pod , lis_iden, lis_gen, lis_alt], "ASC")

    # por cada fila voy a mostrar un mensaje
    for fila in range(len(matriz_ordenada[0])):
        mensaje = "\n"
        # por cada columnda saco el valor correspondiente y lo concateno
        for col in matriz_ordenada:
            mensaje += str(col[fila]) + " | "
        print(mensaje) #TODO: Formatear bien el mensaje


def mostrar_heroes_por_poder_des(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt) -> None:

    matriz_ordenada = ordenar_matriz([lis_nombres ,lis_pod, lis_iden, lis_gen, lis_alt], "DES")

    # por cada fila voy a mostrar un mensaje
    for fila in range(len(matriz_ordenada[0])):
        mensaje = "\n"
        # por cada columnda saco el valor correspondiente y lo concateno
        for col in matriz_ordenada:
            mensaje += str(col[fila]) + " | "
        print(mensaje) #TODO: Formatear bien el mensaje


def mostrar_heroes_por_poder_segun_usuario(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt):

    modo = ""
    
    while True:
        modo = input("Por favor indique si quiere ordenar los heros de forma ascendente (ASC) o descendente (DES): ")
        if modo == "ASC" or modo == "DES":
            break

    
    matriz_ordenada = ordenar_matriz([lis_nombres, lis_pod , lis_iden, lis_gen, lis_alt], modo)

    # por cada fila voy a mostrar un mensaje
    for fila in range(len(matriz_ordenada[0])):
        mensaje = "\n"
        # por cada columnda saco el valor correspondiente y lo concateno
        for col in matriz_ordenada:
            mensaje += str(col[fila]) + " | "
        print(mensaje) #TODO: Formatear bien el mensaje


if __name__ == '__main__':
    utn_mostrar_nombres_heroes(
        ['Ironman', 'Batman', 'Wolverine', 'Flash', 'Spiderman', 'Remy LeBeau'])
    utn_mostrar_identidades_heroes(
        ['Tony Stark', 'Bruce Wayne', 'James Howlett', 'Barry Allen', 'Miles Morales', 'Gambito'])
