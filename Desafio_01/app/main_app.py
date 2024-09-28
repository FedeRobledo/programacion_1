from validaciones import validar_opcion
from funciones import mostrar_menu, limpiar_pantalla, play_sound, utn_filtrar_heroes_genero, utn_mostrar_heroe_mayor_altura, utn_mostrar_heroes_mas_fuertes,\
    utn_mostrar_identidades_heroes, utn_mostrar_nombres_heroes, utn_mostrar_heroes_poder_superior_promedio, utn_mostrar_heroes_mas_debiles, mostrar_heroes_por_poder_asc,\
    mostrar_heroes_por_poder_des, mostrar_heroes_por_poder_segun_usuario

def utn_heroes_app(lis_nombres: list, lis_iden: list, lis_gen: list, lis_pod: list, lis_alt: list):
    
    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 12)
        play_sound()

        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lis_nombres)
                pass
            case 2:
                utn_mostrar_identidades_heroes(lis_iden)
                pass
            case 3:
                utn_mostrar_heroe_mayor_altura(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt)
                pass
            case 4:
                utn_mostrar_heroes_mas_fuertes(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt)
                pass
            case 5:
                utn_filtrar_heroes_genero(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt, 'Femenino')
                pass
            case 6:
                utn_filtrar_heroes_genero(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt, 'Masculino')
                pass
            case 7:
                utn_filtrar_heroes_genero(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt, 'No-Binario')
                pass
            case 8:
                utn_mostrar_heroes_poder_superior_promedio(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt)
                pass
            case 9:
                utn_mostrar_heroes_mas_debiles(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt)
                pass
            case 10:
                mostrar_heroes_por_poder_asc(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt)
                break
            case 11:
                mostrar_heroes_por_poder_des(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt)
                break
            case 12:
                mostrar_heroes_por_poder_segun_usuario(lis_nombres, lis_iden, lis_gen, lis_pod, lis_alt)
                break
            case _:
                continue

        limpiar_pantalla()