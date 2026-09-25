# EJERCICIO 1
# Elementos qde A o en B, o en ambos.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union = A.union(B)


print("====================================")
print("EJERCICIO 1 - UNION")
print("====================================")
print("Conjunto A:", A)
print("Conjunto B:", B)
print("Elementos que estan en A o en B, o en ambos:")
print(union)


# EJERCICIO 2

# Elementos que estan en A y en B.

interseccion = A.intersection(B)

print("\n====================================")
print("EJERCICIO 2 - INTERSECCION")
print("====================================")
print("Conjunto A:", A)
print("Conjunto B:", B)
print("Elementos que estan en A y en B:")
print(interseccion)



# EJERCICIO 3
# Elementos que se encuentran en A o en B,
# pero no en los dos.l

diferencia_simetrica = A.symmetric_difference(B)

print("\n====================================")
print("EJERCICIO 3 - DIFERENCIA SIMETRICA")
print("====================================")
print("Conjunto A:", A)
print("Conjunto B:", B)
print("Elementos que estan en A o en B, pero no en ambos:")
print(diferencia_simetrica)





# EJERCICIO 4
# Comprobar si A es subconjunto de B.

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}


es_subconjunto = A.issubset(B)

print("\n====================================")
print("EJERCICIO 4 - SUBCONJUNTO")
print("====================================")
print("Conjunto A:", A)
print("Conjunto B:", B)

if es_subconjunto:
    print("El conjunto A es un subconjunto de B.")
else:
    print("El conjunto A no es un subconjunto de B.")


# EJERCICIO 5
# Mostrar el NUmero de elementos del conjunto A.

A = {1, 2, 3, 4, 5}

cantidad = len(A)

print("\n====================================")
print("EJERCICIO 5 - CANTIDAD DE ELEMENTOS")
print("====================================")
print("Conjunto A:", A)
print("El numero de elementos del conjunto A es:", cantidad)