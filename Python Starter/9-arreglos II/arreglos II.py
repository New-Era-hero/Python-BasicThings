frutas = ["manzana", "mango", "uva", "sandia", 1, 2]

#append -> agregar un elemento al arreglo
frutas.append("fresa")

#insert -> recive 2 instrucciones, una es elemento y extra
frutas.insert(0,"naranja")

#extend -> agrega una lista sobre otra
lenguajes_prog = ["C", "C++", "C#", "python", "javascript", "java", "unity"]
lenguajes_prog.extend(frutas)

#remove -> elimina elemnentos de un arreglo
lenguajes_prog.remove("unity")
frutas.remove(1)

#pop -> elimina un elemento dada su posicion
frutas.pop(5)

print (frutas)
