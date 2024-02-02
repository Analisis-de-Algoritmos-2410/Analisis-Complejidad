import matplotlib.pyplot as plt
import pandas as pd
from Persona import Persona
import random
import time
from search import busqueda_binaria, busqueda_lineal


def generar_reporte(arr):
    n = 1000
    tiempos = {'binaria': [], 'lineal': []}
    for x in range(1, n):
        censo = Persona.generar_censo(x)
        persona = random.choice(censo)

        # binaria
        inicio = time.perf_counter()
        busqueda_binaria(0, len(censo) - 1, censo, persona.id)
        fin = time.perf_counter()
        tiempos['binaria'].append(fin - inicio)

        # lineal
        inicio = time.perf_counter()
        busqueda_lineal(censo, persona.nombre)
        fin = time.perf_counter()
        tiempos['lineal'].append(fin - inicio)

    df = pd.DataFrame(tiempos)
    df.index.name = 'n'
    df.reset_index(inplace=True)

    plt.plot(df['n'], df['binaria'], label='binaria')
    plt.plot(df['n'], df['lineal'], label='lineal')

    plt.legend()
    plt.xlabel('n')
    plt.ylabel('Tiempo (s)')
    plt.title('Tiempos de ejecución')
    plt.show()

