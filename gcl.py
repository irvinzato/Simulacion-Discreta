semilla1=123457
semilla2=7531
numGen = []
seleccion = []
aleatorio = []
dx = 1/128

def gcl1():
    global semilla1
    print("El valor de la semilla es ---> ", semilla1)
    xi = 40014*semilla1 % 2147483563
    semilla1 = xi
    ri1 = xi/2147483563
    return ri1

def gcl2():
    global semilla2
    print("El valor de la semilla es ---> ", semilla2)
    xi = 40692*semilla2 % 2147483399
    semilla2 = xi
    ri2 = xi/2147483399
    return int(ri2/dx)

def gclc(gen):
    print("Soy gclc y me estan pasando ", gen)
    #gcl1()
    return gen

def main():    
    for i in range(128):
        ri1 = gcl1()
        numGen.append(ri1)
        #print(ri1)
    
    print("EL ULTIMO VALOR ES " ,numGen[127])
    
    for i in range(15):
        ri2 = gcl2()                    #genera un entero
        seleccion.append(ri2)
        sel = gclc(seleccion[i])        #regresa el primer alatorio
        aleatorio.append(numGen[sel])
        r1nuevo = gcl1()                #genera otro R1 para sustituirlo
        print("El nuevo numero generado para GCL1 es --> ",r1nuevo )
        numGen[sel] = r1nuevo           #nuevo numero a guardar en posicion usada
        #print("El numero generado es ",ri2, " El seleccionado es ", sel, "El r1nuevo es ", r1nuevo)

    """for i in range(len(seleccion)):
        sel = gclc(seleccion[i])
        aleatorio.append(numGen[sel])
        print("mi sel es ", sel)"""
    
    print("EL ARREGLO DE GCL1 ES")
    print(numGen)
    print("-------------------")
    print("EL ARREGLO DE GCL2 ES")
    print(seleccion)
    print("-------------------")
    print("EL ARREGLO DE ALEATORIOS ES")
    print(aleatorio)
    

if __name__ == "__main__":
    main()