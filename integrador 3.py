from Libreria3 import *
def __main__():
    #Creacion de matriz por comprension
    mVotos=[[0]*15 for i in range(10) ]
    #Vectores
    vLista=[0]*10
    vTotal=[0]*10
    totalVotos=0

    #carga inicial del vector de listas completo sin repetidos
    #cargaListas(vLista)
    vLista=[111,222,333,444,555,666,777,888,999,123]
    lista=ingresoLista(100,999,0)
    while (lista!=0):
        if lista in vLista:
            posicionLista=vLista.index(lista)
            sede=ingresoSede(1,15)
            votos = int(input("Ingrese Votos ->"))
            while(votos<0):
                votos = int(input("Error - Re-Ingrese Votos ->"))

            # cargo el voto en la matriz
            mVotos[posicionLista][sede-1]+=votos

            #sumo  los votos por lista
            vTotal[posicionLista]+=votos

            #sumo para el totalvotos para calcular porcentaje
            totalVotos+=votos
            
            lista= ingresoLista (100,999,0)
        else:
            # no lo encontro
            print ("\n\nError lista incorrecta, reingrese la lista")
            posicionLista=-1
            lista= ingresoLista (100,999,0)
     #/A - Listar los votos recibidos x lista en cada sede
   # mostrarm(mVotos,vLista,10,15)


    #/C  - Cantidad de candidatos que no recibieron votos en la sede 5
    print ("\n\n\n ***   CANDIDATOS SIN VOTOS EN LA SEDE 5 \n")
    muestraNoVotosxSector(mVotos,vLista,5,10)


    #/B - Listar totales votos ordenados
    ordenar (vLista,vTotal,totalVotos)

     
    

















if __name__ == "__main__":
    __main__()