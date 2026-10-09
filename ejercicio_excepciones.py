# Dividir dos numeros y controlar la division por cero

print("EJERCICIO 1 - DIVISION POR CERO")

try:
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))

    resultado = numero1 / numero2
    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

print("--------------------------------")





# Intentar sumar un numero con una cadena de texto

print("EJERCICIO 2 - ERROR DE TIPO")

numero = 10
texto = "Hola"

try:
    resultado = numero + texto
    print(resultado)

except TypeError:
    print("Error: no se puede sumar un numero con un texto.")

print("--------------------------------")






# Buscar una clave que no existe en un diccionario

print("EJERCICIO 3 - ERROR DE CLAVE")

persona = {
    "nombre": "Agustin",
    "edad": 27
}

try:
    print(persona["apellido"])

except KeyError:
    print("Error: la clave no existe en el diccionario.")

print("--------------------------------")


# Abrir un archivo y crearlo si no existe

print("EJERCICIO 4 - ARCHIVO NO ENCONTRADO")

try:
    archivo = open("practica.txt", "r")
    print(archivo.read())
    archivo.close()

except FileNotFoundError:
    print("Error: el archivo no existe.")
    print("Se va a crear un archivo nuevo.")

    archivo = open("practica.txt", "w")
    archivo.write("Archivo creado desde Python.")
    archivo.close()

    print("El archivo fue creado correctamente.")

print("--------------------------------")


# Controlar division por cero y valores incorrectos

print("EJERCICIO 5 - VARIOS ERRORES")

try:
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))

    resultado = numero1 / numero2
    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

except ValueError:
    print("Error: debe ingresar numeros validos.")

print("Fin de los ejercicios de excepciones.")
