import funciones
import json
import re


with open("pp_lab1_brunell_nazareno\dt.json") as file:
    data = json.load(file)

jugadores = data['jugadores']

indice_jugador = None

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Mostrar todos los jugadores")
    print("2. Seleccionar un jugador y mostrar sus estadísticas")
    print("3. Generar CSV del jugador seleccionado")
    print("4. Buscar un jugador y mostrar sus logros")
    print("5. Mostrar el promedio de los jugadores ordenado por nombre")
    print("6. Ingresar un jugador y buscar si es miembro del salón de la fama")
    print("7. Mostrar jugador con más rebotes totales")
    print("8. Mostrar jugador con más porcentaje de tiros de campo")
    print("9. Mostrar jugador con más asistencias totales")
    print("10. Ingresar un valor y mostrar jugadores que promedien más puntos por partido que el valor")
    print("11. Ingresar un valor y mostrar jugadores que promedien más rebotes por partido que el valor")
    print("12. Ingresar un valor y mostrar jugadores que promedien más asistencias por partido que el valor")
    print("13. Mostrar jugador con más robos totales")
    print("14. Mostrar jugador con más bloqueos totales")
    print("15. Ingresar un valor y mostrar jugadores cuyo porcentaje de tiros libres supere el valor")
    print("16. Mostrar el promedio de puntos por partidos de todos los jugadores excluyendo el que tenga menos")
    print("17. Mostrar jugador con más cantidad de logros")
    print("18. Ingresar un valor y mostrar jugadores cuyo porcentaje de tiros triples supere el valor")
    print("19. Mostrar jugador con más temporadas jugadas")
    print("20. Ingresar un valor y mostrar jugadores cuyo porcentaje de tiros de campo supere el valor, ordenados por posición")
    print("23. Calcular la posición de cada jugador en un ranking de: Puntos - Rebotes - Asistencias - Robos. y generar CSV")
    print("extra 1. Cantidad de jugadores que hay en cada posición")
    print("extra 2. Calcular y mostrar los jugadores que más All Star tienen")
    print("extra 3. Mostrar que jugador tiene las mejores estadísticas en cada valor")
    print("extra 4. Calcular qué jugador posee más estadisticas")

    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")

    match opcion:
        case "1":
            funciones.mostrar_jugadores(jugadores)
        case "2":
            indice_jugador = input('ingrese el índice del jugador que quiere ver')
            if (re.match(r'^\d+$', indice_jugador)):
                indice_jugador = int(indice_jugador)
                print(funciones.mostrar_estadisticas_por_indice_ingresado(jugadores, indice_jugador))
            else:
                print('el índice ingresado no es válido')
        case "3":
            if (indice_jugador is not None):
                funciones.generar_csv('jugador seleccionado.csv', funciones.armar_mensaje_para_indice_csv(jugadores, indice_jugador))
            else:
                print('No se ha declarado un índice')
        case "4":
            print(funciones.mostrar_logros_por_nombre_ingresado())
        case "5":
            funciones.mostrar_promedio_puntos_por_partido(jugadores)
        case "6":
            funciones.buscar_nombre_en_salon_de_la_fama(jugadores)
        case "7":
            print(funciones.calcular_mayor_cantidad_stat(jugadores, 'rebotes_totales'))
        case "8":
            print(funciones.calcular_mayor_cantidad_stat(jugadores, 'porcentaje_tiros_de_campo'))
        case "9":
            print(funciones.calcular_mayor_cantidad_stat(jugadores, 'asistencias_totales'))
        case "10":
            funciones.calcular_mayor_que_el_valor_ingresado(jugadores, 'promedio_puntos_por_partido')
        case "11":
            funciones.calcular_mayor_que_el_valor_ingresado(jugadores, 'promedio_rebotes_por_partido')
        case "12":
            funciones.calcular_mayor_que_el_valor_ingresado(jugadores, 'promedio_asistencias_por_partido')
        case "13":
            print(funciones.calcular_mayor_cantidad_stat(jugadores, 'robos_totales'))
        case "14":
            print(funciones.calcular_mayor_cantidad_stat(jugadores, 'bloqueos_totales'))
        case "15":
            funciones.calcular_mayor_que_el_valor_ingresado(jugadores, 'porcentaje_tiros_libres')
        case "16":
            print(funciones.calcular_promedio_puntos_sin_menor(jugadores))
        case "17":
            print(funciones.calcular_mayor_cantidad_logros(jugadores))
        case "18":
            funciones.calcular_mayor_que_el_valor_ingresado(jugadores, 'porcentaje_tiros_triples')
        case "19":
            print(funciones.calcular_mayor_cantidad_stat(jugadores, 'temporadas'))
        case "20":
            funciones.ordenar_porcentaje_tiros_campo_posicion(jugadores)
        case "23":
            funciones.calcular_posiciones(jugadores)
        case "extra 1":
            funciones.mostrar_cant_jugadores_posicion(jugadores)
        case "extra 2":
            pass
        case "extra 3":
            funciones.mostrar_mejores_cada_estadistica(jugadores)
        case "extra 4":
            pass
        case '0':
            exit()
        case _:
            print('El valor ingresado no es correcto')