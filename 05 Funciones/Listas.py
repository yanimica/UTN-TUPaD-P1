
""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range. """


""" multiplos = []

for i in range (1, 101):
   if i % 4 == 0:
      multiplos.append(i)


print (multiplos) """


""" 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos! """


""" elementos = ["mate", "bombilla", "yerba", "agua"]

print(elementos[-2]) """


""" 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = [] """


""" lista_vacia = []

lista_vacia.append("arbol")
lista_vacia.append("tierra")
lista_vacia.append("rama")

print(lista_vacia) """


""" 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"] """


""" animales = ["perro", "gato", "conejo", "tortuga"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales) """



""" 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. """

""" numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

Entiendo que saca al mayor número en este caso """


""" 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros. """


""" lista = list(range(10, 31, 5))
print(lista[:2]) """


""" 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
 """


""" autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "duna"
autos[2] = "megane"

print(autos) """


""" 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla. """

""" dobles = []

dobles.append(10)
dobles.append(20)
dobles.append(30)

print(dobles) """


""" 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
 """


""" compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)
 """


""" 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
 """


""" lista_anidada = [[15, "true"], [25.5, 57.9, 30.6], ["false"]]

print(lista_anidada) """