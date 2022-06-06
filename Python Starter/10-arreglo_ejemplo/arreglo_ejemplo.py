#pedir las calificaciones
#guardarlas en un arreglo
#recorrer ese arreglo y leer las calificacione
#dividir la suma entre el total de calificaciones y listo

calificacion = 0
calificaciones = []
i = 1

print ("para salir ingrasa un numero negativo")
while calificacion >= 0:
    calificacion = int(input("dame la calificacion " + str(i)+ ": "))
    if calificacion >= 0:
        calificaciones.append(calificacion)
        i = i +1

suma = 0

for cal in calificaciones:
    suma = suma + cal

    print ("tu promedio es: "+ str(suma / len (calificaciones)))

#[10,9,8,7] -> 0 + 10 = 10
# -> 10 + 9 = 19
# -> 19 + 8 = 27
# -> 27 + 7 = 34


 
