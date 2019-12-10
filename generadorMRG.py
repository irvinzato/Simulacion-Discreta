semilla1 = [411040508, 544377427, 2887694751]
semilla2 = [702892456, 758163486, 2462939166]
a1 = 1403580
a2 = 810728 
a3 = 527612
a4 = 1370589
m1 =  4294967087
m2 =  4294944443

def mrg():
    global semilla1
    global semilla2

    x = (a1*semilla1[1] - a2*semilla1[0])%m1
    y = (a3*semilla2[2] - a4*semilla2[0])%m2

    semilla1[0] = semilla1[1]
    semilla1[1] = semilla1[2]
    semilla1[2] = x

    semilla2[0] = semilla2[1]
    semilla2[1] = semilla2[2]
    semilla2[2] = y

    dif = (x - y)%m1
    gen = dif/m1 
    
    return gen

def main():
    for i in range(15):
        print("estoy en la iteracion ",i," el valor de la funcion es ", mrg())

if __name__ == "__main__":
    main()