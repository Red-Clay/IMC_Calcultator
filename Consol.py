import funciones
funciones.limpiar_consola()
while True:

    print("-"*40)
    print(f"1-Peso....(Kilogramos = {funciones.peso_Actual} )")
    print(f"2-Altura..(Metros = {funciones.altura_Actual} )")
    print(f"3-Edad....(Años = {funciones.edad_Actual} )")
    print(f"4-IMC.....(Indice de Masa Corporal = {funciones.imc_Actual} )")
    print("5-Perfil")
    print("6-Save")
    print("7-CSV")
    print("8-Salir")

    print("-"*40)
#Un añadido copiado, pero con flujos logicos faciles de entender
    opc = input("Elige una opción: ")



    if opc in ["1","2","3","4","5","6","7","8"]:
        opcion = int(opc)
    else:
        opcion=0
        funciones.limpiar_consola()

    if opcion == 1:
        _inp = input("Ingresa el peso: ")
        x=funciones.return_range(0,150,_inp)
        if x != 0 :funciones.Act_peso(x)
    elif opcion == 2:
        _alt = input("Ingresa el altura: ")
        x = funciones.return_range(0,2,_alt)
        if x != 0 : funciones.Act_altura(x)
    elif opcion == 3:
        _ed = input("Ingresa la edad: ")
        x=funciones.return_range(0,100,_ed)
        if x != 0 : funciones.Act_edad(x)
    elif opcion == 4:
        funciones.Cal_IMC()
    elif opcion == 5:
        funciones.Ver_perfil()
    elif opcion == 6:
        funciones.guardar_csv()
    elif opcion == 7:
        funciones.vercsv()
    elif opcion == 8:
        break