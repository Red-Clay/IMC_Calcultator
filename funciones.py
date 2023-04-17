import os
import pandas as pd
columnas_csv=["Nombre","Edad","Peso","Altura","IMC"]

peso_Actual=70
altura_Actual=1.7
edad_Actual=15
imc_Actual=0

def guardar_csv():
    limpiar_consola()
    global columnas_csv
    global peso_Actual
    global altura_Actual
    global edad_Actual
    global imc_Actual
    archivo=".\Datos_imc.csv"

    Nombre=input("Nombre con el que desea guardar: ")

    if os.path.exists(archivo):
        df=pd.read_csv(archivo)
        #BenditoMetodo
        lastvalidindex=df.last_valid_index()
        lastindex=lastvalidindex+1
        #print(lastindex)
        # Crear una nueva fila como un diccionariohow to deal with convert in python
        df.loc[lastindex] = [Nombre, edad_Actual, peso_Actual, altura_Actual, imc_Actual]
        df.to_csv('Datos_imc.csv', index=False)
    else:
        df = pd.DataFrame(columns=columnas_csv)
        df.loc[0] = [Nombre, edad_Actual, peso_Actual, altura_Actual, imc_Actual]
        df.to_csv('Datos_imc.csv', index=False)

def return_range(min,max,valor):
    #tipo=type(valor)
    #print(tipo)
    try:
        valor = float(valor)
        if valor >= float(min) and valor <= float(max): 
            return valor
        else:
            #print(f"Rango entre {min}-{max}")
            return 0
    except ValueError:
        return 0
    #if (valor > min and valor < max) and (tipo=="<class 'float'>"): 
     #  #re(tipo)
    #else:
        #return 0

def limpiar_consola():
    os.system('cls')

def vercsv():
    archivo="Datos_imc.csv"
    if os.path.exists(archivo):
        limpiar_consola()
        df=pd.read_csv(archivo)
        print(df)
    else:
        limpiar_consola()
        print(f"No se encontro o no se ha creado el archivo {archivo}")

def Act_peso(P):
    limpiar_consola()
    global peso_Actual
    peso_Actual=P
    Respuesta=f"La Peso ha sido actualizada a:" + str(peso_Actual) + "Kg"
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
    print(f"Peso Actual: {peso_Actual} Kg\n")
    print(f"Altura Actual: {altura_Actual}\n")
    print(f"Edad Actual: {edad_Actual}\n")
    print(f"IMC Actual: {imc_Actual}\n")    

def Cal_IMC():
    global peso_Actual
    global altura_Actual
    limpiar_consola()
    global imc_Actual
    imc_Actual = float(peso_Actual)/(float(altura_Actual)*float(altura_Actual))
    Respuesta=f"Su IMC es de :" + str(imc_Actual)
    return Respuesta
