# Aca capaz te interese ver el EJERCICIO1 que puede ser que tenga algo que te sirva.

# Ejercicio 4.6. Suponiendo que el primer día del año fue lunes, escribir una función que reciba
# un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
# si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.

def dia_semana(dia):
    pass

assert dia_semana(3) == 'miércoles'
assert dia_semana(9) == 'martes'
assert dia_semana(1) == 'lunes'
assert dia_semana(366) == 'sábado'
assert dia_semana(100) == 'viernes'
assert dia_semana(200) == 'miércoles'
assert dia_semana(300) == 'domingo'
assert dia_semana(50) == 'sábado'