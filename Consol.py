import funciones
funciones.limpiar_consola()
while True:
    print("------------------------------")
    print(f"1-Añade tu peso (Kg = {funciones.peso_Actual} )")
    print(f"2-Añade tu Altura (M = {funciones.altura_Actual} )")
    print(f"3-Añade tu edad (años = {funciones.edad_Actual} )")
    print(f"4-Calcula tu IMC  (Indice de Masa Corporal = {funciones.imc_Actual} )")
    print("5-Respuesta completa de tu perfil actual")
    print("6-guardar perfil")
    print("7-ver csv")
    print("8-Salir")

    print("------------------------------")
#Un añadido copiado, pero con flujos logicos faciles de entender
    opc = input("Elige una opción: ")
    if opc in ["1","2","3","4","5","6","7","8","9"]:
        opcion = int(opc)
    else:
        opcion=0
        funciones.limpiar_consola()

    if opcion == 1:
        _inp = input("Ingresa el peso: ")
        i_peso=funciones.return_range(0,100,_inp)
        print(i_peso)
        funciones.Act_peso(i_peso)
    elif opcion == 2:
        _alt = input("Ingresa el altura: ")
        i_altura=funciones.return_range(0,4,_alt)
        funciones.Act_altura(i_altura)
    elif opcion == 3:
        _ed = input("Ingresa la edad: ")
        i_edad=funciones.return_range(0,100,_ed)
        funciones.Act_edad(i_edad)
    elif opcion == 4:
        print(f"{funciones.Cal_IMC()}")
    elif opcion == 5:
        funciones.Ver_perfil()
    elif opcion == 6:
        funciones.guardar_csv()
    elif opcion == 7:
        funciones.vercsv()
    elif opcion == 8:
        break