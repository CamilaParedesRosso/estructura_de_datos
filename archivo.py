import os

print ("\nCrear un archivo")
print ("================")

NOMBRE_ARCHIVO = 'archivo.txt'#Se guarda en la donde se guarda el codigo

archivo = open(NOMBRE_ARCHIVO, 'w') # abre el archivo datos.txt
archivo.write('Bajo el cielo más puro de América \nY en la tierra de Ñuflo de Chávez \nLibertad van trinando las aves \nDe sureste ostentando el primor.')
archivo.close()

if NOMBRE_ARCHIVO in os.listdir("."):#. el archivo actual, .. el archivo superior
    print ("\nArchivo creado en la ruta: \n\n\t{0}/{1}".format(os.getcwd(), NOMBRE_ARCHIVO))
else:
    print ("El archivo no fue creado!!!\n")


print ("\n\nLeer un archivo")
print ("===============\n")

archivo = open(NOMBRE_ARCHIVO, 'r')
contenido = archivo.read()
print (contenido)
archivo.close()

print ("\n\nIterar sobre un archivo")
print ("=======================\n")

archivo = open(NOMBRE_ARCHIVO, 'r')
for linea in archivo:
    print (linea)
print ("\n")
archivo.close()

print ("\nEliminar un archivo")
print ("===================")

os.remove(os.getcwd()+"/"+NOMBRE_ARCHIVO)
print ("\nEliminado archivo desde la ruta: \n\n\t{0}/{1}".format(os.getcwd(), NOMBRE_ARCHIVO))