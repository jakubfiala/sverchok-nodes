"""
in source_vertices  v  
in num_waves        s  d=16 n=2
in period           s  d=1  n=2
in seed             s  d=0  n=2
out displaced       v
out bug             s
"""

# Random Wave function

import numpy as np
import random
import math

def displace_vertex_with_waves(vertex, t, waves):
    translated_vertex = np.array(list(vertex))

    for wave in waves:
        translated_vertex[2] = translated_vertex[2] + wave[0] * math.sin(wave[1] * t + wave[2])

    return tuple(list(translated_vertex))


if source_vertices:
    random.seed(seed)
    waves = [ (random.random(), random.random(), random.random()) for w in range(num_waves) ]
    displaced = [[ displace_vertex_with_waves(vertex, t * period, waves) for t, vertex in enumerate(source_vertices[0]) ]]

