inmuebles_validados = []

def inmueble_check(año, metros, habitaciones, garaje, zona, estado):
    if zona in ['A', 'B', 'C'] and estado in ['Disponible', 'Reservado', 'Vendido']:
        if año > 1999 and metros >= 60  and habitaciones >= 2:
            nuevo_inmueble = {'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garaje, 'zona':                                 zona, 'estado': estado}
            inmuebles_validados.append(nuevo_inmueble)
            print(inmuebles_validados)
        else:
            print('El inmueble no cumple con los requisitos por lo que no va a ser tenido en cuenta, Gracias')
