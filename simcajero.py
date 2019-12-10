from matplotlib import pyplot
import numpy as np

def cajero(dias):
    tabla = [[],[]]                          #Hora en que entra y sale del banco el cliente
    tabla_clientes_en_fila = []              #Almacena los clientes en la fila
    contador_llegada = int(0)
    contador_salida = int(0)
    intervalo = float(0)
    cerrar = False
    hora_cerrar = dias
 
    
    while (cerrar == False  or contador_llegada > contador_salida):      #termina el horario del cajero
       
        if (int(intervalo)-hora_cerrar != 0 and cerrar == False):
            aleatorio_entrada = np.random.uniform(0.0,1.0)
            
            if (aleatorio_entrada < .259):                  #Llega un cliente
                contador_llegada += 1
                tabla[0].append(intervalo)
        else:
            cerrar = True;                              #Cierra el banco
            
        if (contador_llegada - contador_salida >= 1 and tabla[0][contador_llegada-(contador_llegada-contador_salida)] != intervalo):
            aleatorio_salida = np.random.uniform(0.0,1.0)
           
            if(aleatorio_salida < .393):                    #Se va el cliente
                contador_salida += 1
                tabla[1].append(intervalo)
                                
            
        intervalo += .1
        tabla_clientes_en_fila.append(contador_llegada-contador_salida)
        
    print("--------------------------------------------------------------")
    print(f"Total de clientes que llegaron --> {contador_llegada} ")
    print(f"salieron --> {contador_salida} ")
    return tabla,tabla_clientes_en_fila

            
def main():
    dias = int(8)
    terminar = 60000
    promedio_espera = [[],[]]                       #promedio tiempo/ dias
    promedio_fila = [[],[]]                       #promedio clientes/ hrs 
    
    while (dias <= terminar):
        suma = float(0)
        total = []
        tabla = cajero(dias)
        tabla_tiempo_espera = tabla[0]
        tabla_clientes_en_fila = tabla[1]
        contador = int(0)

        while(contador < len(tabla_tiempo_espera[0])):                          #Tiempo en que esta en cajera el cliente
            suma += round(tabla_tiempo_espera[1][contador]-tabla_tiempo_espera[0][contador],2)
            total.append(round(tabla_tiempo_espera[1][contador]-tabla_tiempo_espera[0][contador],2))
            contador += 1

        promedio_espera[0].append(suma/len(tabla_tiempo_espera[0]))
        promedio_espera[1].append(dias)
    
        contador = 0
        suma = 0.0

        while(contador < len(tabla_clientes_en_fila)):                          #Clientes que estan en la fila
            suma += tabla_clientes_en_fila[contador]
            contador += 1

        promedio_fila[0].append(suma/(dias*10))
        promedio_fila[1].append(dias)

        dias = 2*dias

    #RESULTADOS EN GRAFICAS
        
    pyplot.plot(promedio_espera[1],promedio_espera[0])
    pyplot.plot(promedio_fila[1],promedio_fila[0],"r-")
    pyplot.show()
        
if __name__ == "__main__":
    main()