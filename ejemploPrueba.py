import os
from collections import defaultdict
from nltk.corpus import stopwords
import nltk
import string
import operator


contenido = os.listdir()
print(contenido)
archivos_pdf=[]
for archivo in contenido:
    if archivo.endswith('.pdf'):
        archivos_pdf.append(archivo)

print(archivos_pdf)

palabra='hola sebastian estas\ncon julieta \n'
lista=palabra.split()
print(lista)

lista1=['Sebas', 'Carlos', 'Julieta', 'Romina']
lista2=['Maria', 'Soledad', 'Carina', 'Valeria', 'Sebas']
lista3=['hola','que','tal','has','de','jugar', 'http://www.youtube.com', 'georgina, analia y sofia']

print(string.punctuation)


for palabra in lista1:
    print(palabra.lower())
lista3Limpia=[]
for palabra in lista3: 
    if palabra not in stopwords.words('spanish'):
        lista3Limpia.append(palabra)
# lista3Limpia=[palabra for palabra in lista3 if palabra not in stopwords.words('spanish')] 
print(lista3Limpia)
lista3LimpiaPuntuacion=[]
for palabra in lista3Limpia:
    for letra in palabra:
        if letra in string.punctuation:
            palabra=palabra.replace(letra, '')
    lista3LimpiaPuntuacion.append(palabra)
print(lista3LimpiaPuntuacion)

listaprincipal=[]
listaprincipal.append(lista1)
listaprincipal.append(lista2)
print(str(listaprincipal))
# no funciona con elementos tipos listas solo si los elementos de la lista no es lista
# temp=defaultdict(lambda:len(temp))
# res=[temp[elemento] for elemento in listaprincipal]
# print(str(res))


listaDefinitiva=[]
identificador=0
for lista in listaprincipal:
    listaConIdentificador=[]
    identificador=identificador+1
    listaConIdentificador.append(identificador)
    listaConIdentificador.append(lista)
    listaDefinitiva.append(listaConIdentificador)
print(str(listaDefinitiva))

# ---------------------------------------------------------------------
lista4=['sebas', 'julieta', 'sebas', 'sebas', 'julieta', 'analia']
print(lista4[0])
frecuencias1=nltk.FreqDist(lista4)
print(frecuencias1.items())
frecuencias2=[]
for palabra in lista4:
    frecuencias2.append(lista4.count(palabra))

print('-------------a-----------------------------a------------')
print(str(list(zip(lista4,frecuencias2))))
listadoFrec=list(set(list(zip(lista4,frecuencias2))))
print(listadoFrec)
for elemento in listadoFrec:
    print(elemento[0], elemento[1])




lista5=[['1',['sebas','analia', 'sebas', 'gabriela']],['2',['sebas', 'lorena', 'claudia']]]
for elemento in lista5:
    # print(len(elemento))
    # for i in range(0, len(elemento)):
    #     print(elemento[i])
    print(elemento[0], elemento[1])

print(lista5[0][1])
diccionario={}
listaCompleta=[]
# con lista
for elementos in lista5:
    listaSinRepeticion=[]
    listaSinRepeticion.append(elementos[0])    
    listaPalabras=list(set(elementos[1]))
    listaSinRepeticion.append(listaPalabras)
    listaCompleta.append(listaSinRepeticion)
print(listaCompleta)
# con diccionario

print('------------diccionarios--------------')
for elementos in lista5:
    listasinrepeticion=list(set(elementos[1]))
    diccionario[elementos[0]]=listasinrepeticion
print(diccionario)

print(diccionario.keys())
print(diccionario.values())

documento=diccionario.keys()
print(list(documento))
for doc in documento:
    print(doc)

dicpalabras=diccionario.values()
print(list(dicpalabras))
for c in dicpalabras:
    print(c)

listadoPalabras=[]
# print(list(lista5[1][1]+lista5[0][1]))
for conjunto in lista5:
    for palabras in conjunto[1]:
        listadoPalabras.append(palabras)
print (listadoPalabras)
listadoDef=list(set(listadoPalabras))
print(listadoDef)

# listado de frecuencias
print('---------listado de frecuancias--------------')
listadoFrec11=[]
for listaPal in lista5:
    # print(listaPal[1])
    listaIdPalabra=[]
    listaPalabras=[]
    for pal in listaPal[1]:
        listaPalabras.append(listaPal[1].count(pal))
    listaIdPalabra.append(listaPal[0])
    listadoFrecc=list(set(list(zip(listaPal[1],listaPalabras))))
    listaIdPalabra.append(listadoFrecc)
    listadoFrec11.append(listaIdPalabra)
print(listadoFrec11) # lista de listado id palabra-frec

# for elemento in listadoFrec11:
#     for tup in elemento[1]:
#         print(tup[0])


listaIdDocDicCompleta=[]
print('-----------q--------g------------r----')
for elemento in listadoFrec11:
    listaIdDocDic=[]
    i=0
    diccPalabbraPos={}
    listaIdDocDic.append(elemento[0])
    for tup in elemento[1]:
        # print(tup[0], 'posicion', i)
        diccPalabbraPos[tup[0]]=i
        i+=1
    listaIdDocDic.append(diccPalabbraPos)
    listaIdDocDicCompleta.append(listaIdDocDic)
print(listaIdDocDicCompleta)
# print(listadoFrec11[1][1][0])

print('posicion de la palabra sebas en el doc 1 ',listaIdDocDicCompleta[0][1]['sebas'])


print('------ listar los elementos y indexaxion')
for palabra in listadoDef:
    listaPalabraDocumentoFrec=[]
    listaPalabraDocumentoFrec.append(palabra)
    for elemento in lista5:
        if palabra in elemento[1]:
            listaDocPalFrec=[]
            # print('el elemento:{} esta en el arreglo{}'.format(palabra, elemento[0]))
            doc='doc'+elemento[0]
            listaDocPalFrec.append(doc)
            # listaPalabraDocumentoFrec.append(doc)
            posDoc=int(elemento[0])-1
            # print(posDoc)
            pos=listaIdDocDicCompleta[posDoc][1][palabra]
            frec=listadoFrec11[int(elemento[0])-1][1][pos] # el primer indice se resta para obtener la posicion 
            listaDocPalFrec.append('frec:'+str(frec[1]))
            # listaPalabraDocumentoFrec.append('frec:'+str(frec[1]))
            listaPalabraDocumentoFrec.append(listaDocPalFrec)

            
    print(listaPalabraDocumentoFrec)



# for elemento in listadoDef:
    
        

