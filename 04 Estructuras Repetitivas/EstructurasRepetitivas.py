
""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
""" 


for i in range(0,101):

    print (i)


""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. """


numero = int(input("Por favor ingrese un numero entero"))
digitos = len(str(abs(numero)))
print ("El numero tiene", digitos)


""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

numero1 = int(input("Por favor ingrese un número: "))
numero2 = int(input("Por favor ingrese otro número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

suma = 0

for i in range(numero1 + 1, numero2):
    suma += i

print("La suma de los números entre", numero1, "y", numero2, "es:", suma)


"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.""" 

suma = 0

numero1 = int(input("Por favor ingrese un número entero: "))

while numero1 != 0:
    suma += numero1
    numero1 = int(input("Ingrese otro numero: "))

print("La suma total es:", suma)


"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.""" 


numeroAdivinar = 5
intentos = 0

numero1 = int(input("Indica un numero: "))

while numero1 != 5:
    numero1 = int(input("Indica otro numero: "))
    intentos += 1

print("Fueron necesarios ", intentos, "intentos")


"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
""" 

for i in range (100, -1, -1):
    if i % 2 == 0:
        print (i) 
        

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

suma = 0
numeroUsuario = int(input("Por favor ingrese un número positivo: "))

for i in range(0, numeroUsuario + 1):
    suma += i

print("La suma es", suma)


"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
""" 

numerosPares = 0
numerosImpares = 0
numerosNegativos = 0
numerosPositivos = 0

for i in range (100):
    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1


if numero < 0:
    numerosNegativos += 1
elif numero > 0:
    numerosPositivos += 1

print("Cantidad de números pares:", numerosPares)
print("Cantidad de números impares:", numerosImpares)
print("Cantidad de números negativos:", numerosNegativos)
print("Cantidad de números positivos:", numerosPositivos)


""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""


suma = 0

for i in range (100):
    numerosEnteros = int(input("Por favor igresar un nro entero: "))
    suma += numerosEnteros

media = suma / 100

print("la suma es: ", media)


""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """


numero = int(input("por favor ingresar un numero"))

numero_invertido = str(numero)[::-1]

print("El número invertido es:", numero_invertido)