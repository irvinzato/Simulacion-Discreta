import random
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("**************************")
    print("SIMULACION DE CAJA ATENDIENDO A CLIENTES")
    print("**************************")
    veces = int(input("Dame el numero de veces que quieres simular: "))   #Numero de veces que quiera entrar al juego
    num_de_iteraciones_inicial = int(1)           
    num_de_iteraciones_total = int(veces) 
    dia = int(1)   
    promedio_tiempo_grafica = []                                          #Guardar el promedio en tiempo de cada iteracion
    promedio_clientes_grafica = []                                        #"                 " de clientes 
    num_simulaciones = []

    while num_de_iteraciones_inicial <= num_de_iteraciones_total:
        hora_abierto = int(540)                                    #A esta hora se empezara a atender clientes 60 min es 1 hora
        hora_cerrado = int(1020)                                   #A esta hora cierra la caja 1020 son las 5pm
        if dia > 1:
            hora_cerrado = dia*hora_cerrado
        else:
            hora_cerrado = 1020
        estado_caja = "CERRADO"
        arreglo_tiempo = [[],[]]                                    #lista donde se agregara la hora de entrada y hora de salida
        arreglo_tiempo_entrada = []
        arreglo_tiempo_salida = []
        contador_minutos = int(0)                                      #Mide el tiempo en minutos dentro del while
        contador_clientes_total = int(0)                               #Total de clientes
        contador_clientes_entrada = int(0)                             #Clientes que han entrado       
        contador_clientes_salida = int(0)                              #Clientes que fueron atendidos
        suma_intervalos_clientes_total = int(0)
        #tiempo_promedio_espera = []
        cliente_fila = int(0)
        
        while hora_abierto < hora_cerrado or contador_clientes_salida < contador_clientes_entrada:
            hora_abierto += 6                                          #Se le suma los minutos que quieran pasar  
            if hora_abierto <= hora_cerrado:  
                aleatorio_entrada = np.random.uniform(0.0,1.0)             #Genero numero aleatorio para entrada
                #print(f"el numero aleatorio es {aleatorio_entrada}")
                if aleatorio_entrada < 0.259:
                    #Ocurre una llegada de cliente
                    arreglo_tiempo[0].append(hora_abierto)                 #Guardo el tiempo en que entra el cliente
                    arreglo_tiempo_entrada.append(hora_abierto)
                    #print(f"Acaba de llegar un cliente en el tiempo {hora_abierto}")
                    contador_clientes_entrada += 1
                    cliente_fila +=1
                else:                                                       #Numero mayor a .0259
                    #No llega ningun cliente
                    print(f"No llego cliente")
            
            if contador_clientes_entrada > 0:                        #Ya llego algun cliente por atender
                aleatorio_salida = np.random.uniform(0.0,1.0)          #Genero numero aleatorio para entrada
                if aleatorio_salida < 0.393 and cliente_fila >= 1:
                    #Ocurre una salida de cliente
                    arreglo_tiempo[1].append(hora_abierto)          #Guardamos el tiempo en que salio el cliente
                    arreglo_tiempo_salida.append(hora_abierto)
                    contador_clientes_total += 1
                    contador_clientes_salida +=1
                    cliente_fila -= 1
                    #print(f"Un cliente ya fue atendido en el tiempo {hora_abierto}")
                elif hora_abierto == hora_cerrado:
                    contador_minutos+=6                                 #Minutos extra despues de cerrar la caja
                else:
                    pass
                    #No ocurre ninguna salidas     
        for i,j in zip(arreglo_tiempo_entrada, arreglo_tiempo_salida):
            suma_intervalos_clientes = j - i
            #print(f"El tiempo tardado por el primer cliente es de {suma_intervalos_clientes}")
            suma_intervalos_clientes_total += suma_intervalos_clientes
            suma_intervalos_clientes = int(0)

        #PROMEDIOS POR ITERACION
        tiempo_promedio_espera = suma_intervalos_clientes_total/contador_clientes_total
        promedio_clientes = contador_clientes_total/hora_cerrado
        
        #PROMEDIO PARA GRAFICAS 
        promedio_tiempo_grafica.append(tiempo_promedio_espera)
        promedio_clientes_grafica.append(promedio_clientes)
        dia += 1
        num_simulaciones.append(dia)
        num_de_iteraciones_inicial += 1

    #print("La caja ya esta cerrada")
    #print(f"Los horarios de entradas de clientes son --> {arreglo_tiempo_entrada}")
    #print(f"Los horarios de salida de los clientes son --> {arreglo_tiempo_salida}")
    #print(f"El banco cierra a las: {hora_cerrado} pero como habia gente este cerrando a las: {hora_abierto}")
    print(f"El total de clientes fue de -> {contador_clientes_total}")
    #print(f"La suma total de los invervalos de tiempo es de {suma_intervalos_clientes_total}")
    print(f"EL TIEMPO PROMEDIO DE ESPERA ES {tiempo_promedio_espera}")
    #print("-------------------------------------------------------------")
    print(f"La lista de los promedios de cada itereacion es --> {promedio_tiempo_grafica}")
    print(f"La lista de los promedios de clientes por itereacion es --> {promedio_clientes_grafica}")

    #GRAFICA
    plt.xlabel("Tiempo promedio")
    plt.ylabel("Número promedio de clientes")
    plt.plot(num_simulaciones, promedio_clientes_grafica)

    #plt.ylabel("Promedio de espera cliente")
    #plt.xlabel("Numero de dias")
    #plt.plot(num_simulaciones, promedio_tiempo_grafica)
    plt.show()

if __name__ == "__main__":
    main()