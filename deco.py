from funciones import limpiar_consola
import msvcrt

diccionario_imc={"peso_Actual":70,"altura_Actual":1.2,"edad_Actual":15,"puntos":2}
#print(diccionario_imc)
v=0
""""for clave,valor in diccionario_imc.items():
        v=v+1
        #print(f"{clave}:{valor}")
        globals()[clave] = valor
print(puntos)
print(edad_Actual)
print(peso_Actual)
print(diccionario_imc)"""
limpiar_consola()
digits = []
print("Introduce la opcion: ")
while True:
    key = msvcrt.getch()
    if key.decode() == "\r":
        break
    if key.decode() =="\x08":
        digits= digits[:-1]

    if  len(digits)<3 and key.decode() != "\r" and key.decode() != "\x08" :

        limpiar_consola()
        digits.append(key.decode())
        my_string = ''.join([str(x) for x in digits])
        print("Introduce la opcion: "+my_string)

print(digits)
#print(digits)