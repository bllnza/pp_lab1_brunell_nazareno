import json
import re

with open("dt.json") as file:
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


mostrar_jugadores(jugadores)

#Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, 
# promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, 
# bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.