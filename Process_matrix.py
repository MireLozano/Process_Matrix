import numpy


#----------------------------------------------------------------#

def calculo_matriz2(i,j,matriz1):
    valor=matriz1[i][j]
    promedio=valor
    cuenta=1 
    if i !=0:
        i_sup=i-1 
        j_sup=j
        valor_sup=matriz1[i_sup][j_sup]
        promedio=valor_sup+promedio
        cuenta=cuenta + 1 
    if i !=(len(matriz1)-1):
        i_inf=i + 1 
        j_inf=j
        valor_inf=matriz1[i_inf][j_inf]
        promedio=valor_inf+promedio 
        cuenta=cuenta + 1 
    if j !=len(matriz1[i])-1:
        i_dcha=i 
        j_dcha=j+1 
        valor_dcha=matriz1[i_dcha][j_dcha]
        promedio=valor_dcha+promedio
        cuenta=cuenta+1 
    if j !=0:
        i_izq=i
        j_izq=j-1
        valor_izq=matriz1[i_izq][j_izq]
        promedio=valor_izq+promedio
        cuenta=cuenta+1 
    return round((promedio/cuenta),2)

#----------------------------------------------------------------#

def process_matriz(matriz1):
    lista_matriz=[]
    for i in range(len(matriz1)):
        i_lista=[]
        for j in range(len(matriz1[i])):
            element_lista=calculo_matriz2(i,j,matriz1)
            i_lista.append(element_lista)
        lista_matriz.append(i_lista)
    return lista_matriz


filas=int(input('Introduce numero de filas ➡️   '))
columnas=int(input('Introduce numero de columnas ➡️   '))

matriz1=numpy.random.random_integers(0,50,(filas,columnas))
print(matriz1)


#-------------------------------------------------------------------#

def ver_matriz(matriz1):
    a= ''
    for fila in range(len(matriz1)):
        for columna in range(len(matriz1[-1])):
            a+=str(matriz1[fila][columna])+ '\t' 
        a+= '\n'
    print('matriz1 ➡️   ' '\n' '\n' + a)
    ver_process_matriz = process_matriz(matriz1)
    b= ''
    for fila in range(len(ver_process_matriz)):
        for columna in range(len(ver_process_matriz[-1])):
            b+=str(ver_process_matriz[fila][columna])+ '\t' 
        b+= '\n'   
    print('matriz2 ➡️   ' '\n' '\n'+b)
ver_matriz(matriz1)