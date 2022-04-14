import numpy as np
import math as m
import scipy.stats as ss

def llegadas(n, time, lam):
    err = float(input("Inserte el error -> "))
    sig = float(input("Inserte la probabilidad -> "))

    Nt = []
    for i in range(n):
        sn = 0
        c = 0 
        while sn <= time:
            x = np.random.gamma(2, 1/lam, 1)
            sn = sn + x
            c += 1
        Nt = np.append(Nt, c)

    Z = ss.norm(0, 1)
    t = Z.ppf(sig)

    cont = 0
    while t*m.sqrt(np.var(Nt))/m.sqrt(n) > err :
        if(cont == 4): break
        n = int((m.sqrt(np.var(Nt))*t/err)**2) 			

        print("Se iterará ->",n ,"veces")
        for i in range(n):
            sn = 0
            c = 0 
            while sn <= time:
                x = np.random.gamma(2, 1/lam, 1)
                sn = sn + x
                c += 1
            Nt = np.append(Nt, c)
        cont += 1

    return(Nt, t, n, err, sig, lam, time)

#Aqui cambie el tiempo el tiempo y el parametro  
x = llegadas(50, time = 30, lam = 3.4)

err = x[3]
sig = x[4]
E = np.mean(x[0]-1)
exact = (x[5]*x[6]/2) - (1 - m.e**(-2*x[5]*x[6]))/4
print("Error <", err, "con una probabilidad de" ,sig ,"->" ,E, ", mientras el exacto es ", exact)

 
    
