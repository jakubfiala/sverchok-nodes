"""Random Wave function
"""
import numpy as np
import random
import math

def displace_vertex_with_waves(vertex, t, waves):
    translated_vertex = np.array(list(vertex))

    for wave in waves:
        translated_vertex[2] = translated_vertex[2] + wave[0] * math.sin(wave[1] * t + wave[2])

    return tuple(list(translated_vertex))

def sv_main(source_vertices=[[]], num_waves=16, period=1, seed=0):
    in_sockets = [
        ['v', 'source vertices', source_vertices],
        ['s', 'number of waves', num_waves],
        ['s', 'period', period],
        ['s', 'seed', seed]]

    random.seed(seed)

    waves = [ (random.random(), random.random(), random.random()) for w in range(num_waves) ]
    displaced = [ displace_vertex_with_waves(vertex, t * period, waves) for t, vertex in enumerate(source_vertices[0]) ]

    out_sockets = [
        ['v', 'Displaced vertices', [displaced]],
        ['s', 'Debug', []]
    ]

    return in_sockets, out_sockets
