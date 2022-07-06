
    
def naloga2(vhod: list, nacin: int) -> tuple[list, float]:
    R = float('nan')
    izhod = []
    max_size=pow(2,12)
    
    if nacin == 0 :
        stElementov = 256
        slovar = dict([(chr(x), x) for x in range(stElementov)])
        inLen=len(vhod)
        N =""
        for crka in vhod :
            sn=N+crka
            if sn in slovar:
                N=sn
            else:
                izhod.append(slovar[N])
                if(len(slovar) < max_size):
                    slovar[sn] = stElementov
                    stElementov+=1
                N=crka
        izhod.append(slovar[N])
        outLen=len(izhod)
        R=(outLen*12)/(inLen*8)   
    elif nacin == 1:
        stElementov = 256
        slovar = dict([(x, chr(x)) for x in range(stElementov)])
        inLen=len(vhod)
        k=vhod.pop(0)
        n=slovar[k]
        izhod.append(n)
        K=n
        for koda in vhod:
            if koda in slovar:
                n=slovar[koda]
            else:
                n=K+K[0]
            for i in n:
                izhod.append(i)
            if(len(slovar) < max_size):
                slovar[stElementov] = K+n[0]
                stElementov+=1
            K=n
        outLen=len(izhod)
        R=(inLen*12)/(outLen*8)


    return (izhod, R)

