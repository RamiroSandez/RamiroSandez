from random import randint
from Libreria1 import *
vPrecios=[randint(10,100) for i in range(20)]
mProductos=[[0]*12 for i in range(20)]
vRecaudacion=[]
filas=len(mProductos)
columnas=len(mProductos[0])
codigo=ingresoCodigo(1,20,0)
while codigo!=0:
    print("\nIngrese el dia -->")
    dia=ingresa_valida(1,31)
    print("\nIngrese el mes -->")
    mes=ingresa_valida(1,12)
    print("\nIngresa la cantidad de unidades -->")
    cantidad=ingresa_valida2(0)
    
    
    mProductos[codigo-1][mes-1]+=cantidad
    
    codigo=ingresoCodigo(1,20,0)

mostrarM(mProductos,filas,columnas)
MayorRe(mProductos,filas,vRecaudacion,vPrecios)
MostrarMayorR(filas,vRecaudacion)