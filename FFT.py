import numpy as np


def naloga4(vhod: list, fs: int) -> str:
    izhod = ''
    t=len(vhod)/fs
    df=1/t

    toni = {
    261.63:  'C1'  ,   523.25:'C2',
    277.18:  'CIS1',   554.37:'CIS2', 
    293.66:  'D1'  ,   587.33:'D2',   
    311.13:  'DIS1',   622.25:'DIS2', 
    329.63:  'E1'  ,   659.25:'E2',   
    349.23:  'F1'  ,   698.46:'F2',   
    369.99:  'FIS1',   739.99:'FIS2', 
    392  :  'G1'  ,    783.99:'G2',   
    415.30:  'GIS1',   830.61:'GIS2', 
    440  :  'A1'  ,    880:  'A2',
    466.16:  'B1'  ,   932.33:'B2',       
    493.88:  'H1'  ,   987.77:'H2',   
    }
    akordi = {
    'Cdur' : ['C1', 'E1', 'G1'],
    'Cmol' : ['C1', 'DIS1', 'G1'],
    'Ddur' : ['D1', 'FIS1', 'A1'],
    'Dmol' : ['D1', 'F1', 'A1'],
    'Edur' : ['E1', 'GIS1', 'H1'],
    'Emol' : ['E1', 'G1', 'H1'],
    'Fdur' : ['F1', 'A1', 'C2'],
    'Fmol' : ['F1', 'GIS1', 'C2'],
    'Gdur' : ['G1', 'H1', 'D2'],
    'Gmol' : ['G1', 'B1', 'D2'],
    'Adur' : ['A1', 'CIS2', 'E2'],
    'Amol' : ['A1', 'C2', 'E2'],
    'Hdur' : ['H1', 'DIS2', 'FIS2'],
    'Hmol' : ['H1', 'D2', 'FIS2'],
    }
    transformed = np.fft.fft(vhod) 
    transformed = abs(transformed[:len(vhod)//2]) # ker je simetričen

    interval = np.arange(len(vhod) // 2) * (df)
    #print(np.average(transformed))
    arr = np.sort(transformed)[len(transformed)-20:]
    povp = np.average(arr)
    #print(povp)
    for i in range(0, len(transformed)):
        if(transformed[i] < povp):
            transformed[i] = 0
    intervalStart = -1
    curr = set()
    #print(interval)
    for i in range(0, len(transformed)):
        if(transformed[i] > 0 and intervalStart == -1):
            intervalStart = i
        elif(transformed[i] == 0 and intervalStart != -1):
            #print("intervalStart: "+str(intervalStart)+" "+str(i))
            avg = np.average(interval[intervalStart:i])
            #print(avg, intervalStart, i, interval[intervalStart:i])
            for t in toni:
                if(abs(avg-t) < df+0.3):
                    curr.add(toni[t])
            intervalStart = -1 
        
                
            
 
    for a in akordi:
        if(set(akordi[a]).issubset(curr)):
            izhod = a
    return izhod


