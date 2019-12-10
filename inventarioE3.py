import math
import random
import numpy as np

s=[20,20,20,20,40,40,40,60,60]
S=[40,60,80,100,60,80,100,80,100]
p=[1,2,2,3,3,4]

ct = 0 #costo total promedio por mes
co = 0 #costo total orden por mes
cm = 0 #costo total mantenimiento por mes
ce = 0 #costo total escacez por mes

i=0
meses = 120
Nmeses = 30*meses
Iinicial = 60
cliente = 0
bandera_pedido = True
contador = 0
dia_llegada = 0
productoActual = 0
mesActual = 1
entregaPedido = 0
encargo = False
cant_pedido =0

def pedido():
    global productoActual
    global entregaPedido
    global contador
    global encargo
    global cant_pedido
    global co
    global i
    if ((productoActual >= s[i] and productoActual<= S[i])or(productoActual>= S[i])):
        pass
    else:
        entregaPedido = random.randint(15,30)
        entregaPedido = contador + entregaPedido
        cant_pedido = S[i]-productoActual
        co += (3*cant_pedido)+32
        encargo = True
    

def llegadas_clientes():
    global dia_llegada
    global contador
    global productoActual
    global mesActual
    global bandera_pedido
    global entregaPedido
    global encargo
    global cliente
    global cm
    global ce
    #se calcula la llegada del proximo cliente con una distribucion exponencial
    llegada = np.random.uniform(0.0,1.0) 
    dia_llegada_aux = ((math.log(1-llegada))/(-10))*(30)
    dia_llegada += dia_llegada_aux
    #si la llegada es en el siguiente mes se realiza antes el pedido
    if(dia_llegada>= 30*(mesActual+1)):     
        mesActual +=1
        if (bandera_pedido==False):            
            if (productoActual >= 0):
                cm += 1*(productoActual)
            else:
                ce += 5*(productoActual)
        bandera_pedido = True
    if(entregaPedido<= dia_llegada and encargo == True):
        contador = entregaPedido
        productoActual = productoActual + cant_pedido       
        encargo = False
    if (dia_llegada >= 30 *mesActual and bandera_pedido == True):
        contador = 30*mesActual
        bandera_pedido = False
        entregaPedido = 0
        pedido()
    contador = dia_llegada
    cliente+=1
    num_prod = random.choice(p)
    productoActual = productoActual - num_prod    
    
def main():
    global productoActual
    global Iinicial
    global cliente
    global cant_pedido
    global encargo
    global contador
    global dia_llegada
    global mesActual
    global bandera_pedido
    global entregaPedido
    global ct
    global co
    global meses
    global cm
    global ce
    global i
    coL = []
    cmL = []
    ceL = []
    ctL = []
    for i in range(9):# hace el recorrido sobre las 9 politicas establecidad
        productoActual = Iinicial
        cliente = 0
        bandera_pedido = True
        contador = 0
        dia_llegada = 0
        productoActual = 0
        mesActual = 1
        entregaPedido = 0
        encargo = False
        cant_pedido =0
        co = 0
        ct = 0
        ce = 0
        cm = 0
        while(contador <= Nmeses):
            llegadas_clientes()
        co = co/meses
        cm = cm/meses
        ce = ce/meses
        ct = co + cm + (ce*(-1))
        coL.append(co)
        cmL.append(cm)
        ceL.append(ce*(-1))
        ctL.append(ct)
    for j in range(9):
        print("s: {} S:{} Ct:{:.2f} Co:{:.2f} Cm:{:.2f} Ce:{:.2f}".format(s[j],S[j],ctL[j],coL[j],cmL[j],ceL[j]))
        print()
       
            
    
if __name__ == "__main__":
    main()