# Expresiones regulares

import re

my_string = 'Soy una cadena de texto para hacer los ejemplos...'
my_other_string = 'Esto es otra string'

match = re.match('Soy una cadena', my_string, re.I)
print (match)





print (re.match('hacer los ejemplos', my_string, re.I)) # Con esto sabemos si el string tiene esta porción de texto
print (re.match('Soy una cadena', my_other_string))


# Search
search = re.search('para hacer los ejercicios', my_string, re.I)
print (search)

# Findall

findall = re.findall('hacer los ejemplos...', my_string, re.I) # Nos busca lo indicado y nos devuelve una lista con el número de veces que aparece
print (findall)

# Split

split = re.split('\n', my_string)
print (split)

#Sub

sub = re.sub('Soy una cadena', 'Esto es una cadena guapa', my_string) # Nos sustituye una cosa por otra
print (sub)

# Búsqueda de caracteres

caracteres = r'[a-z]'
print (re.findall(caracteres, my_string))
print (re.search(caracteres, my_string))


