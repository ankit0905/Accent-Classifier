import os
import numpy as np

def generate_y(folder):
    accents = {}
    y = []
    index = 0
    # folder = '/media/enigmaeth/My Passport/sounds_wav/'

    for filename in os.listdir(folder):
        name = ''.join([i for i in filename if not i.isdigit()])
        name = name.split('.')[0]
        if name not in accents:
            accents[name] = index
            index += 1
        y.append(accents[name])

    return np.reshape(np.array(y), (len(y), 1))