import numpy as np
import math as m
import scipy.stats as ss

#ESTA ES LA INTENSIDAD DEL PROCESO DE POISON NO HOMOGENEO  
#MODIFIQUELA SI PREFIERE USAR OTRA
def lambd(t):

    if t < 6:
        f = 2
    elif t > 6 and t < 18:
        f = 9
    else: f = 5

    return(f)

def nhp(n, time, mu):
    err = float(input("Inserte el error -> "))
    sig = float(input("Inserte la probabilidad -> "))

    Nt = []
    for i in range(n):
        sn = 0
        Pt = 0 
        t = 1
        while sn <= time:
            x = np.random.exponential(1/mu, 1)
            sn = sn + x
            u = np.random.uniform(0, 1, 1)
            if u <= lambd(sn)/mu: Pt += 1
        Nt = np.append(Nt, Pt)

    Z = ss.norm(0, 1)
    t = Z.ppf(sig)

    cont = 0
    while t*m.sqrt(np.var(Nt))/m.sqrt(n) > err :
        if(cont == 4): break
        n = int((m.sqrt(np.var(Nt))*t/err)**2) 			

        print("Se iterará ->",n ,"veces")

        Nt = []
        for i in range(n):
            sn = 0
            Pt = 0 
            t = 1
            while sn <= time:
                x = np.random.exponential(1/mu, 1)
                sn = sn + x
                u = np.random.uniform(0, 1, 1)
                if u <= lambd(sn)/mu: Pt += 1
            Nt = np.append(Nt, Pt)
        cont += 1

    return(Nt, t, n, err, sig)


x = nhp(50, time = 24, mu = 9) 
err = x[3]
sig = x[4]
E = np.mean(x[0])
print("Error <", err, "con una probabilidad de" ,sig ,"->" ,E, ", mientras el exacto es 150")
