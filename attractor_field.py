"""Attractor Field

This Sverchok scripted node applies an "attractor field" to another
collection of vertices. This means that the source vertices are going
to be displaced along the Z axis, as if being attracted to the nearby
attractor vertices.

Under the hood this node uses sklearn's kth nearest neighbour implementation.
"""
import numpy as np
import random
import math
from sklearn.neighbors import NearestNeighbors

def translate_by_distance(vertex, attractors, vertex_id):
    translated_vertex = np.array(list(vertex))

    a_attractors = np.zeros(shape=(len(attractors), len(attractors[0])))
    # translate attractor coords from tuples into ndarray values
    for ri in range(len(attractors)):
        # we only use the XY position of each attractor
        a_attractors[ri][0] = attractors[ri][0]
        a_attractors[ri][1] = attractors[ri][1]

    nn = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(a_attractors)
    distances, indices = nn.kneighbors(np.array([translated_vertex]))
    dist_magnitude = np.linalg.norm(distances)

    translated_vertex[2] = translated_vertex[2] - min(2, math.pow(dist_magnitude,2))

    return tuple(list(translated_vertex))

def sv_main(source_vertices=[[]], source_edges=[[]], source_faces=[[]], attractors=[[]]):
    in_sockets = [
        ['v', 'source vertices', source_vertices],
        ['s', 'source edges', source_edges],
        ['s', 'source faces', source_faces],
        ['v', 'attractor centres', attractors]]

    vertices = []
    edges = []
    faces = []
    
    # translate source vertices using the attractors
    vertices = [ translate_by_distance(v, attractors[0], vi) for vi, v in enumerate(source_vertices[0]) ]

    out_sockets = [
        ['v', 'vertices', [vertices]],
        ['s', 'edges', [source_edges]],
        ['s', 'faces', [source_faces]],
        ['s', 'Debug', []]]
    ]

    return in_sockets, out_sockets
