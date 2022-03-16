

import numpy as np
import sklearn as sk
import scipy as sp

import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf


dataBirdPresence = pd.read_csv('../Ressouces/ff1010bird_metadata.csv', index_col = 'itemid')

def reseauKeras(data):
    global neuron
    global optimiseur

    neuron = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation = 'relu', input_shape = tailleEntree),
    tf.keras.layers.Dropout(0.3, seed = 2),
    tf.keras.layers.Dense(64, activation = 'swish'),
    tf.keras.layers.Dense(64, activation = 'relu'),
    tf.keras.layers.Dense(64, activation = 'swish'),
    tf.keras.layers.Dense(64, activation = 'relu'),
    tf.keras.layers.Dense(64, activation = 'swish'),
    tf.keras.layers.Dense(1)])

    optimiseur = tf.keras.optimizers.RMSprop(learning_rate=0.001)
    neuron.compile(loss = tf.keras.losses.MeanSquaredError(),
                   optimizer = optimiseur,
                   metrics = ['mae'])

    return
