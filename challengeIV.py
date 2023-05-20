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

check_inmueble(2001, 64, 3, 'Si', 'A', 'Disponible')
print(inmuebles_validados)


def editor(indice, año, metros, habitaciones, garaje, zona, estado):
    while indice >= 0 and indice < len(inmuebles_validados):
        if zona in ['A', 'B', 'C'] and estado in ['Disponible', 'Reservado', 'Vendido']:
            if año > 1999 and metros >= 60 and habitaciones >= 2:
                inmuebles_validados[indice]['año'] = año
                inmuebles_validados[indice]['metros'] = metros
                inmuebles_validados[indice]['habitaciones'] = habitaciones
                inmuebles_validados[indice]['garaje'] = garaje
                inmuebles_validados[indice]['zona'] = zona
                inmuebles_validados[indice]['estado'] = Estado
                print('El inmueble ha sido modificado exitosamente')
            else:
                print('El inmueble no cumple con los requisitos')
        else:
            print('Zona no deseada o Estado inválido')



editor(0, 2010, 64, 3, 'Si', 'A', 'Disponible')
print(inmuebles_validados)




