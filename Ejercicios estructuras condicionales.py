####Ejercicios Estructuras Condicionales:#####

#1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha ganado el sorteo!
"""
num=int (input("Por favor ingrese un número entero: "))

if num ==10:
    print ("Usted ha ganado el sorteo!") 
"""
#2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco, seguí participando! 
#Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!
"""
num=int (input("Por favor ingrese un número entero: "))

if num ==10:
    print ("Usted ha ganado el sorteo!") 
elif num <10:
    print ("¡Falto un poco, seguí participando!")
else: 
    print ("¡Te pasaste, a seguir intentando!")

"""
#3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, 
#otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
"""
dia= input("Por favor ingrese un día de la semana: ")
if dia =="lunes":
    print ("¡Hoy es el primer día de la semana!")
elif dia =="viernes":
    print ("¡Por fin llegó el gran día!")
elif dia =="sabado" or dia=="domingo":
    print ("¡Hoy es fin de semana, disfrtalo!")
else: 
    print ("Todavía falta para el viernes") 
"""
#4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.
"""
letra= input("Por favor ingrese una letra: ")

if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print ("Es vocal")

"""
####Ejercicios Estructuras Repetitivas:#####

#1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar hasta que se ingrese -1.
"""
suma = 0

while True:
    entrada = input("Ingrese un número (presione -1 para finalizar): ")

    if entrada == "-1":
        break
    else: 
        numero = int (entrada)
        suma += numero

print ("La suma de todos los numero es: ", suma)
"""

#2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
#El programa debe informar de cuantos números introducidos son mayores que
#0, menores que 0 e iguales a 0.
"""
cantidad_numeros = int(input("Por favor, ingrese la cantidad de números a introducir: ")) 

mayores_cero = 0
menores_cero  = 0
iguales_cero  = 0

for i in range (cantidad_numeros):
    numero = float(input(f"Ingrese un número {i + 1}: "))

    if numero > 0:
        mayores_cero  +=1
    elif numero < 0:
        menores_cero  +=1
    else: 
        iguales_cero  +=1

print ("Números mayores que 0: ", mayores_cero)
print ("Números menores que 0: ", menores_cero)
print ("Números iguales a 0: ", iguales_cero)

"""
#3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un cero.
"""
while True:

    letra = input("Ingrese una letra (presione 0 para salir): ")

    if letra == "0":
            break
    if letra.lower() in ["a", "e", "i", "o", "u"]:
        print ("VOCAL")
    else:
         print ("NO VOCAL")
"""
#4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
total_suma = 0
cant_numeros = 0
while True:
    numero = float(input("Por favor ingrese un número (Presione 0 para finalizar): "))
     
    if numero == 0:
        break

    total_suma += numero
    cant_numeros +=1
if cant_numeros >0:   
    media = total_suma/cant_numeros

    print ("La suma de todos los números es: ", total_suma)
    print ("La media de todos los números es: ", media)
else: 
    print ("No se ingresaron números")

    