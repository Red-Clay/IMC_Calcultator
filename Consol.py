import os

peso_actual=0
altura_Actual=0
edad_Actual=0
imc_Actual=0

def limpiar_consola():
    os.system('cls')

limpiar_consola()

def Act_peso(P):
    limpiar_consola()
    global peso_actual
    peso_actual=P
    Respuesta=f"La Peso ha sido actualizada a:" + str(peso_actual) + "Kg"
    print("------------------------------")
    print(Respuesta)
    print("------------------------------")
def Act_altura(A):
    limpiar_consola()
    global altura_Actual
    altura_Actual=A
    Respuesta=f"La Altura ha sido actualizada a:" + str(altura_Actual) + "M"
    print("------------------------------")
    print(Respuesta)
    print("------------------------------")
def Act_edad(E):
    limpiar_consola()
    global edad_Actual
    edad_Actual = E
    Respuesta=f"La Edad ha sido actualizada a:" + str(edad_Actual) + "Años"
    print("------------------------------")
    print(Respuesta)
    print("------------------------------")

def Ver_perfil():
    limpiar_consola()
    print(f"Peso Actual: {peso_actual}\n")
    print(f"Altura Actual: {altura_Actual}\n")
    print(f"Edad Actual: {edad_Actual}\n")
    print(f"IMC Actual: {imc_Actual}\n")    

def Cal_IMC(peso,altura):
    limpiar_consola()
    global imc_Actual
    imc_Actual = float(peso)/(float(altura)*float(altura))
    Respuesta=f"Su IMC es de :" + str(imc_Actual)
    return Respuesta

while True:
    print("------------------------------")
    print("1-Añade tu peso (Kg)")
    print("2-Añade tu Altura (M)")
    print("3-Añade tu edad ()")
    print("4-Calcula tu IMC  (Indice de Masa Corporal)")
    print("5-Respuesta completa de tu perfil actual")
    print("6-Salir")

    print("------------------------------")
#Un añadido copiado, pero con flujos logicos faciles de entender
    opcion = int(input("Elige una opción: "))
    print("------------------------------")
    if opcion == 1:
        i_peso = float(input("Ingresa el peso: "))
        Act_peso(i_peso)
    elif opcion == 2:
        i_altura = float(input("Ingresa el altura: "))
        Act_altura(i_altura)
    elif opcion == 3:
        i_edad = int(input("Ingresa la edad: "))
        Act_edad(i_edad)
    elif opcion == 4:
        print(f"{Cal_IMC(peso_actual,altura_Actual)}")
    elif opcion == 5:
        Ver_perfil()
    elif opcion == 6:
        break