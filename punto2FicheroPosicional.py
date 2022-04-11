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

# función que genera una lista cuyos elementos son listas
# que contienen id del documento y un diccionario de palabras:[indices]
def listadoResumen(lista):
    listaIdPalabraPosiciones=[]
    for elemento in lista:
        listaElem=[]
        listaElem.append(elemento[0])
        dicPalDoc={}
        listaSinRepeticion=list(set(elemento[1]))
        dicPal={}
        for palabra in listaSinRepeticion:
            listaPos=[]
            for i in range(len(elemento[1])):
                if palabra==elemento[1][i]:
                    listaPos.append(i)
            dicPal[palabra]=listaPos
        listaElem.append(dicPal)
        listaIdPalabraPosiciones.append(listaElem)
    return listaIdPalabraPosiciones

# función que busca un termino y
# retorna una lista con las posiciones del termino
def buscarTermino(termino, listaRes):
    listaPosicional=[]
    for documento in listaRes:
        listaDoc=[]
        if termino in documento[1]:            
            listaDoc.append(documento[0])
            listaDoc.append(documento[1][termino])
        listaPosicional.append(listaDoc)    
    return listaPosicional


# funcion que muestra un string con la informacion del termino buscado y su 
# ubicación en los documentos. 'termino:    Doc[i]->[pos,pos..]  Doc[j]->[pos,pos,..] ..'
# parametro: termino, termino buscado
# parametro: lista
# retorna una string
def mostrarDato(termino, lista):
    infoSalida=termino+':   '
    cont=0
    for elemento in lista:
        if len(elemento)==0:
            cont+=0
        else:
            cont+=1
            infoSalida+='Doc'+str(elemento[0])
            infoSalida+='->'+str(elemento[1])+'  '
    if cont==0:
        infoSalida+='Termino inexistente'
    return infoSalida

#--------------------- menú principal ----------------------------
listaResumida=listadoResumen(extraerContenidoArchivo(buscaDocumentos()))
terminoBuscar=''
cont=1
print('****** Consultas ******')
while cont<=4:
    print('-'*6+' Consulta '+str(cont)+' -'*6)
    cont+=1
    terminoBuscar=input('--Ingrese palabra a buscar en fichero invertido posicional:')
    terminoBuscar=terminoBuscar.lower()
    listaDocPos=buscarTermino(terminoBuscar,listaResumida)
    salida=mostrarDato(terminoBuscar,listaDocPos)
    print(salida)
    print('-'*60)
print('-'*60)
print('\n--------------- Se realizó '+str(cont-1)+' consultas-----------------')
print('-'*60)