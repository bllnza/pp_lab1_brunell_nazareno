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
    if indice_jugador:
        if (re.match(r'^\d+$', indice_jugador)):
            indice_jugador = int(indice_jugador)
            if 0 <= indice_jugador < len(jugadores):
                    jugador = jugadores[indice_jugador]
                    estadisticas = jugador['estadisticas']
                    jugador_seleccionado = ("Estadísticas de {0}: \n"
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
    else:
        print('No se ingresó ningún índice')

    return jugador_seleccionado




def generar_csv(jugadores:list, jugador_seleccionado: str):
    """
    Genera un csv si se declaró un índice en la función anterior. Sino, imprime un mensaje aclarando que no se declaró
    
    Recibe como parámetro la lista de jugadores y al jugador seleccionado de la función anterior
    """

    if jugador_seleccionado:
        with open('jugador_seleccionado.csv', 'w') as archivo:
            mensaje = jugador_seleccionado.replace('\n', ', ')
            archivo.write(mensaje)
    else:
        print('No se seleccionó ningún jugador')




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






