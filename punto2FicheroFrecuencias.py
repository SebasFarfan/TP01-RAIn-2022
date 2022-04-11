# usamos la libreria PyPDF2 para extraer texto de un archivo pdf
import PyPDF2
import string
import os
from nltk.corpus import stopwords

# función que busca los documentos a procesar
# retorna una lista con los nombres de los archivos pdf.
def buscaDocumentos():
    listaArchivos=[]
    contenido=os.listdir()
    for archivo in contenido:
        if archivo.endswith('pdf'):
            listaArchivos.append(archivo)
    
    return listaArchivos

# funcion que pone en minuscula todas las palabras de la lista
# retorna una lista
def pasarMinuscula(lista):
    listaMinuscula=[]
    for palabra in lista:
        listaMinuscula.append(palabra.lower())
    return listaMinuscula

# funcion que limpia la lista de stopwords
# retorna una lista
def limpiarStopword(lista):
    listaSinStopwords=[]
    for palabra in lista:
        if palabra not in stopwords.words('spanish'):
            listaSinStopwords.append(palabra)
    return listaSinStopwords

# funcion que limpia la lista de signos de puntuacion
# retorna una lista
def limpiarSignosPuntuacion(lista):
    listaSinSignosPuntuacion=[]
    for palabra in lista:
        for letra in palabra:
            if letra in string.punctuation:
                palabra=palabra.replace(letra, '')
        listaSinSignosPuntuacion.append(palabra)
    return listaSinSignosPuntuacion

# funcion que extrae contenido de los archivos los limpia y genera 
# una lista cuyos elementos son listas con los contenidos de los archivos.
def extraerContenidoArchivo(lista):
    listaContenidoArchivo=[]    
    for archivo in lista:
        # extraemos el archivo en modo binario y la almacenamos en un objeto
        pdfFileObj=open(archivo,'rb')
        # creamos un objeto lector de pdf 
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        # print('numeros de paginas ',pdfReader.numPages)
        contenido = ''
        # recorremos las paginas del objeto lector y extraemos el contenido 
        # del pdf y lo almacenamos en un string.
        for pagina in range(0,pdfReader.numPages):
            pdfObj=pdfReader.getPage(pagina)
            contenido += pdfObj.extractText()
        pdfFileObj.close()

        # print(contenido)
        # limpiamos el texto de espacios en blancos e interlineados
        textoLimpio=contenido.split()
        # print(textoLimpio)
        # ponemos en minuscula
        listaEnMinuscula=pasarMinuscula(textoLimpio)
        # eliminar stopwords
        listaSinStopWords=limpiarStopword(listaEnMinuscula)
        # eliminar signos de puntuacion
        listaSinSignosPuntuacion=limpiarSignosPuntuacion(listaSinStopWords)

        listaContenidoArchivo.append(listaSinSignosPuntuacion)
    # generamos la lista definitiva con sus correspondiente elemento identificador
    listaDefinitiva=[]
    identificador=0
    for lista in listaContenidoArchivo:
        listaConIdentificador=[]
        identificador+=1
        listaConIdentificador.append(identificador)
        listaConIdentificador.append(lista)
        listaDefinitiva.append(listaConIdentificador)
    return listaDefinitiva

# función que obtiene la frecuencias de las palabras de la lista
# retorna una lista con los elemento y su frecuencia
def obtenerFrecuenicas(lista):
    frecuencias=[]
    for palabra in lista:
        frecuencias.append(lista.count(palabra))    
    listado=list(set(list(zip(lista, frecuencias))))
    return listado

# funcion para listar las frecuencias por documentos
# retorna una lista, el la primera posicion contiene el id del documento
# y la segunda posicion contiene la lista de frecuencias 
def obtenerListadoFrecuencias(lista):
    listaFrecuencias=[]
    for listado in lista:
        listaFrec=[]
        listaFrec.append(listado[0])
        listaFrec.append(obtenerFrecuenicas(listado[1]))
        listaFrecuencias.append(listaFrec)
    return listaFrecuencias

# función para obtener listado completo de todas 
# las palabras de los documentos sin repetirlos
# retorna un listado
def obtenerlistadoPalabras(lista):
    listadoPalabras=[]
    for conjunto in lista:
        for palabras in conjunto[1]:
            listadoPalabras.append(palabras)
    return list(set(listadoPalabras))

# funcion que crea una lista que contiene un listado [[id, {palabra:pos,...}],[id,{palabra:pos,..}]]
# donde id es el id del documento y el diccionario contiene las posisciones de las palabras y sus frec
# retorna una lista
def obtenerListadoDocPalabraFrecPosicion(lista):
    listaIdDocDicCompleta=[]
    # lista: tiene que ser lista frecuencia [['1',[(),()]],['2',[(),()]]]
    print('cantidad de elementos:---',len(lista))
    for elemento in lista:
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
    return listaIdDocDicCompleta

print('------Listar los elementos e indexación--------')
listaDocumentos=buscaDocumentos()
# print(listaDocumentos)
listaDatos=extraerContenidoArchivo(listaDocumentos)
# print(listaDatos)
listadoFrec=obtenerListadoFrecuencias(listaDatos)
# print(listadoFrec) #[[1, [('cómo', 1), ('describir', 1), ('8', 1)..]],[2,[(),..]]]
listadoFinalPalabras=obtenerlistadoPalabras(listaDatos)
# print(listadoFinalPalabras) #['juan','carlos',..]
listadoPalFrecPos=obtenerListadoDocPalabraFrecPosicion(listadoFrec)
# print(listadoPalFrecPos)
# print(len(listadoFrec))
# print(len(listadoPalFrecPos))

for palabra in listadoFinalPalabras:
    listaPalabraDocumentoFrec=[]
    listaPalabraDocumentoFrec.append(palabra)
    for elemento in listaDatos:
        if palabra in elemento[1]:
            listaDocPalFrec=[]
            # print('el elemento:{} esta en el arreglo{}'.format(palabra, elemento[0]))
            doc='Doc'+str(elemento[0])
            listaDocPalFrec.append(doc)
            posDoc=int(elemento[0])-1
            pos=listadoPalFrecPos[posDoc][1][palabra]
            frec=listadoFrec[int(elemento[0])-1][1][pos]
            listaDocPalFrec.append('frec:'+str(frec[1]))
            listaPalabraDocumentoFrec.append(listaDocPalFrec)
    # print(listaPalabraDocumentoFrec)
    # print(str(listaPalabraDocumentoFrec))
    texto=''
    frecuencia=''
    for i in range(0,len(listaPalabraDocumentoFrec)):
        if i==0:
            texto+=listaPalabraDocumentoFrec[i]
        else:
            frecuencia+=listaPalabraDocumentoFrec[i][0]+'->'+listaPalabraDocumentoFrec[i][1]+' '
                
    print('{:<20}{:>30}'.format(texto,frecuencia))

