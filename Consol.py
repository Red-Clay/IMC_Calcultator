import funciones



funciones.limpiar_consola()

while True:
    print("------------------------------")
    print(f"1-Añade tu peso (Kg )")
    print(f"2-Añade tu Altura (M )")
    print(f"3-Añade tu edad (años )")
    print(f"4-Calcula tu funciones  (Indice de Masa Corporal = )")
    print("5-Respuesta completa de tu perfil actual")
    print("6-Salir")

    print("------------------------------")
#Un añadido copiado, pero con flujos logicos faciles de entender
    opcion = int(input("Elige una opción: "))
    print("------------------------------")
    if opcion == 1:
        i_peso = float(input("Ingresa el peso: "))
        funciones.Act_peso(i_peso)
    elif opcion == 2:
        i_altura = float(input("Ingresa el altura: "))
        funciones.Act_altura(i_altura)
    elif opcion == 3:
        i_edad = int(input("Ingresa la edad: "))
        funciones.Act_edad(i_edad)
    elif opcion == 4:
        print(f"{funciones.Cal_IMC()}")
    elif opcion == 5:
        funciones.Ver_perfil()
    elif opcion == 6:
        break