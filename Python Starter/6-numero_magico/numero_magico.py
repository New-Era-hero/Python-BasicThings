numero_magico = int(input("ingrese el numero magico: "))
numero_no_magico = int(input("adivina el numero magico:"))

while numero_magico != numero_no_magico:
    if numero_magico > numero_no_magico:
        numero_no_magico = int(input("fallaste, intenta con un numero mas grande "))
    else:
        numero_no_magico = int(input("no adivinaste, intenta con un numero mas pequeño "))
    
print ("increible has acertado")
        
