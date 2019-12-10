import random
import matplotlib.pyplot as plt
import numpy as np

#Variables globales
numganados = int(0)    #Numero de partidas ganadas en total
numperdidos = int(0)   #Numero de partidas perdidas en total

def jugar():
    cara = int(0)   #Tomaremos 0 si el volado es cara
    cruz = int(0)   #Tomaremos 1 si es volado es cruz
    pagojuego = int(0)   #Cada que se tire un volado sera 1 peso 
    pagofijo = int(8)    #Una vez termine el juego siempre recibe esta cantidad
    pagofinal= int(0)    
    numpromedio = int(0)
    
    while abs(cara-cruz)!=3 or abs(cruz-cara)!=3:
        pagojuego = pagojuego +1        #Se paga 1 peso por cada volado, es el total de volados
        volado = np.random.uniform(0.0,1.0)    #Solo nos puede dar 0(cara) o 1(cruz)
        if volado < 0.5:
            cara += 1
        else:
            cruz += 1

    numpromedio += pagojuego          #Total de volados en todos los juegos
    pagofinal = pagofijo-pagojuego    #Pago final por juego

    if pagofinal > 0:       #Juegos donde se gano
        global numganados
        numganados += 1
    else:                   #Juegos donde se perdio
        global numperdidos
        numperdidos += 1
    
    """print(f"Obtuviste un total de {pagofinal} pesos")
    print(f"El total de volados en el juego es: {pagojuego}")"""

    return [pagofinal,pagojuego]
    

def main():
    print("**************************")
    print("BIENVENIDO A JUGAR VOLADOS")
    print("**************************")
    veces = int(input("Dame el numero de veces a jugar: "))  #Numero de veces que quiera entrar al juego
    num_de_iteraciones_inicial = int(10)           
    num_de_iteraciones_total = int(veces)            
    matriz_promedio = [[],[]]
    lista_ganancias = []

    while num_de_iteraciones_inicial <= num_de_iteraciones_total:
        totalvoladosgeneral = int(0)
        pagofinalgeneral = int(0)
        promediovoladototal = float(0)  
        promedioganancias = float(0)

        for i in range(num_de_iteraciones_inicial):      #Recorrido del 0 al numero proporcionado
            """print("---------------------------------")
            print(f"En el juego numero {i+1} obtuviste lo siguiente")"""
            listarespuesta = jugar()
            pagofinalgeneral += listarespuesta[0]
            totalvoladosgeneral += listarespuesta[1]
              
        promediovoladototal = totalvoladosgeneral/num_de_iteraciones_inicial       #Promedio total de volados
        promedioganancias = pagofinalgeneral/num_de_iteraciones_inicial      #Promedio total de ganancias 
        matriz_promedio[0].append(promediovoladototal)
        matriz_promedio[1].append(num_de_iteraciones_inicial)
        lista_ganancias.append(promedioganancias)
        num_de_iteraciones_inicial = 100+num_de_iteraciones_inicial           #Valor donde incrementamos los juegos

    print("*********************************************")
   # print(f"El numero promedio de lanzamiento de todos los juegos es: {}")
    """print(f"El numero de juegos ganados es de: {numganados}")
    print(f"El numero de juegos perdidos es de: {numperdidos}")
    print(f"El promedio de ganancias es de: {promedioganancias}")
    print("*********************************************")"""
    plt.xlabel("Número de partidas")
    plt.ylabel("Número promedio de volados")
    """print(f"El arreglo del promedio total tiene: {matriz_promedio[0]}")
    print(f"El arreglo del numero de iteraciones tiene: {matriz_promedio[1]}")"""
    print(f"El promedio de volados es {promediovoladototal}")
    print(f"El promedio de ganancias es {promedioganancias}")
    print(f"Mientras mas grande sea el numero de lanzamientos es mejor para sacar el promedio, ya que el promedio de lanzamientos es mas acercado al 9 y la perdida de pesos es de $1")
    print(f"Como se observa en la grafica azul se representa el promedio de lanzamientos que tiende a 9 y en la naranja se muestra el promedio de las ganancias o perdidas, la cual tiene a -1 y representa mayor perdidas")
    plt.plot(matriz_promedio[1],matriz_promedio[0])
    plt.plot(matriz_promedio[1],lista_ganancias)
    plt.show()

if __name__ == "__main__":
    main()
    