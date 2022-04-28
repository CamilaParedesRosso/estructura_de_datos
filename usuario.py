import os

print ("\nCrear un archivo")
print ("================")

NOMBRE_ARCHIVO = 'usuario.txt'#Se guarda en la donde se guarda el codigo

archivo = open(NOMBRE_ARCHIVO, 'w') # abre el archivo datos.txt
archivo.write('Camila \tasdf1234 \tcamila@gmail.com \t14/11\n')
archivo.write('Daniela\tghjk5678\tdaniela@gmail.com\t10/04\n')
archivo.write('Diego \trtyu9123 \tdiego@gmail.com \t05/10\n')
archivo.write('Mario \tzxcv4567 \tmario@gmail.com \t24/01\n')
archivo.write('Carla \tbnmv8912 \tcarla@gmail.com \t31/10\n')
archivo.close()

print ("\n\nLeer un archivo")
print ("===============\n")

archivo = open(NOMBRE_ARCHIVO, 'r')
contenido = archivo.read()
print (contenido)
archivo.close()