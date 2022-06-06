n = 11

matriz = [[0 for i in range(n)] for j in range(n)]

#F0 F1 F2
#0  0  0 -> colunna 0
#0  1  2 -> colunna 1
#0  2  4 -> colunna 2

for i in range (len(matriz)):
    arreglo = matriz[i]
    for j in range(len(arreglo)):
        arreglo[j] = i * j

i = 0
j = 0

for i in range (len(matriz)):
    arreglo = matriz[i]
    print(arreglo)

n1 = int(input("ingrese un numero"))
n2 = int(input("ingrese otro numero"))
print (str(n1) + " * " +  str(n2) + " el resultado es: " + str(matriz[n1][n2]))
        
