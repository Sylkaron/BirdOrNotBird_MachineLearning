import pandas as pd
import scipy.io.wavfile as wave
import matplotlib.pyplot as plt
import numpy as np

def loadDataSpectre():
    dfBird = pd.read_csv('D://dev//Pycharm-project//Ressources//ff1010bird_metadata.csv')
    dfBird.set_index('itemid', inplace=True)
    fmax = 20000
    freq=range(0,fmax,100)
    df=pd.DataFrame(index=dfBird.index,columns=freq)
    df.insert(0,'hasBird',dfBird['hasbird'])
    k=0
    spec_red=np.zeros(int(fmax/100))
    for sound in df.index:
        print(k,sound)
        file="D://dev//Projet Machine Learning//wav//"+str(sound)+".wav"

        rate,data=wave.read(file)
        spectre = np.absolute(np.fft.fft(data[0:441000]))
        spectre = spectre / spectre.max()
        for i in range(int(fmax/100)):
            spec_red[i]=np.mean(spectre[i*1000:i*1000+1000])
        df.loc[[sound],freq]=spec_red
        # plt.vlines(freq, [0], spec_red, 'r')
        # plt.xlabel('f (Hz)')
        # plt.ylabel('A')
        # plt.grid()
        # plt.title(sound)
        # plt.show()
        k+=1
    df.to_csv('..//Ressources//spectre.csv')
    return df



