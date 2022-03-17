import pandas as pd
import scipy.io.wavfile as wave
import matplotlib.pyplot as plt
import numpy as np

def loadDataSpectre():
    dfBird = pd.read_csv('..//Ressources//ff1010bird_metadata.csv')
    dfBird.set_index('itemid', inplace=True)
    fmax = 20000
    freq=range(0,fmax+1,10)
    df=pd.DataFrame(index=dfBird.index,columns=freq)
    df.insert(0,'hasBird',dfBird['hasbird'])
    k=0
    for sound in df.index:
        print(sound)
        file="D://dev//Projet Machine Learning//wav//"+str(sound)+".wav"

        rate,data=wave.read(file)
        n=data.shape[0]
        duree=n/rate

        start = 0
        stop = int(duree * rate)
        spectre = np.absolute(np.fft.fft(data[start:stop]))
        spectre = spectre / spectre.max()
        spec_red=np.zeros(int(fmax/10)+1)
        for i in range(int(fmax/10)+1):
            spec_red[i]=np.mean(spectre[i*100:i*100+100])
        df.loc[[sound],freq]=spec_red
        if(k>10):
            return df
        else:
            k+=1
    return df



