############################################
def cargaListas(v):
    for i in range(len(v)):
        lista=ingresaListaValidaRango(100,999)
        if lista in v :
            pos=v.index(lista)
            while (pos>=0):
                print("Error ingrese un numero que no este en la Lista\n\n")
                lista=ingresaListaValidaRango(100,999)
                if lista in v :
                    pos=v.index(lista)
                else:
                    pos=-1
        v[i]=lista  
        
   
def ingresoLista ( li, ls,  condicionCorte):

    lista=int(input("\nIngrese Numero de Lista: (100-999 ** 0 para finalizar) ->"))
    while (not(validaRango(lista,100,999)) and (lista!=condicionCorte)):
         lista=int(input("\nIngrese Numero de Lista: (100-999 ** 0 para finalizar) ->"))
    return lista
################################/
def ingresaListaValidaRango ( li,  ls):
    
    valor=int(input("\nIngrese un numero de lista de 3 cifras :->>"))
    
    while(valor<li or valor >ls):
        valor=int(input("\nError - Ingrese un numero de lista de 3 cifras :->>"))
    return valor



################################/
def validaRango ( dato,  li,  ls):
    ok=False
    if (dato >=li and dato <= ls):
        ok=True
    return ok

###############################

def ingresoSede(li,ls):
   sede=int(input("Ingrese Sede: (1-15) ->"))
   while(not validaRango (sede,li,ls)):
       sede=int(input("Ingrese Sede: (1-15) ->"))
   return sede

######################################
def mostrarm( m, vl, filas, columnas):

    print("\n\n\n      SEDE ->>\n")
    print ("LISTA\t01\t02\t03\t04\t05\t06\t07\t08\t09\t10\t11\t12\t13\t14\t15")
    for i in range (filas):
        mensaje=""
        mensaje="\n%3d\t" %vl[i]
        for j in range (columnas):
            
            mensaje=mensaje + "%3d\t" %m[i][j]
        print(mensaje)
############################################
def ordenar( v1, v2,total):
          
    print ("\n\n\nVOTOS\tPORC\tLISTA")
   
    for valor, lista in sorted(zip(v2, v1), reverse = True):
        
        if (total>0):
            porcentaje= valor*100/total
            print("\n%4d " %(valor),end=" ")
            print("\t%3.2f " %(porcentaje),end=" ")
            print("\t%3d " %(lista),end=" ")
# ########################################
def muestraNoVotosxSector( mVoto, vLista, sede,  fila):

    for i in range (fila):
        if (mVoto[i][sede-1] ==0):
            print ("\n\n\n Candidato sin voto en sede " + str(sede) + " " + str(vLista[i]) + "\n")

