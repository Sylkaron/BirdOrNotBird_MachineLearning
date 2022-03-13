import scipy.io.wavfile as wave
import matplotlib.pyplot as plt
import numpy as np

rate,data=wave.read("D:\Documents\ProjetML\wav//55.wav")

print(data.shape)

te=1/rate
n=data.shape[0]
print(n)
duree=n/rate
t=np.array([te*k for k in range(n)])

"""plt.plot(t,data)
plt.legend()
plt.axis([0,duree,data.min(),data.max()])
plt.show()
print(duree)"""


def tracerSpectre(data, rate, debut, duree):
    start = int(debut * rate)
    stop = int((debut + duree) * rate)
    spectre = np.absolute(np.fft.fft(data[start:stop]))
    print(stop)
    spectre = spectre / spectre.max()
    n = spectre.size
    freq = np.zeros(n)
    for k in range(n):
        freq[k] = 1.0 / n * rate * k
    plt.vlines(freq, [0], spectre, 'r')
    plt.xlabel('f (Hz)')
    plt.ylabel('A')
    plt.axis([0, 0.5 * rate, 0, 1])
    plt.grid()


plt.figure(figsize=(12, 4))
tracerSpectre(data, rate, 0.0, 11.0)
plt.axis([0, 800, 0, 1])
plt.show()