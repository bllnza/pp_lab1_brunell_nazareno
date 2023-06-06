import re
import quicksort
import json

with open("pp_lab1_brunell_nazareno\dt.json") as file:
    data = json.load(file)

jugadores = data['jugadores']

def mostrar_jugadores(jugadores: list):
    """
    Muestra por consola una lista de todos los jugadores del Dream Team, mostrando su nombre y posición.

    Recibe como parámetro 'jugadores', que es una lista de diccionarios.
    """

    for jugador in jugadores:
        formato = '{0} - {1}'.format(
            jugador['nombre'],
            jugador['posicion']
        )
        print(formato)






def mostrar_estadisticas_por_indice_ingresado(jugadores: list, indice_jugador: int) -> str:
    """
    Recibe un número de índice ingresado para mostrar las estadísticas del jugador
    
    Recibe como parámetro 'jugadores', que es una lista de diccionarios
    Devuelve un string que muestra las estadísticas y el nombre del jugador seleccionado
    """

    
    if (0 <= indice_jugador) and (indice_jugador < len(jugadores)):
            jugador = jugadores[indice_jugador]
            estadisticas = jugador['estadisticas']
            jugador_seleccionado = ("{0}\n"
                                        "Temporadas jugadas: {1}\n"
                                        "Puntos totales: {2}\n"
                                        "Promedio de puntos por partido: {3}\n"
                                        "Rebotes totales: {4}\n"
                                        "Promedio de rebotes por partido: {5}\n"
                                        "Asistencias totales: {6}\n"
                                        "Promedio de asistencias por partido: {7}\n"
                                        "Robos totales: {8}\n"
                                        "Bloqueos totales: {9}\n"
                                        "Porcentaje de tiros de campo: {10}\n"
                                        "Porcentaje de tiros libres: {11}\n"
                                        "Porcentaje de tiros triples: {12}".format(
                                            jugador['nombre'],
                                            estadisticas['temporadas'],
                                            estadisticas['puntos_totales'],
                                            estadisticas['promedio_puntos_por_partido'],
                                            estadisticas['rebotes_totales'],
                                            estadisticas['promedio_rebotes_por_partido'],
                                            estadisticas['asistencias_totales'],
                                            estadisticas['promedio_asistencias_por_partido'],
                                            estadisticas['robos_totales'],
                                            estadisticas['bloqueos_totales'],
                                            estadisticas['porcentaje_tiros_de_campo'],
                                            estadisticas['porcentaje_tiros_libres'],
                                            estadisticas['porcentaje_tiros_triples']
                                        )
                                    )
            return jugador_seleccionado
    else:
        print('El índice ingresado no es válido')



def armar_mensaje_para_indice_csv(jugadores:list, indice_jugador:int) -> str:
    """
    Toma la lista de jugadores y el índice ingresado por el jugador
    Devuelve un str para poder generar un csv
    """
    jugador = jugadores[indice_jugador]
    mensaje = "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}\n"
    mensaje = mensaje.format(
                jugador["nombre"],
                jugador["posicion"],
                jugador["estadisticas"]["temporadas"],
                jugador["estadisticas"]["puntos_totales"],
                jugador["estadisticas"]["promedio_puntos_por_partido"],
                jugador["estadisticas"]["rebotes_totales"],
                jugador["estadisticas"]["promedio_rebotes_por_partido"],
                jugador["estadisticas"]["asistencias_totales"],
                jugador["estadisticas"]["promedio_asistencias_por_partido"],
                jugador["estadisticas"]["robos_totales"],
                jugador["estadisticas"]["bloqueos_totales"],
                jugador["estadisticas"]["porcentaje_tiros_de_campo"],
                jugador["estadisticas"]["porcentaje_tiros_libres"],
                jugador["estadisticas"]["porcentaje_tiros_triples"]
    )
    return mensaje


def generar_csv(ruta: str, mensaje:str):
    """
    Toma como parámetro una ruta y un mensaje para generar un csv
    """
    with open(ruta, 'w') as archivo:
        archivo.write(mensaje)


def encontrar_nombre_jugador(jugadores: list):
    """
    This function takes a list of players and prompts the user to input a name to search for, then
    returns the player's information if found or None if not found.
    
    :param jugadores: The parameter "jugadores" is a list of dictionaries, where each dictionary
    represents a player and contains information such as their name, age, position, etc
    :type jugadores: list
    :return: either the dictionary of the player whose name matches the input name (if found in the list
    of players), or None if no player with that name is found in the list.
    """
    nombre = input('Ingrese el nombre del jugador a buscar: ')
    nombre_min = nombre.lower()
    for jugador in jugadores:
        nombre_jugador_min = jugador['nombre'].lower()
        if re.search(fr'\b{nombre}', nombre_jugador_min):
            return jugador
    return None



