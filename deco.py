
diccionario_imc={"peso_Actual":70,"altura_Actual":1.2,"edad_Actual":15,"puntos":2}
#print(diccionario_imc)
v=0
for clave,valor in diccionario_imc.items():
        v=v+1
        #print(f"{clave}:{valor}")
        globals()[clave] = valor
print(puntos)
print(edad_Actual)
print(peso_Actual)
print(diccionario_imc)