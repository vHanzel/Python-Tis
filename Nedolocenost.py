import math
import re
from collections import Counter


def naloga1(besedilo: str, p: int) -> float:
    str = re.sub(r'[^A-Za-z]', '', besedilo)
    res = str.upper()
    n = len(res)
    crke = Counter(res)
    H = float(0)
    if p == 0 :
        for l in crke:
            H -= crke[l]/n * math.log2(crke[l]/n)
    elif p == 1:
        crke2 = {}
        for i in range(0,n - 1):
            curr = res[i] + res[i + 1]
            if(curr in crke2):
                crke2[curr] +=1 
            else:
                crke2[curr] = 1
        for l in crke:
            H += crke[l]/n * math.log2(crke[l]/n)
        for l in crke2:
            H -= crke2[l]/(n-1) * math.log2(crke2[l]/(n-1))
    elif p == 2:
        crke3 = {}
        for i in range(0,n - 2):
            curr = res[i] + res[i + 1]+ res[i + 2]
            if(curr in crke3):
                crke3[curr] +=1 
            else:
                crke3[curr] = 1 

        crke2 = {}
        for j in range(0,n - 1):
            curr = res[j] + res[j + 1]
            if(curr in crke2):
                crke2[curr] +=1 
            else:
                crke2[curr] = 1
        
        for l in crke3:
            H -= crke3[l]/(n-1) * math.log2(crke3[l]/(n-1))
        for l in crke2:
            H += crke2[l]/(n-2) * math.log2(crke2[l]/(n-2))
    
    
    return H

