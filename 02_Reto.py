# Reto

'''
Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos inscluidos y con un salto de línea
entre cada impresión, sustituyendo los siguientes:
  --- Múltiplos de 3 por la palabra "fizz"
  --- Múltiplos de 5 por la palabra "buzz"
  --- Mñultiple de 3 y de 5 a la vez por la palabra "fizzbuz"
'''

def fizzbuzz():
    for i in range(1, 101):
        print (i)
        if i % 3 == 0 and i % 5 == 0:
            print ('fizzbuz')
        elif i % 3 == 0:
            print ('fizz')
        elif i % 5 == 0:
            print ('buz')

        else:
            print (i)



fizzbuzz()

'''
Escribe una función que reciba dos palabras y retorne verdadero o falso según sean o no anagramas.
   --- Un Anagrama consiste en formar una palabra reordenando todas las letras de la palabra original
   --- No hace falta comprobar que ambas palabras existan
   --- Dos palabras exactamente iguales no son un anagrama
'''

def anagrama(palabra1, palabra2):
    if palabra1.lower() == palabra2[::-1].lower():
        print ('Son iguales¡¡')
anagrama('amor', 'roma')

'''
Escribe un programa que impriman los 50 primeros números de la sucesión de Fibonacci enpezando en 0.
   --- La serie Fibonacci se compone por una sucesión de números en la que 
   el siguiente siempre es la suma de los dos anteriores
'''

def Fibonacci():
    prev = 0
    next = 1
    for i in range (0, 51):
        print (prev)
        fib = prev + next
        prev = next
        next = fib



Fibonacci()