def mostrar_logros_por_nombre_ingresado() ->str:
    """
    Utiliza la función encontrar_nombre_jugador() para tomar un nombre ingresado
    
    Devuelve un str con los logros del jugador ingresado. Si no se encuentra, devuelve -1
    """
    jugador_encontrado = encontrar_nombre_jugador(jugadores)
    if jugador_encontrado:
        mensaje = '{0} - {1}'
        mensaje = mensaje.format(
                        jugador_encontrado['nombre'],
                        jugador_encontrado['logros']
        )
        return mensaje
    else:
        return -1
    





def mostrar_promedio_puntos_por_partido(jugadores: list):
    """
    Imprime el nombre y el promedio de puntos por partido de cada jugador de la lista, ordenados por nombre de la A a la Z
    
    Recibe como parámetro una lista
    """
    nombre_promedio_jugadores = []
    for jugador in jugadores:
        nombre = jugador['nombre']
        promedio_puntos = jugador['estadisticas']['promedio_puntos_por_partido']
        nombre_promedio_jugadores.append((nombre, promedio_puntos))

    nombre_promedio_jugadores_asc = quicksort.quick_sort(nombre_promedio_jugadores, True)

    for nombre, promedio_puntos in nombre_promedio_jugadores_asc:
        formato = '{0} - {1}'.format(nombre, promedio_puntos)
        print(formato)




def buscar_nombre_en_salon_de_la_fama(jugadores:list):
    """
    Utiliza la función encontrar_nombre_jugador() para tomar un nombre ingresado
    
    imprime un str mostrando si el jugador pertenece o no al salon de la fama
    """
    jugador_encontrado = encontrar_nombre_jugador(jugadores)
    if jugador_encontrado is not None:
        logros = jugador_encontrado['logros']
        if 'Miembro del Salon de la Fama del Baloncesto' in logros:
            print('{0} es miembro del salón de la fama'.format(jugador_encontrado['nombre']))
        else:
            print('{0} no es miembro del salón de la fama'.format(jugador_encontrado['nombre']))
    else:
        print('No se encuentra el jugador')



def calcular_mayor_cantidad_stat(jugadores:list, clave: str) -> str:
    """
    Toma la lista de jugadores y devuelve un string indicando quién sea el que tenga mayores estadísticas en la clave seleccionada
    
    Recibe como parámetro 'jugadores'(lista), 'clave'(la estadística que se desea calcular)
    """
    mayor_cantidad_total = 0
    jugador_con_mas = jugadores[0]['estadisticas'][clave]
    for jugador in jugadores:
        if (jugador['estadisticas'][clave] > mayor_cantidad_total):
            mayor_cantidad_total = jugador['estadisticas'][clave]
            jugador_con_mas = jugador['nombre']
    clave_formateada = clave.replace('_', ' ')
    formato = 'el jugador con más cántidad de {0} es: {1} ({2})'.format(
        clave_formateada,
        jugador_con_mas,
        mayor_cantidad_total
    )
    return formato

def validar_valor_a_superar():
    valor_a_superar = input('Ingrese un valor a superar: ')
    if re.match(r'^\d+(\.\d+)?$', valor_a_superar):
        valor_a_superar = float(valor_a_superar)
        return valor_a_superar
    else:
        return None

def calcular_mayor_que_el_valor_ingresado(jugadores:list, clave: str):
    """
    Toma la lista de jugadores e imprime un string indicando si se superan las estadísticas en la clave seleccionada que el valor ingresado
    
    Recibe como parámetro 'jugadores'(lista), 'clave'(la estadística que se desea calcular)
    """
    valor_a_superar = validar_valor_a_superar()
    if valor_a_superar is not None:
        for jugador in jugadores:
            if(jugador['estadisticas'][clave] > valor_a_superar):
                print('{0} supera el valor ingresado'.format(
                    jugador['nombre']
                ))
    else:
        print('El valor ingresado no es válido')



def calcular_mayor_cantidad_logros(jugadores: list) -> str:
    """
    Toma la lista de jugadores e imprime un string indicando quién es el que mayor cantidad de logros tiene
    
    Recibe como parámetro 'jugadores'(lista)
    """
    mayor_logros = 0
    jugador_con_mas = jugadores[0]['logros']
    for jugador in jugadores:
        if (len(jugador['logros']) > mayor_logros):
            mayor_logros = len(jugador['logros'])
            jugador_con_mas = jugador['nombre']
    formato = 'el jugador con más cántidad de logros es: {0}'.format(
        jugador_con_mas
    )
    return formato



