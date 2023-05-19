inmuebles_validados = []

def inmueble_check(año, metros, habitaciones, garaje, zona, estado):
    if zona in ['A', 'B', 'C'] and estado in ['Disponible', 'Reservado', 'Vendido']:
        if año > 1999 and metros >= 60  and habitaciones > 1:
            nuevo_inmueble = {}
