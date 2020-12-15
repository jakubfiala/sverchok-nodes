"""ASCII Word to point multi-cloud function
"""
import numpy as np
import random
import math

from mathutils.noise import seed_set, random_unit_vector

def letter_to_vertices(letter, letter_vertices, letter_scale, position_scale, seed):
    vertices = []

    random.seed(letter + seed)
    position = (random.uniform(-1, 1) * position_scale, random.uniform(-1, 1) * position_scale)

    for v in range(letter_vertices):
        vertex = (random_unit_vector() * letter_scale)
        vertex[0] = vertex[0] + position[0]
        vertex[1] = vertex[1] + position[1]
        vertex[2] = 0
        vertices.append(vertex.to_tuple())

    return vertices

def sv_main(letters=[[]], letter_vertices=32, letter_scale=1, position_scale=10, seed=0):
    in_sockets = [
        ['s', 'letters', letters],
        ['s', 'letter_vertices', letter_vertices],
        ['s', 'letter_scale', letter_scale],
        ['s', 'position_scale', position_scale],
        ['s', 'seed', seed]]

    vertices = []

    if len(letters[0]) > 0:
        for letter_index, letter in enumerate(letters[0][0]):
            vertices = vertices + letter_to_vertices(letter,
                                                    letter_vertices,
                                                    letter_scale,
                                                    position_scale,
                                                    seed + letter_index)

    out_sockets = [['v', 'Vertices', [vertices]]]

    return in_sockets, out_sockets
