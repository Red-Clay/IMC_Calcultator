import os
import pandas as pd

columnas_csv=["Nombre","Edad","Peso","Altura","IMC","Nivel de peso"]

peso_Actual=70
altura_Actual=1.7
edad_Actual=15
imc_Actual=0
nivel_peso=0

def guardar_csv():
    limpiar_consola()
    global columnas_csv
    global peso_Actual
    global altura_Actual
    global edad_Actual
    global imc_Actual
    global nivel_peso
    archivo=".\Datos_imc.csv"

    Nombre=input("Nombre con el que desea guardar: ")

    if os.path.exists(archivo):
        df=pd.read_csv(archivo)
        #BenditoMetodo
        lastvalidindex=df.last_valid_index()
        lastindex=lastvalidindex+1
        #print(lastindex)
        # Crear una nueva fila como un diccionario
        df.loc[lastindex] = [Nombre, edad_Actual, peso_Actual, altura_Actual, imc_Actual,nivel_peso]
        df.to_csv('Datos_imc.csv', index=False)
    else:
        # Nuevas columnas
        df = pd.DataFrame(columns=columnas_csv)
        df.loc[0] = [Nombre, edad_Actual, peso_Actual, altura_Actual, imc_Actual,nivel_peso]
        df.to_csv('Datos_imc.csv', index=False)

def return_range(min,max,valor):
    limpiar_consola()
    try:
        valor=float(valor)
    except ValueError:
        print("Valor incorrecto")
    tipo=type(valor)
    #print(tipo)
    
    if isinstance(valor,int) or isinstance(valor,float) :
        valor = float(valor)
        if valor >= float(min) and valor <= float(max): 
            return valor
        else:
            #print(f"Rango entre {min}-{max}")
            return 0
    else:
        return 0
    
def limpiar_consola():
    _so=os.name 
    if _so == "nt":
        os.system('cls')
    elif _so == "posix":
        os.system('clear')
    #print(_so)

def vercsv():
    archivo="Datos_imc.csv"
    if os.path.exists(archivo):
        limpiar_consola()
        df=pd.read_csv(archivo)
        print(df)
    else:
        limpiar_consola()
        print(f"No se encontro o no se ha creado el archivo {archivo}")

def marco(mensaje):
    marco = "+{:-^48}+".format('')
    mensaje_central = "|{:^48}|".format(mensaje)
    Respuesta= marco +"\n"+ mensaje_central + "\n" + marco
    return Respuesta
def Act_peso(P):
    limpiar_consola()
    global peso_Actual
    peso_Actual=P
    Respuesta=f"Peso Actualizado: " + str(peso_Actual) + " Kg"
    print(marco(Respuesta))

    #print("------------------------------")

def Act_altura(A):
    limpiar_consola()
    global altura_Actual
    altura_Actual=A
    Respuesta=f"Altura Actualizada: " + str(altura_Actual) + " M"
    print(marco(Respuesta))
    #print("------------------------------")

def Act_edad(E):
    limpiar_consola()
    global edad_Actual
    edad_Actual = E
    Respuesta=f"Edad Actualizada: " + str(edad_Actual) + " Años"
    print(marco(Respuesta))
    #print("------------------------------")

def Ver_perfil():
    limpiar_consola()
    print(f"Peso : {peso_Actual} Kg\n")
    print(f"Altura : {altura_Actual}\n")
    print(f"Edad : {edad_Actual}\n")
    print(f"IMC : {imc_Actual}\n")    

def Cal_IMC():
    global peso_Actual
    global altura_Actual
    limpiar_consola()
    global imc_Actual
    global nivel_peso
    imc_Actual = float(peso_Actual)/(float(altura_Actual)*float(altura_Actual))
    Respuesta=f"IMC Actualizado: " + str(imc_Actual)
    print(marco(Respuesta))

    if imc_Actual<18.5:
        nivel_peso="INFERIOR al normal"
    elif imc_Actual>=18.5 and imc_Actual<=24.9:
        nivel_peso="Normal"
    elif imc_Actual>=25 and imc_Actual<=29.9:
        nivel_peso="SUPERIOR al normal"
    elif imc_Actual>=30:
        nivel_peso="Obeso"