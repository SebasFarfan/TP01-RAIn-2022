# generar un diccionario cuyo clave es un valor tipo diccionario

listaElemento=[['1',['sebas', 'cursa','rain','tambien','cursa','pvisual']],['2',['juan','cursa','ingles']]]

# crear un diccionario cuyo clave es el nro doc y su valor es una lista con sus palabras.
# diccionario={}
# for elemento in listaElemento:
#     # print(len(elemento))
#     # print('id:'+elemento[0])
#     # print('contendio:'+str(elemento[1]))
#     tup=tuple(elemento[1])    
#     diccionario[elemento[0]]=elemento[1]
# print(diccionario)

listaIdPalabraPosiciones=[]
for elemento in listaElemento:
    listaElem=[]
    listaElem.append(elemento[0]) # se almancena el id del doc
    dicPalDoc={}    
    listaSinRepeticion=list(set(elemento[1]))
    dicPal={}
    for palabra in listaSinRepeticion:
        listaPos=[]
        for i in range(len(elemento[1])):
            if palabra==elemento[1][i]:
                listaPos.append(i)
        dicPal[palabra]=listaPos
    # print(dicPal)
    listaElem.append(dicPal)
    listaIdPalabraPosiciones.append(listaElem)  # lista cuyos elementos [[id,{palabra:[1,3],..}],[id,{palabra:[1],..}],.]
# print(listaIdPalabraPosiciones)

# print(listaIdPalabraPosiciones[0][0]+' '+str(listaIdPalabraPosiciones[0][1].keys()))
palabraBuscar='cursa'
# print(listaIdPalabraPosiciones[0][1][palabraBuscar])
# print(diccionario)
# print(listaIdPalabraPosiciones[0][1])
# for elemento in listaIdPalabraPosiciones[0][1]:
#     print(elemento)

# if 'analia' in listaIdPalabraPosiciones[0][1]:
#     print('la palabra:{} esta en doc{} sus indices {}'.format('sebas',listaIdPalabraPosiciones[0][0],listaIdPalabraPosiciones[0][1]['sebas']))
# else:
#     print('no existe')
listaPoscional=[]
print(len(listaPoscional))
for documento in listaIdPalabraPosiciones:
    # print(documento)
    if palabraBuscar in documento[1]:
        # print(documento[1][palabraBuscar])
        listaDoc=[]
        listaDoc.append(documento[0])
        listaDoc.append(documento[1][palabraBuscar])
    listaPoscional.append(listaDoc)
# print(palabraBuscar,' ',str(listaPoscional))


            
    
    # for i in range(5):
    #     print(i)





# listaPalabrasPosicion=[]
# for elemento in listaElemento:
    

#     for item in elemento[1]:



        

