inmueble_a_verificar = input('Ingrese datos del inmueble respetando el siguiente formato {"año": año_del_inmueble, "metros": metros_cuadrados, "habitaciones": cantidad_de_habitaciones, "garaje": si_no, "zona": A_B_C, "estado": Disponible_Reservado_Vendido}')

inmuebles_validados = []

def inmueble_check(año, metros, habitaciones, garaje, zona, estado):
    if zona in ['A', 'B', 'C'] and estado in ['Disponible', 'Reservado', 'Vendido']:
        if año > 1999 and metros >= 60  and habitaciones >= 2:
            nuevo_inmueble = {}
