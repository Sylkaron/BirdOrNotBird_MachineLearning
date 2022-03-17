

import numpy as np
import sklearn as sk
import scipy as sp

import pandas as pd
import matplotlib.pyplot as plt

dfBird = pd.read_csv('..//Ressources//ff1010bird_metadata.csv')
dfBird.set_index('itemid',inplace=True)
