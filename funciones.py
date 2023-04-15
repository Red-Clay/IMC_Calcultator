import os

peso_actual=0
altura_Actual=0
edad_Actual=0
imc_Actual=0

def limpiar_consola():
    os.system('cls')


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
    print(f"Peso Actual: {peso_actual} Kg\n")
    print(f"Altura Actual: {altura_Actual}\n")
    print(f"Edad Actual: {edad_Actual}\n")
    print(f"IMC Actual: {imc_Actual}\n")    

def Cal_IMC():
    global peso_actual
    global altura_Actual
    limpiar_consola()
    global imc_Actual
    imc_Actual = float(peso_actual)/(float(altura_Actual)*float(altura_Actual))
    Respuesta=f"Su IMC es de :" + str(imc_Actual)
    return Respuesta
