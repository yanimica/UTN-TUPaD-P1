""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal. """


""" def saludo ():
    print("Hola mundo")

saludo() """


""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario. """

""" 
def saludar_usuario (nombre):
    print("Hola" , nombre )

nombre = input("Como te llamas?")
saludar_usuario(nombre)
 """


""" 3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados. """


""" def informacion_personal(nombre,apellido,edad,residencia):
    print("Soy" , nombre , apellido , "tengo", edad, "años y vivo en" , residencia)

nombre = input ("Indique su nombre: ")
apellido = input ("Indique su apellido: ")
edad = input ("Indique su edad: ")
residencia = input ("Indique su residencia: ")

informacion_personal(nombre,apellido,edad,residencia) """


""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. """

""" import math 

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area


def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingresá el radio del círculo: "))


area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}") """



""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
 """

""" def segundos_a_horas(segundos):
    hora = segundos / 3600
    return hora

segundos = int(input("Ingrese por favor una cantidad de segundos: "))
resultado = segundos_a_horas(segundos)

print(f"{segundos} segundos son {resultado} horas.") """


""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función. """


""" def tabla_multiplicar(numero):
    for i in range (1, 11):
        print (numero)

numero = int(input("Ingrese un numero: "))
tabla_multiplicar (numero)

print("Tabla de multiplicar ", tabla_multiplicar)
 """


""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara. """

""" def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)
a = float(input("por favor indique un numero: "))
b = float(input("por favor indique OTRO numero: "))

resultados = operaciones_basicas(a, b)

print ("La suma es de: ", resultados [0])
print ("La resta es de: ", resultados [1])
print ("La multiplicacion es de: ", resultados [2])
print ("La division es de: ", resultados [3] ) """


""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales. """

""" def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Por fvaor indicar su peso: "))
altura = float(input("por favor indicar su altura: "))

resultado = calcular_imc (peso, altura)

print ("Su indice de masa corporal es de ", resultado)  """


""" 
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
 """

""" 
def celsius_a_fahrenheit(celsius):

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(celsius)


print("La temperatura en Fahrenheit es: {:.2f}".format(resultado))
 """

""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
 """

""" def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = int(input("Por fvaor indicar numero: "))
b = int(input("Por fvaor indicar numero: "))
c = int(input("Por fvaor indicar numero: "))

resultado = calcular_promedio(a, b, c)

print ("El promedio de los numeros ingresados es de: ", resultado)

 """