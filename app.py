import funciones
import json


with open("pp_lab1_brunell_nazareno\dt.json") as file:
    data = json.load(file)

jugadores = data['jugadores']

indice_jugador = None

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1.")
    print("2.")
    print("3.  ")
    print("4. ")
    print("5. ")
    print("6. ")
    print("7. ")
    print("8. ")
    print("9. ")
    print("10..")
    print("11. ")
    print("12. ")
    print("13. ")
    print("14. ")
    print("15. ")
    print("16. ")
    print("17. ")
    print("18. ")
    print("19. ")
    print("20. ")

    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")

    match opcion:
        case "1":
            funciones.mostrar_jugadores(jugadores)
        case "2":
            indice_jugador = input('ingrese el índice del jugador que quiere ver')
            print(funciones.estadisticas_por_indice(jugadores, indice_jugador))
        case "3":
            if (indice_jugador is not None):
                funciones.generar_csv(jugadores, funciones.estadisticas_por_indice(jugadores, indice_jugador))
            else:
                'No se ha declarado un índice'
        case "4":
            nombre_jugador = input('ingrese nombre de jugador')
            print(funciones.logros_por_nombre(jugadores, nombre_jugador))
        case "5":
            funciones.promedio_puntos_por_partido(jugadores)
        case "6":
            nombre_jugador = input('ingrese nombre de jugador')
            funciones.nombre_salon_de_la_fama(jugadores, nombre_jugador)
        case "7":
            print(funciones.mayor_cantidad(jugadores, 'rebotes_totales'))
        case "8":
            print(funciones.mayor_cantidad(jugadores, 'porcentaje_tiros_de_campo'))
        case "9":
            print(funciones.mayor_cantidad(jugadores, 'asistencias_totales'))
        case "10":
            valor_a_superar = input('Ingrese un valor a superar')
            valor_a_superar = float(valor_a_superar)
            funciones.mayor_que_el_valor(jugadores, valor_a_superar, 'promedio_puntos_por_partido')
        case "11":
            valor_a_superar = input('Ingrese un valor a superar')
            valor_a_superar = float(valor_a_superar)
            funciones.mayor_que_el_valor(jugadores, valor_a_superar, 'promedio_rebotes_por_partido')
        case "12":
            valor_a_superar = input('Ingrese un valor a superar')
            valor_a_superar = float(valor_a_superar)
            funciones.mayor_que_el_valor(jugadores, valor_a_superar, 'promedio_asistencias_por_partido')
        case "13":
            print(funciones.mayor_cantidad(jugadores, 'robos_totales'))
        case "14":
            print(funciones.mayor_cantidad(jugadores, 'bloqueos_totales'))
        case "15":
            valor_a_superar = input('Ingrese un valor a superar')
            valor_a_superar = float(valor_a_superar)
            funciones.mayor_que_el_valor(jugadores, valor_a_superar, 'porcentaje_tiros_libres')
        case "16":
            print(funciones.promedio_puntos_sin_menor(jugadores))
        case "17":
            print(funciones.mayor_cantidad_logros(jugadores))
        case "18":
            valor_a_superar = input('Ingrese un valor a superar')
            valor_a_superar = float(valor_a_superar)
            funciones.mayor_que_el_valor(jugadores, valor_a_superar, 'porcentaje_tiros_triples')
        case "19":
            print(funciones.mayor_cantidad(jugadores, 'temporadas'))
        case "20":
            valor_a_superar = input('Ingrese un valor a superar')
            valor_a_superar = float(valor_a_superar)
            funciones.porcentaje_tiros_campo_posicion(jugadores, valor_a_superar)
        case '0':
            exit()
        case _:
            print('El número ingresado no es correcto')