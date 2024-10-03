from validaciones import validar_opcion
from funciones import mostrar_menu, limpiar_pantalla, mostrar_nombres_heroes, mostrar_identidades_heroes, mostrar_heroe_mayor_altura, mostrar_heroes_mas_fuertes, mostrar_heroes_genero_femenino


def utn_heroes_app(matriz_heroes):
    
    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 13)

        match opcion:
            case 1:
                mostrar_nombres_heroes(matriz_heroes[0])
                pass
            case 2:
                mostrar_identidades_heroes(matriz_heroes[1])
                pass
            case 3:
                mostrar_heroe_mayor_altura(matriz_heroes)
                pass
            case 4:
                mostrar_heroes_mas_fuertes(matriz_heroes)
                pass
            case 5:
                mostrar_heroes_genero_femenino(matriz_heroes)
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                break
            case 11:
                break
            case 12:
                break
            case 13:
                break
            case _:
                continue

        limpiar_pantalla()