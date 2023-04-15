import os
#Un bucle infinito para ver las opciones de calculo del IMC
Peso_Actual=0
Altura_Actual=0
Edad_Actual=0
IMC_Actual=0
def Act_peso(P):
    global Peso_Actual
    Peso_Actual=P
    Respuesta=f"La Peso ha sido actualizada a:" + str(Peso_Actual)
    print(Respuesta)

def Act_altura(A):
    global Altura_Actual
    Altura_Actual=A
    Respuesta=f"La Altura ha sido actualizada a:" + str(Altura_Actual)
    print(Respuesta)

def Act_edad(E):
    global Edad_Actual
    Edad_Actual = E
    Respuesta=f"La Edad ha sido actualizada a:" + str(Edad_Actual)
    print(Respuesta)

def Cal_IMC(peso,altura):
    global IMC_Actual
    IMC_Actual = float(peso)/(float(altura)*float(altura))
    Respuesta=f"Su IMC es de :" + str(Edad_Actual)
    return Respuesta

def Ver_perfil():
    print(f"Peso Actual: {Peso_Actual}\n")
    print(f"Altura Actual: {Peso_Actual}\n")
    print(f"Edad Actual: {Peso_Actual}\n")
    print(f"IMC Actual: {IMC_Actual}\n")

while True:
    print("1-Añade tu peso (Kg)")
    print("2-Añade tu Altura (M)")
    print("3-Añade tu edad ())")
    print("4-Calcula tu IMC  (Indice de Masa Corporal)")
    print("5-Respuesta completa de tu perfil actual")
#Un añadido copiado, pero con flujos logicos faciles de entender
    opcion = int(input("Elige una opción: "))
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
        print(f"{Cal_IMC(Peso_Actual,Altura_Actual)}")
    elif opcion == 5:
        break