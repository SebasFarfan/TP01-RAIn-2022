import ast

print('-'*60)
# tamaño del indice
limite=184
# se crea un diccionario
resumenInv={}
# se abre y lee el fichero invertido ResumenInvertido.txt en modo lectura
leerResumenInvertido=open('indiceInv.txt','r',encoding='UTF-8')
palabras=leerResumenInvertido.read()
leerResumenInvertido.close()

# se pasa texto del archivo original como diccionario de forma literal, 
# clave = palabra ; valor = indice
resumenInv=ast.literal_eval(palabras)
print('\n********* Diccionario de Indice Invertido Original *********\n')
print(resumenInv)
print('-'*60)

# se guarda la cantidad de elementos del diccionario como una lista [0-183]
listaFinal=list(range(0,limite))

print('-'*60)

# se recorre el diccionario y se agrega la clave 
# del mismo en la posicion segun indice a lista_final
for palabra, listaPosicion in resumenInv.items():
    for i in listaPosicion:
        listaFinal[i]=palabra

# Cada elemento de la lista se convierte primero en un str, 
# luego todo se combina en una línea usando el método de join.
mensaje=' '.join(str(item) for item in listaFinal)

print('***** Mensaje reconstruido  *****','\n')
# se muestra mensaje reconstruido
print(mensaje,"\n")

# se escribe en archivo txt el mensaje reconstruido
escribeResumen=open('mensajeExtraido.txt', 'w')
escribeResumen.write(mensaje)
escribeResumen.close()
print('\nPuede visualizar el contenido del Resumen Ordenado abriendo el Archivo --> mensajeExtraido.txt')

