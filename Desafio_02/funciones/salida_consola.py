def mostrar_menu():
    menu = """"
    Menú:
    01) Mostrar los nombres de los héroes
    02) Mostrar la identidad de los héroes
    03) Mostrar al heroe con mayor altura
    04) Mostrar al/los heroe/s con mayor poder,\nen caso de haber mas de uno, mostrarlos a todos
    05) Filtrar a los heroes Femeninos y mostrar sus nombres
    06) Filtrar a los heroes Masculinos y mostrar sus identidades
    07) Filtrar a los personajes No-Binarios y mostrar su nombre e identidad
    08) Determinar cuales heroes tienen un poder superior al promedio.
    09) Determinar cual es el maximo de poder y\nmostrar los nombres de cuales heroes tienen un poder inferior\nA LA MITAD DE PODER del heroe mas fuerte.
    10) Mostrar los héroes por poder ascendente
    11) Mostras los héroes por altura descendente
    12) Ordernar los héroes por poder DES o ASC
    13) Salir
    """

    print(menu)

if __name__ == '__main__':
    mostrar_menu()