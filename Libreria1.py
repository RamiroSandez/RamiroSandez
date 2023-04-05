def ingresoCodigo ( li, ls,  condicionCorte):
    codigo=int(input("Ingrese el codigo del producto (1-20)-->"))
    while not(validaRango(codigo,1,20)) and (codigo!=condicionCorte):
         codigo=int(input("Ingrese el codigo del producto (1-20)-->"))
    return codigo

#############################
def validaRango ( dato,  li,  ls):
    ok=False
    if (dato >=li and dato <= ls):
        ok=True
    return ok
############################
def ingresa_valida(linf,lsup):
    nro=int(input("Ingrese un valor entero :"))
    while(nro < linf or nro > lsup):
        nro=int(input("Ingrese un valor entero :"))
    return nro
##########################
def ingresa_valida2(valor):
    nro=int(input("Ingrese un valor positivo :"))
    while nro<valor:
          nro=int(input("Ingrese un valor positivo ."))
    return nro
################################
def mostrarM(m,filas,columnas):
    print("\t\tENERO\tFEBRERO\tMARZO ABRIL\tMAYO\tJUNIO\tJULIO AGOSTO SEPTIEMBRE OCTUBRE NOVIEMBRE DICIEMBRE")
    for i in range(filas):
        print("PRODUCTO %2d"  %(i+1),end=" ")
        for j in range(columnas):
            print("\t",m[i][j],end=" ")
        print()
 ######################       
def MayorRe(m,filas,v1,v2):
    for i in range(filas):
        suma=0
        suma+=sum(m[i])
        v1.append(v2[i]*suma)
###########################          
def MostrarMayorR(filas,v)  :
    pos=v.index(max(v))
    print("El producto "+str(pos+1),"hizo la mayor reacudacion con  $" +str(max(v)))



def punto_C ( matriz, vprecio,  cf , cc):
    vecfactrim=[0.0]*4 
    
    '''POSICIÓN CONTENIDO
              0      Facturación del 1er trimestre.
              1      Facturación del 2do trimestre.
              2      Facturación del 3er trimestre.
              3      Facturación del 4to trimestre.'''
                            
    for f in range (cf):
        for c in range (cc):
             # c/3= > Retorna el número entero de la división.
                     # si c<3 -> índice del primer trimestre,
                     # si c<6 ->índice del 2do trimestre,
                     # c<9 ->índice del 3er trimestre,
                     # c <12 -> índice del 4º trimestre.
             
            vecfactrim[c//3]+=matriz[f][c] * vprecio[f]
        

    posmin=minimo(vecfactrim,4)
    print("\n El trimestre de menor facturacion fue " +str(posmin+1)+"  con una facturacion de " + str(vecfactrim[posmin]))