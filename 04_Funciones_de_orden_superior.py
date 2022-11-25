# Funciones de orden superior
''''¡¡¡¡Este archivo contiene errores¡¡¡¡'''
'''Son funciones que hacen cosas con funciones dentro'''
# Closures

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print (add_closure(5))

# Built-in

# Map
numeros = [2,5,10,21]

def multiplicar():
    return numeros * 2

map(multiplicar, numeros)
print (map(multiplicar(), numeros))


# Filter
def filter_greater_ten(number):
    if number > 10:
        return True
    else:
        False

filter(filter_greater_ten, numeros)
print (list(filter(filter_greater_ten(numeros))))

# Reduce
