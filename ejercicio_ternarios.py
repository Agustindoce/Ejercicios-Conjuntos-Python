# Calcular el mayor de dos numeros con operador ternario

print("EJERCICIO 1 - NUMERO MAYOR")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

mayor = numero1 if numero1 > numero2 else numero2

print("El numero mayor es:", mayor)

print("--------------------------------")





# Buscar una palabra en una lista usando args y ternario

print("EJERCICIO 2 - BUSCAR PALABRA")

def buscar_palabra(palabra, *args):
    resultado = "La palabra esta en la lista" if palabra in args else "La palabra no esta en la lista"
    print(resultado)


palabras = input("Ingrese varias palabras separadas por espacios: ").split()
buscar = input("Ingrese la palabra que quiere buscar: ")

buscar_palabra(buscar, *palabras)

print("--------------------------------")





# Determinar si un numero es par o impar

print("EJERCICIO 3 - PAR O IMPAR")

numero = int(input("Ingrese un numero: "))

resultado = "El numero es par" if numero % 2 == 0 else "El numero es impar"

print(resultado)

print("--------------------------------")




# Calcular promedio usando args y operador ternario

print("EJERCICIO 4 - PROMEDIO")

def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else 0
    return promedio


numeros = input("Ingrese numeros separados por espacios: ").split()

lista_numeros = []

for numero in numeros:
    lista_numeros.append(float(numero))

resultado = calcular_promedio(*lista_numeros)

print("El promedio es:", resultado)

print("--------------------------------")





# Mostrar un error si no se pasan suficientes argumentos

print("EJERCICIO 5 - CANTIDAD DE ARGUMENTOS")

def sumar_numeros(*args):
    if len(args) < 2:
        print("Error: debe ingresar al menos dos numeros.")
    else:
        resultado = sum(args)
        print("La suma es:", resultado)


numeros = input("Ingrese numeros separados por espacios: ").split()

lista_numeros = []

for numero in numeros:
    lista_numeros.append(float(numero))

sumar_numeros(*lista_numeros)

print("Fin de los ejercicios.")
