import json
import re

with open("pp_lab1_brunell_nazareno\dt.json") as file:
    data = json.load(file)

jugadores = data['jugadores']

#Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
#Nombre Jugador - Posición. Ejemplo:
#Michael Jordan - Escolta

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


#mostrar_jugadores(jugadores)

#Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, 
# promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, 
# bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

def seleccionar_por_indice(jugadores: list, indice: int) -> str:
    jugador = jugadores[indice]
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
    return jugador_seleccionado

indice_jugador = input('ingrese el índice del jugador que quiere ver')
if (re.match(r'^\d+$', indice_jugador)):
    indice_jugador = int(indice_jugador)
    if 0 <= indice_jugador < len(jugadores):
        print(seleccionar_por_indice(jugadores, indice_jugador))
    else:
        print('El índice ingresado no es válido')
else:
    print('el índice ingresado no es válido')

