import random
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    dias = int(2)
    terminar = 200000
    promedio_espera = [[],[]]                       #promedio tiempo/ dias
    promedio_fila = [[],[]]                       #promedio clientes/ hrs 
    
    while (dias <= terminar):               #Veces que se va a iterar la simulacion
        suma = float(0)
        cont = int(0)

        tabla = [[],[]]                             #Hora en que entra y sale del banco el cliente
        tabla_clientes_en_fila = []                 #Almacena los clientes en la fila
        contador_llegada = int(0)
        clientes_total = int(0)
        contador_salida = int(0)
        nt = int(0)
        tiempo_caja = []
        hora_cerrar = int(300)                        #Simular 8 horas de 9:00 - 5:00
        llegadaEvento = float(0)                     #Incrementos por evento P3
        salidaEvento = float(0)
        horaSigLlegada = float(0)                   # horaSigLlegada += llegadaEventoMin
        horaSigSalida = float(-1)                    # horaSigSalida += salidaEventoMin    
        tiempo = []                                 # almacenara la hora siguiente de llegada y salida
        tiempo.append(0)                            #Para que empiece en el tiempo 0
        contadorTiempo = int(0)                     #Recorrer el arreglo
        banderaSalida = False                       #Para saber si ya tengo una horaSigSalida

        #Primer hora de entrada generada antes de entrar al ciclo
        #Antes de agregar la hora de llegada hay que verificar que sea menor que la hora de salida
        #contadorTiempo += 1
        #tiempo.append(horaSigLlegada)
        #print(f"El valor de tiempo en 1 es de {tiempo[contadorTiempo]}")

        while(tiempo[contadorTiempo] <= hora_cerrar):

            if(contadorTiempo == 0):       #caso especial
                aleatorio_entrada = np.random.uniform(0.0,1.0)
                llegadaEvento =  (math.log(1 - aleatorio_entrada)/(-3)) * 60
                print(f"El primer valor de llegada es de {llegadaEvento}")
                horaSigLlegada = llegadaEvento + tiempo[contadorTiempo]
                if(horaSigLlegada > horaSigSalida):                    #Añade las horas de menor a mayor
                    tiempo.append(horaSigLlegada)                      #Siguiente hora de llegada
                else:  #La hora siguiente de salida es menor
                    tiempo.append(horaSigSalida)
                contadorTiempo += 1

            if(tiempo[contadorTiempo] == horaSigLlegada):       #Ocurre una llegada de cliente
                print(f"LLEGO UN CLIENTE EN EL TIEMPO {tiempo[contadorTiempo]}")
                contador_llegada += 1  
                tabla[0].append(horaSigLlegada)                 #Hora en que llego el cliente
                nt += 1
                #Puedo tener la siguiente hora de llegada   
                aleatorio_entrada = np.random.uniform(0.0,1.0)
                llegadaEvento =  (math.log(1 - aleatorio_entrada)/(-3)) * 60
                horaSigLlegada = llegadaEvento + tiempo[contadorTiempo]
                print(f"El siguiente valor de llegada es de {horaSigLlegada}")
                if(nt > 0 and banderaSalida != True):           #Puede ocurrir una salida por que hay alguien en la fila
                    aleatorio_salida = np.random.uniform(0.0,1.0)
                    salidaEvento = (math.log(1 - aleatorio_salida)/(-5)) * 60
                    horaSigSalida = salidaEvento + tiempo[contadorTiempo]
                    print(f"Llego un cliente y genero una variable de salida nueva {horaSigSalida}")
                    #contador_salida += 1
                    #tabla[1].append(intervalo)
                    banderaSalida = True                #Ya hay una salida generada

            if(tiempo[contadorTiempo] == horaSigSalida and nt > 0):  #Ya es hora de que salga alguien
                print(f"SE FUE UN CLIENTE EN EL TIEMPO {tiempo[contadorTiempo]}")
                contador_salida += 1
                tabla[1].append(horaSigSalida)          #Hora en que salio el cliente
                nt -= 1
                #print(f"El valor de clientes en cola es de ---> {contador_llegada}")
                clientes_total += 1             #Los clientes que ya fueron atendidos
                banderaSalida = False           #Ya atendi mi horaSalida
                if(nt > 0 and banderaSalida != True):       #Aun hay gente por atender
                    aleatorio_salida = np.random.uniform(0.0,1.0)
                    salidaEvento = (math.log(1 - aleatorio_salida)/(-5)) * 60
                    horaSigSalida = salidaEvento + tiempo[contadorTiempo]
                    print(f"Ya atendi una salida pero genero otra por que hay mas gente {horaSigSalida}")
                    banderaSalida = True        #Ya hay una salida generada

            if(tiempo[contadorTiempo] == horaSigSalida and (contador_llegada-contador_salida) <= 0):
                #tiempo.append(horaSigLlegada)
                horaSigSalida = 100000

            if(horaSigLlegada < horaSigSalida):                    #Añade las horas de menor a mayor
                tiempo.append(horaSigLlegada)                      #Siguiente hora de llegada
                tabla_clientes_en_fila.append(nt)       #clientes que hay en cola en el tiempo n
            if(horaSigLlegada > horaSigSalida):  #La hora siguiente de salida es menor
                tiempo.append(horaSigSalida)
                tabla_clientes_en_fila.append(nt)
            print("---------------------------------------------")
            print(f"t= {tiempo[contadorTiempo]}, nt= {nt}, hlleg= {horaSigLlegada}, hsalid{horaSigSalida}")
            print("---------------------------------------------")

            contadorTiempo += 1             

        while(nt > 0):          #Aun hay clientes por atender pero ya acabo la hora de salida
            contador_salida +=1
            nt -= 1
            aleatorio_salida = np.random.uniform(0.0,1.0)
            salidaEvento = (math.log(1 - aleatorio_salida)/(-5)) * 60
            horaSigSalida = salidaEvento + tiempo[contadorTiempo]
            #print(f"Ya atendi una salida pero genero otra por que hay mas gente {horaSigSalida}")
            tiempo.append(horaSigSalida)
            tabla_clientes_en_fila.append(nt)
            contadorTiempo += 1

                       
            #Fuera de los ifs
            #Para atender el siguiente tiempo
        #print(f"Se atendio un total de {clientes_total} clientes")
        #print(f"La tabla tiene {tabla}, tamaño de llegada: {len(tabla[0])}, tamaño de salida: {len(tabla[1])}")
        #print(f"El valor 1 del arreglo llegada es {tabla[0][0]}")
        
        #Tiempo que paso cada cliente en la caja
        tamaño = len(tabla[1])          #Tamaño del arreglo de salidas

        while(cont < tamaño):
            suma += (tabla[1][cont] - tabla[0][cont])
            tiempo_caja.append(tabla[1][cont] - tabla[0][cont])
            cont += 1
        print(f"El tiempo tola en caja es de -> {suma}")
        promedio_espera[0].append((suma/tamaño)/60)       #tabla 1 tiene los clientes que salieron
        promedio_espera[1].append(dias)
        cont = 0
        suma = 0.0

        while(cont < len(tabla_clientes_en_fila)):                          #Clientes que estan en la fila
            suma += tabla_clientes_en_fila[cont]
            cont += 1

        promedio_fila[0].append(suma/len(tabla_clientes_en_fila))
        promedio_fila[1].append(dias)

        print("------------------------------------------")

        dias = 2*dias

    #RESULTADOS EN GRAFICAS
        
    plt.plot(promedio_espera[1],promedio_espera[0])
    plt.plot(promedio_fila[1],promedio_fila[0],"r-")
    plt.show()
    
if __name__ == "__main__":
    main()
