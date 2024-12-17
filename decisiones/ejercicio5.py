# Ojo con este caso que es bastante complejo
# Estate muy atento de como y cuando vas a aplicar cada uno de los operadores
# Hace caso a la Nota del final, si ya calculaste una funcion que te puede servir para el ejercicio siguiente
# no dudes en usarla, no es necesario que la vuelvas a escribir.

# Ejercicio 4.5. Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
# excepto que también sea divisible por 400.
# b) Dado un mes y un año, devolver la cantidad de días correspondientes.
# c) Dada una fecha (día, mes, año), indicar si es válida o no.
# d) Dada una fecha, indicar los días que faltan hasta fin de mes.
# e) Dada una fecha, indicar los días que faltan hasta fin de año.
# Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.

def es_bisiesto(year):
    pass

def dias_mes(month, year):
    pass

def fecha_valida(day, month, year):
    pass

def dias_fin_mes(day, month, year):
    pass

def dias_fin_year(day, month, year):
    pass

assert es_bisiesto(2000) == True
assert es_bisiesto(1900) == False
assert dias_mes(2, 2000) == 29
assert dias_mes(2, 1900) == 28
assert fecha_valida(29, 2, 2000) == True
assert fecha_valida(29, 2, 1900) == False
assert dias_fin_mes(11, 5, 2021) == 20
assert dias_fin_year(11, 5, 2021) == 234
