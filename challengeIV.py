inmuebles_validados = []

def check_inmueble(año, metros, habitaciones, garaje, zona, estado):
    if zona in ['A', 'B', 'C'] and estado in ['Disponible', 'Reservado', 'Vendido']:
        if año > 1999 and metros >= 60  and habitaciones >= 2:
            nuevo_inmueble = {'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garaje, 'zona':                                 zona, 'estado': estado}
            inmuebles_validados.append(nuevo_inmueble)
            print('El inmueble cumple con los requisitos y ha sido agregado a la lista exitosamente')
        else:
            print('El inmueble no cumple con los requisitos')
    else:
        print('Zona no deseada o Estado inválido')

def editor(indice, año, metros, habitaciones, garaje, zona, estado):
    while indice >= 0 and indice < len(inmuebles_validados):
        if zona in ['A', 'B', 'C'] and estado in ['Disponible', 'Reservado', 'Vendido']:
            if año > 1999 and metros >= 60 and habitaciones >= 2:
                inmuebles_validados[indice]['año'] = año
                inmuebles_validados[indice]['metros'] = metros
                inmuebles_validados[indice]['habitaciones'] = habitaciones
                inmuebles_validados[indice]['garaje'] = garaje
                inmuebles_validados[indice]['zona'] = zona
                inmuebles_validados[indice]['estado'] = estado
                print('El inmueble ha sido modificado exitosamente')
                break
            else:
                print('El inmueble no cumple con los requisitos')
        else:
            print('Zona no deseada o Estado inválido')

def remover_inmueble(indice):
    if indice >= 0 and indice < len(inmuebles_validados):
        inmueble_eliminado = inmuebles_validados.pop(indice)
        print(f'El inmueble {inmueble_eliminado} ha sido eliminado exitosamente')
    else:
        print('El inmueble a eliminar no existe en la lista')

def renovar_estado(indice, cambio_estado):
    if indice >= 0 and indice < len(inmuebles_validados):
        if cambio_estado in ['Disponible', 'Reservado', 'Vendido']:
            inmuebles_validados[indice]['estado'] = cambio_estado
            print('El estado a sido actualizado exitosamente')
        else:
            print('El estado que quieres poner no está permitido. Recuerda que los estados válidos son: Disponible,                 Reservado o Vendido.')
    else:
        print('No se encuentra estado a modificar según el índice dado')

def precio_inmueble(presupuesto):
    resultados = []
    for inmueble in range(len(inmuebles_validados)):
        consulta = inmuebles_validados[inmueble]
