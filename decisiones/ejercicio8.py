# De que signo es Justin? y vos? de que signo sos?

# Ejercicio 4.8. Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
# y el programa le debe decir a qué signo corresponde.
# Aries: 21 de marzo al 20 de abril. Tauro: 21 de abril al 20 de mayo.
# Geminis: 21 de mayo al 21 de junio. Cancer: 22 de junio al 23 de julio.
# Leo: 24 de julio al 23 de agosto. Virgo: 24 de agosto al 23 de septiembre.
# Libra: 24 de septiembre al 22 de octubre. Escorpio: 23 de octubre al 22 de noviembre.
# Sagitario: 23 de noviembre al 21 de diciembre. Capricornio: 22 de diciembre al 20 de enero.
# Acuario: 21 de enero al 19 de febrero. Piscis: 20 de febrero al 20 de marzo.

def decir_signo(dia, mes):
    pass

assert decir_signo(1, 1) == 'Capricornio'
assert decir_signo(1, 2) == 'Acuario'
assert decir_signo(1, 3) == 'Piscis'
assert decir_signo(1, 4) == 'Aries'
assert decir_signo(1, 5) == 'Tauro'
assert decir_signo(1, 6) == 'Geminis'
assert decir_signo(1, 7) == 'Cancer'
assert decir_signo(1, 8) == 'Leo'
assert decir_signo(1, 9) == 'Virgo'
assert decir_signo(1, 10) == 'Libra'
assert decir_signo(1, 11) == 'Escorpio'
assert decir_signo(1, 12) == 'Sagitario'
assert decir_signo(40, 3) == 'Fecha invalida'
assert decir_signo(1, 13) == 'Fecha invalida'