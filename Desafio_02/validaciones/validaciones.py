def validar_opcion (min: int, max: int):
    opcion = input(f"Seleccione una opción [{min} - {max}]:")

    if not opcion or not opcion.isdigit() or not (min <= int(opcion) <= max):
        return validar_opcion(min, max)
    
    return int(opcion)

if __name__ == '__main__':
    print(validar_opcion(1, 13))