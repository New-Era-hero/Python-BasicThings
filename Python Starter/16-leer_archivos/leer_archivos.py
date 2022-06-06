archivo = open("SVC.txt","r")
matriz = []
for linea in archivo:
    arreglo_cadenas = linea.split(",")
    arreglo = []
    for j in range(len(arreglo_cadenas)):
        numero_sin_caracteres = int (arreglo_cadenas[j])
        arreglo.append(numero_sin_caracteres)
    matriz.append(arreglo)

n1 = int(input("ingrese un numero"))
n2 = int(input("ingrese otro numero"))
print (str(n1) + " * " +  str(n2) + " el resultado es: " + str(matriz[n1][n2]))
    
    
