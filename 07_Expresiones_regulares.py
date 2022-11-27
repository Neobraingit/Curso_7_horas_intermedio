# Esxtresiones regulares

import re

texto = 'Me gusta el chocolate con nata pero mis gatas son unas pesadas'

resultado = re.search('Me gusta', texto) # Solamente la primera aparición

if resultado != None:
    print ('Búsqueda exitosa')
    print (resultado)
else:
    print ('No se encontró el patrón buscado')

# Findall

resultado = re.findall('son', texto) # Nos busca todas las apariciones
if resultado != None:
    print ('Búsqueda exitosa')
    print (resultado)
else:
    print ('No se encontró el patrón buscado')

resultado = re.findall('perro', texto)
if resultado != None:
    print ('Búsqueda exitosa')
    print (resultado)
else:
    print ('No se encontró el patrón buscado')

# Acento circunflejo

import re

texto = 'Me llamo Marcos Carmona'
print (re.search('^Me', texto))

# Signo $
for frase in texto:
    if re.search('es$', frase): # El signo $ nos indica que frases terminan con el string pasado
        print (frase)

# Utilización de los []












