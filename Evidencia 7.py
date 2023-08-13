#Ejercicios Listas:
#1)	Lista de nombres de familia
nombres_familia = ["Caliope", "Dante", "Carlos", "Miguela"]

#2)	Lista de temperaturas del mes
temperaturas_julio = [15.0, 12.3, 9.4, 5.1, 7.8, 9.2, 21.7, 14.9, 10.0, 8.9, 5.5, 0.1, 2.3, 5.5, 6.9, 7.2, 11.7, 13.6, 18.1, 10.9, 12.3, 17.0, 15.7, 9.2, 8.8, 6.3, 4.4, 8.1, 10.3, 16.7, 18.5]

#3)	Lista de Ciudades
ciudades =["Puerto Pirámides", "Punta Tombo", "Bariloche", "CABA", "Puerto Iguazú", "Villa Mercedes"]

#4)	Lista de Fechas y nombres de eventos importantes
eventos = ["Cumpleaños de Carlos", '10/01/1970', "Cumpleaños de Miguela", '15/03/1980', "Día de San Patricio", '17/03/2023', "Día del amigo", '20/07/2023', "Cumpleaños de Caliope", '03/09/1975', "Cumpleaños de Dante", '11/11/2010, “Navidad”, 25/12/2023', "Año Nuevo", '31/12/2023']

#Luego: 
# #1)	Ordenar alfabéticamente:
nombres_familia.sort()
print(nombres_familia)

#2)	Ordenar ascendentemente:
temperaturas_julio.sort()
print(temperaturas_julio)

#3)	Agregar las temperaturas:
temperaturas_julio.extend([16.0, 17.3, 9.2, 5.9, 8.8, 12.2, 21.5, 12.9, 10.4, 7.9, 9.5, 15.1, 12.3, 8.5, 6.4])

#4)	Quitar abuelos:
nombres_familia = ["Caliope", "Dante", "Carlos", "Miguela"]
del nombres_familia[2]
del nombres_familia[0]
print(nombres_familia)

#5)	Quitar Ciudades:
del ciudades [4]
del ciudades [3]
del ciudades [1]

#6)	Mostrar las listas:
print(nombres_familia)
print(temperaturas_julio)
print(ciudades)
print(eventos)

#Ejercicios Tuplas:
# -	Crear 3 tuplas con  datos random:
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
vocales = ('a', 'e', 'i', 'o', 'u')

#-	Crear una lista que las contenga y mostrarla:
lista_random = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'e', 'i', 'o', 'u']
print(lista_random)

#Ejercicio Diccionario:
# -	Crear un diccionario:

diccionario = {25123784: "Caliope", 50487652: "Dante", 31849756: "Miguela",}

#-	Añadir los datos de la familia ampliada:
diccionario [15345985] = "Isabel"
diccionario [5249781] = "Zulma"
diccionario [14875612] = "Roberto"
diccionario [6178546] = "Carlos"

#-	Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono

import random

def generar_numero():
    return f'{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}'

numeros_telefono = {}
cantidad_numeros = 10  

for i in range(cantidad_numeros):
    clave_autogenerada = f'cliente{i + 1}'
    numero_telefono = generar_numero()
    numeros_telefono[clave_autogenerada] = numero_telefono

print(numeros_telefono)









