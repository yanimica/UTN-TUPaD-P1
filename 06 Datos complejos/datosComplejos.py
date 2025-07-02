# Ejercicio 1
precios = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450}
precios['Naranja'] = 1200
precios['Manzana'] = 1500
precios['Pera'] = 2300
print('Ejercicio 1:', precios)


# Ejercicio 2
if 'Banana' in precios:
    precios['Banana'] = 1330
if 'Manzana' in precios:
    precios['Manzana'] = 1700
if 'Melón' in precios:
    precios['Melón'] = 2800
print('Ejercicio 2:', precios)


# Ejercicio 3
frutas = []
for fruta in precios:
    frutas.append(fruta)
print('Ejercicio 3:', frutas)


# Ejercicio 4
contactos = {}
for i in range(5):
    nombre = input('Nombre del contacto: ')
    numero = input('Número telefónico: ')
    contactos[nombre] = numero
busqueda = input('Buscar contacto: ')
print('Número:', contactos.get(busqueda, 'No encontrado'))


# Ejercicio 5
frase = input('Ingrese una frase: ')
palabras = frase.split()
unicas = []
for palabra in palabras:
    if palabra not in unicas:
        unicas.append(palabra)
print('Palabras únicas:', unicas)
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print('Conteo:', conteo)


# Ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input('Nombre del alumno: ')
    notas = []
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    notas.append(float(input('Nota 3: ')))
    alumnos[nombre] = notas
for nombre in alumnos:
    suma = 0
    for nota in alumnos[nombre]:
        suma += nota
    promedio = suma / 3
    print(nombre, 'Promedio:', promedio)


# Ejercicio 7
num1 = int(input('Cantidad aprobados P1: '))
alum1 = []
for i in range(num1):
    alum1.append(input('Nombre P1: '))
num2 = int(input('Cantidad aprobados P2: '))
alum2 = []
for i in range(num2):
    alum2.append(input('Nombre P2: '))
set1 = set(alum1)
set2 = set(alum2)
print('Aprobados ambos parciales:', set1 & set2)
print('Solo uno de los parciales:', set1 ^ set2)
print('Al menos uno:', set1 | set2)


# Ejercicio 8
stock = {}
while True:
    accion = input('Acción (consultar/agregar/salir): ')
    if accion == 'salir':
        break
    prod = input('Producto: ')
    if accion == 'consultar':
        print(stock.get(prod, 'No existe'))
    elif accion == 'agregar':
        cant = int(input('Cantidad a agregar: '))
        if prod in stock:
            stock[prod] += cant
        else:
            stock[prod] = cant
        print('Stock de', prod, ':', stock[prod])
    else:
        print('Opción no válida')


# Ejercicio 9
agenda = {('Lunes','10:00'): 'Reunión', ('Martes','14:00'): 'Clase'}
dia = input('Día: ')
hora = input('Hora (HH:MM): ')
if (dia, hora) in agenda:
    print('Actividad:', agenda[(dia, hora)])
else:
    print('No hay actividad')


# Ejercicio 10
paises = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}
invertido = {}
for pais in paises:
    ciudad = paises[pais]
    invertido[ciudad] = pais
print('Diccionario invertido:', invertido)
