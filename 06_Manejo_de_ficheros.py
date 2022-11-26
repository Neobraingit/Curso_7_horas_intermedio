# Manejo de ficheros

# .txt file
import os
open('My_file.txt', 'w+')
txt_file = open('My_file.txt', 'r+') # Leer y escribir
txt_file.write('\nMi nombre es Marcos\n'
               'Mi apeellido es Carmona\n'
               'Mi edad es 47\n'
               'Mi lenguaje favorito es Python\n')
#print (txt_file.read(10))

# print (txt_file.readline()) # Lectura línea a línea
# print (txt_file.readline())


txt_file.write('Este es mi caballo')
print (txt_file.read())
txt_file.close()

import os
os.remove('My_file.txt')

# .jason file
import json
json_file = open('my_file.json', 'w+')

json.text = {
    'Nombre' : 'Marcos',
    'Apellido' : 'Carmona',
    'Edad' : 47
             }
json.dump(json.text, json_file, indent = 4)

# csv.file
import csv
csv_file = open('my_csv.csv', 'w+')




