n = 11
matriz = [[0 for i in range(n)] for j in range(n)]

for i in range (len(matriz)):
    arreglo = matriz[i]
    for j in range(len(arreglo)):
        arreglo[j] = i * j

file = open("escribir_archivos.txt","w")

for i in (len(matriz)):
    arreglo = matriz[i]
    for j in range(len(arreglo)):
        numero = arreglo[j]
        if j < (len(arreglo)) -1:
            file.write(str(numero)+",")
        else:
            file.write(str(numero))
    if i < (len(arreglo)) -1:
        file.write("\n")
        
# R sirve para leer un archivo
# W sirve para escribir en un archivo pero borra todo el contenido que tenia el mismo
# A lo mismo que la anterior con la diferencia que todo va al final sin borrar el contenido