def calcular_promedio_puntos_sin_menor(jugadores:list) -> list:
    """
    Toma la lista de jugadores y devuelve una lista que excluye al jugador que menos promedio de puntos tenga.
    
    Recibe como parámetro 'jugadores'(lista)
    """
    menor_promedio_puntos = float('inf')
    jugador_con_menos = jugadores[0]['estadisticas']['promedio_puntos_por_partido']
    lista_aux = []
    for jugador in jugadores:
        if (jugador['estadisticas']['promedio_puntos_por_partido'] < menor_promedio_puntos):
            menor_promedio_puntos = jugador['estadisticas']['promedio_puntos_por_partido']
            jugador_con_menos = jugador['nombre']
    for jugador in jugadores:
        if (jugador['nombre'] != jugador_con_menos):
            lista_aux.append(jugador['nombre'])

    return lista_aux



def ordenar_porcentaje_tiros_campo_posicion(jugadores:list):
    """
    Toma la lista de jugadores e imprime un string indicando quién sea el que tenga mayores estadísticas en la clave seleccionada que el valor ingresado
    El string los muestra ordenados según su posición.
    
    Recibe como parámetro 'jugadores'(lista), 'clave'(la estadística que se desea calcular) y  'valor_a_superar'(el valor que ingresa el usuario)
    """
    valor_a_superar = validar_valor_a_superar()
    if valor_a_superar is not None:
        posicion_nombre_porcentaje_jugadores = []
        for jugador in jugadores:
            if(jugador['estadisticas']['porcentaje_tiros_de_campo'] > valor_a_superar):
                posicion = jugador['posicion']
                nombre = jugador['nombre']
                porcentaje = jugador['estadisticas']['porcentaje_tiros_de_campo']
                posicion_nombre_porcentaje_jugadores.append((posicion, nombre, porcentaje))
        posicion_nombre_porcentaje_jugadores_asc = quicksort.quick_sort(posicion_nombre_porcentaje_jugadores, True)
        for posicion, nombre, porcentaje in posicion_nombre_porcentaje_jugadores_asc:
            print('{0} - {1} - {2}'.format(
                    posicion,
                    nombre,
                    porcentaje
                ))
    else:
        print('El valor ingresado no es válido')




def mostrar_cant_jugadores_posicion(jugadores:list):
    """
    Toma como parámetro la lista de jugadores e imprime la cantidad de jugadores que juegan en cada posición
    """
    diccionario_posiciones  = {}
    
    for jugador in jugadores:
        nombre_posicion = jugador['posicion']

        if nombre_posicion in diccionario_posiciones:
            diccionario_posiciones[nombre_posicion] += 1
        else:
            diccionario_posiciones[nombre_posicion] = 1

    for clave, valor in diccionario_posiciones.items():
        print('{0}: {1}'.format(
            clave,
            valor
        ))


def mostrar_mejores_cada_estadistica(jugadores:list):
    """
    Toma como parámetro la lista de jugadores e imprime quién es el jugador que mayores estadísticas posee en cada estadística
    """
    claves_estadisticas = jugadores[0]['estadisticas'].keys()

    for clave in claves_estadisticas:
        resultado = calcular_mayor_cantidad_stat(jugadores, clave)
        print(resultado)


def calcular_posiciones(jugadores):
    rankings = {
        'puntos_totales': [],
        'rebotes_totales': [],
        'asistencias_totales': [],
        'robos_totales': []
    }

    for jugador in jugadores:
        nombre = jugador['nombre']
        puntos = jugador['estadisticas']['puntos_totales']
        rebotes = jugador['estadisticas']['rebotes_totales']
        asistencias = jugador['estadisticas']['asistencias_totales']
        robos = jugador['estadisticas']['robos_totales']
        rankings['puntos_totales'].append((puntos, nombre))
        rankings['rebotes_totales'].append((rebotes, nombre))
        rankings['asistencias_totales'].append((asistencias, nombre))
        rankings['robos_totales'].append((robos, nombre))

    for categoria, jugadores in rankings.items():
        jugadores = quicksort.quick_sort(jugadores, False)
        for i in range(len(jugadores)):
            jugador = jugadores[i]
            mensaje = '{0}. {1}'
            mensaje = mensaje.format(
                    i+1,
                    jugador[1]
            )
    generar_csv('ranking.csv', mensaje)   

calcular_posiciones(jugadores)