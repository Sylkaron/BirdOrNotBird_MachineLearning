import scipy.io.wavfile as wave
import matplotlib.pyplot as plt
import numpy as np

rate,data=wave.read("C://Users//thoma\Downloads//AMBSea_Mer vagues moyennes et mouettes (ID 0267)_LS.wav")

print(data.shape)

te=1/rate
n=data.size//2
print(n)
duree=n/rate
t=np.array([te*k for k in range(n)])

plt.plot(t,data[:,0])
plt.axis([0,duree,data.min(),data.max()])
plt.show()
print(duree)