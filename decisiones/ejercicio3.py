# Para encarar este ejercicio es muy importante que entiendas de Matrices
# Te dejo un elace a wikipedia para que puedas entender mejor el concepto
# https://es.wikipedia.org/wiki/Matriz_(matem%C3%A1ticas)

# En grandes rasgos podes pensarlo como una lista de listas

# [[1, 2, 3], 
#  [4, 5, 6], 
#  [7, 8, 9]]

# Donde las posiciones de la matriz equivalen a las posiciones de los vectores
# por ejemplo: matriz[0][0] = 1, matriz[0][1] = 2, matriz[1][0] = 4, matriz[1][1] = 5

# Te dejo otro ejemplo para que lo entiendas un poco mejor
# Pensa en cuando jugabas al TaTeTi, cada casilla era una posición de la matriz

# [[X, O, X],
#  [O, X, O],
#  [X, O, X]]

# En este caso la matriz es de 3x3, es decir 3 filas y 3 columnas
# Si te fijas en la posición matriz[0][0] = X, matriz[0][1] = O, matriz[1][0] = O, matriz[1][1] = X

# Ahora que entendemos que es una matriz, te preguntaras que es una "matriz identidad"
# Pensalo como una matriz que tiene 1 en la diagonal principal y 0 en el resto de las posiciones
# Por ejemplo para una matriz de 3x3:

# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]

# Y un detalle muy importante es que las matrices identidad son cuadradas, 
# es decir que la cantidad de filas es igual a la cantidad de columnas

# Ahora si, vamos al ejercicio

# Ejercicio 4.3. Escribir una función que reciba por parámetro una dimensión n, e imprima la
# matriz identidad correspondiente a esa dimensión.

def matriz_identidad(n):
    pass

assert matriz_identidad(1) == [[1]]
assert matriz_identidad(2) == [[1, 0], [0, 1]]
assert matriz_identidad(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]