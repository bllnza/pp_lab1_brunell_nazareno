import funciones
import json
import re

with open("pp_lab1_brunell_nazareno\dt.json") as file:
    data = json.load(file)

jugadores = data['jugadores']



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
    print("21. ")

    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")

    match opcion:
        case "1":
            funciones.mostrar_jugadores(jugadores)
        case "2":
            indice_jugador = input('ingrese el índice del jugador que quiere ver')
            print(funciones.seleccionar_por_indice(jugadores, indice_jugador))
        case "3":
            funciones.generar_csv(jugadores, funciones.seleccionar_por_indice(jugadores, indice_jugador))
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            pass
        case "13":
            pass
        case "14":
            pass
        case "15":
            pass
        case "16":
            pass
        case "17":
            pass
        case "18":
            pass
        case "19":
            pass
        case "20":
            pass
        case "21":
            pass
        case '0':
            exit()
        case _:
            print('El número ingresado no es correcto')