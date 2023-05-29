import json
import re

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






def estadisticas_por_indice(jugadores: list, indice_jugador: str) -> str:
    """
    Recibe un número de índice ingresado para mostrar las estadísticas del jugador
    
    Recibe como parámetro 'jugadores', que es una lista de diccionarios
    Devuelve un string que muestra las estadísticas y el nombre del jugador seleccionado
    """

    if (re.match(r'^\d+$', indice_jugador)):
        indice_jugador = int(indice_jugador)
        if 0 <= indice_jugador < len(jugadores):
                jugador = jugadores[indice_jugador]
                estadisticas = jugador['estadisticas']
                jugador_seleccionado = ("Estadisticas de {0}: \n"
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
    Imprime el nombre y el promedio de puntos por partido de cada jugador de la lista
    
    Recibe como parámetro una lista
    """
    for jugador in jugadores:
        formato = '{0} - {1}'.format(
            jugador['nombre'],
            jugador['estadisticas']['promedio_puntos_por_partido']
        )
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
            break
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
    formato = 'el jugador con más cántidad de {0} es: {1}'.format(
        clave_formateada,
        jugador_con_mas
    )
    return formato


#Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
valor_a_superar = input('Ingrese un valor a superar')
valor_a_superar = float(valor_a_superar)
def mayor_que_el_valor(jugadores:list, valor_a_superar: float, clave: str):
    lista_aux_mayor_valor = []
    for jugador in jugadores:
        if(jugador['estadisticas'][clave] > valor_a_superar):
            print('{0} supera el valor ingresado'.format(
                jugador['nombre']
            ))




mayor_que_el_valor(jugadores, valor_a_superar, 'promedio_puntos_por_partido')