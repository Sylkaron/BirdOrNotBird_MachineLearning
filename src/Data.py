import scipy.io.wavfile as wave
import matplotlib.pyplot as plt
import numpy as np

rate,data=wave.read("D://dev//Pycharm-project//BirdOrNotBird_MachineLearning//Ressources//wav//55.wav")

print(data.shape)

te=1/rate
n=data.shape[0]
print(n)
duree=n/rate
print(duree)
t=np.array([te*k for k in range(n)])

def tracerSpectre(data, rate, debut, duree):
    start = int(debut * rate)
    stop = int((debut + duree) * rate)
    spectre = np.absolute(np.fft.fft(data[start:stop]))
    spectre = spectre / spectre.max()
    n = spectre.size
    print(n)
    freq = np.zeros(n)
    for k in range(n):
        freq[k] = 1.0 / n * rate * k
    print(freq)
    plt.vlines(freq, [0], spectre, 'r')
    plt.xlabel('f (Hz)')
    plt.ylabel('A')
    plt.axis([0, 0.5 * rate, 0, 1])
    plt.grid()

plt.figure(figsize=(12, 4))
tracerSpectre(data, rate, 0.0, 10.0)
plt.axis([0, 8000, 0, 1])
plt.show()