import re


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






def estadisticas_por_indice(jugadores: list, indice_jugador: str) -> str:
    """
    Recibe un número de índice ingresado para mostrar las estadísticas del jugador
    
    Recibe como parámetro 'jugadores', que es una lista de diccionarios
    Devuelve un string que muestra las estadísticas y el nombre del jugador seleccionado
    """

    if (re.match(r'^\d+$', indice_jugador)):
        indice_jugador = int(indice_jugador)
        if 0 < indice_jugador < len(jugadores):
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
        else:
            print('El índice ingresado no es válido')
    else:
        print('el índice ingresado no es válido')


    return jugador_seleccionado




def generar_csv(jugadores:list, jugador_seleccionado: str):
    """
    Genera un csv si se declaró un índice en la función anterior. Sino, imprime un mensaje aclarando que no se declaró
    
    Recibe como parámetro la lista de jugadores y al jugador seleccionado de la función anterior
    """
    with open('jugador_seleccionado.csv', 'w') as archivo:
        mensaje = jugador_seleccionado.replace('\n', ', ')
        archivo.write(mensaje)





def logros_por_nombre(jugadores: list, nombre_jugador:str):
    """
    Recibe un nombre ingresado para mostrar los logros del jugador deseado
    
    Recibe como parámetro 'jugadores', que es una lista de diccionarios 
    Devuelve un string que muestra los logros y el nombre del jugador seleccionado. En caso de no encontralo, devuelve -1
    """
    for jugador in jugadores:
        if jugador['nombre'] == nombre_jugador:
            logros = jugador.get('logros')
            formato =('Logros de {0}: \n'
                            '{1}'.format(
                                nombre_jugador,
                                logros
                            ))
            return formato
        else:
            return -1





def promedio_puntos_por_partido(jugadores: list):
    """
    Imprime el nombre y el promedio de puntos por partido de cada jugador de la lista, ordenados por nombre de la A a la Z
    
    Recibe como parámetro una lista
    """
    nombre_promedio_jugadores = []
    for jugador in jugadores:
        nombre = jugador['nombre']
        promedio_puntos = jugador['estadisticas']['promedio_puntos_por_partido']
        nombre_promedio_jugadores.append((nombre, promedio_puntos))

    nombre_promedio_jugadores.sort()

    for nombre, promedio_puntos in nombre_promedio_jugadores:
        formato = '{0} - {1}'.format(nombre, promedio_puntos)
        print(formato)




def nombre_salon_de_la_fama(jugadores:list, nombre_jugador:str):
    """
    Recibe el nombre de un basquetbolista y busca si dentro de sus logros es parte del salón de la fama
    
    Recibe una lista y un string
    """
    jugador_encontrado = None
    for jugador in jugadores:
        if jugador['nombre'] == nombre_jugador:
            jugador_encontrado = jugador
    if jugador_encontrado is not None:
        logros = jugador_encontrado['logros']
        if 'Miembro del Salon de la Fama del Baloncesto' in logros:
            print('{0} es miembro del salón de la fama'.format(nombre_jugador))
        else:
            print('{0} no es miembro del salón de la fama'.format(nombre_jugador))
    else:
        print('No se encuentra el jugador')



def mayor_cantidad(jugadores:list, clave: str) -> str:
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



def mayor_que_el_valor(jugadores:list, valor_a_superar: float, clave: str):
    """
    Toma la lista de jugadores e imprime un string indicando si se superan las estadísticas en la clave seleccionada que el valor ingresado
    
    Recibe como parámetro 'jugadores'(lista), 'clave'(la estadística que se desea calcular) y  'valor_a_superar'(el valor que ingresa el usuario)
    """
    for jugador in jugadores:
        if(jugador['estadisticas'][clave] > valor_a_superar):
            print('{0} supera el valor ingresado'.format(
                jugador['nombre']
            ))



def mayor_cantidad_logros(jugadores: list) -> str:
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



def promedio_puntos_sin_menor(jugadores:list) -> list:
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



def porcentaje_tiros_campo_posicion(jugadores:list, valor_a_superar:float):
    """
    Toma la lista de jugadores e imprime un string indicando quién sea el que tenga mayores estadísticas en la clave seleccionada que el valor ingresado
    El string los muestra ordenados según su posición.
    
    Recibe como parámetro 'jugadores'(lista), 'clave'(la estadística que se desea calcular) y  'valor_a_superar'(el valor que ingresa el usuario)
    """
    posicion_nombre_porcentaje_jugadores = []
    for jugador in jugadores:
        if(jugador['estadisticas']['porcentaje_tiros_de_campo'] > valor_a_superar):
            posicion = jugador['posicion']
            nombre = jugador['nombre']
            porcentaje = jugador['estadisticas']['porcentaje_tiros_de_campo']
            posicion_nombre_porcentaje_jugadores.append((posicion, nombre, porcentaje))
    posicion_nombre_porcentaje_jugadores.sort()
    for posicion, nombre, porcentaje in posicion_nombre_porcentaje_jugadores:
        print('{0} - {1} - {2}'.format(
                posicion,
                nombre,
                porcentaje
            ))




def cant_jugadores_posicion(jugadores:list):
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


def mejores_cada_estadistica(jugadores:list):
    """
    Toma como parámetro la lista de jugadores e imprime quién es el jugador que mayores estadísticas posee en cada estadística
    """
    claves_estadisticas = jugadores[0]['estadisticas'].keys()

    for clave in claves_estadisticas:
        resultado = mayor_cantidad(jugadores, clave)
        print(resultado)

