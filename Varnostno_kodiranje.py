import math

import numpy as np


def naloga3(vhod: list, n: int) -> tuple[list, str]:
    izhod = []
    crc = ''
    m = int(math.log2(n + 1))
    k = n - m
    H = np.zeros((m,n),dtype=np.uint8)
    
    for i in range(1,n + 1):
        num = bin(i)[2:].zfill(m)
        for j in range(0, m):
            H[j,i-1] = num[len(num)-j-1]
    data = []
    var = []
    pow2  = 1
    for i in range(1,n+1):
        if(i == pow2):
            pow2*=2
            var.append(i-1)
        else:
            data.append(i-1)
    res = data
    res.extend(var)
    H = H[:,res]
    #print(res)
    #print(H)
    Ht = np.transpose(H)
    arr = np.zeros(n, dtype=np.uint8)
    #zeroVector = np.zeros(m, dtype=np.uint8)
    for i in range(0,len(vhod)):
        arr[i % n] = vhod[i]
        if(i % n  == n - 1):
            S = arr.dot(Ht)
            S = np.remainder(S,2)
            if(np.all(S == 0)):
                izhod.extend(arr[0:k])
            else:
                for j in range(0,n):
                    found = True
                    for k1 in range(0,m):
                        if(H[k1,j] != S[k1]):
                            found = False
                            break
                    if (found):
                        arr[j]^=1
                        izhod.extend(arr[0:k])
                        break
    ################################################################################################
    gPolinom = 0xD9
    reg = 0xFF
    for i in vhod:
        curr = (reg&1)^i
        reg>>=1
        if(curr == 1):
            reg^=gPolinom
    
    res = str(bin(reg)[2:]).zfill(8)[::-1]
    crc = hex(int(res,2))[2:].upper()
        




    #print(izhod)
    return (izhod, crc)
