import numpy as np

from config import SAMPLE_RATE

def sine_wave(FREQUENCIA, DURACAO):

    NUMERO_AMOSTRAS = int(SAMPLE_RATE * DURACAO)

    TEMPO = np.linspace(0, DURACAO, NUMERO_AMOSTRAS)

    WAVE = np.sin(2 * np.pi * FREQUENCIA * TEMPO)

    return WAVE