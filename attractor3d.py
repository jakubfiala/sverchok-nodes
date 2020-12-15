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

def prune_by_distance(vertex, attractors, vertex_id, threshold):
    translated_vertex = np.array(list(vertex))

    a_attractors = np.zeros(shape=(len(attractors), len(attractors[0])))
    # translate attractor coords from tuples into ndarray values
    for ri in range(len(attractors)):
        # we only use the XY position of each attractor
        a_attractors[ri][0] = attractors[ri][0]
        a_attractors[ri][1] = attractors[ri][1]
        a_attractors[ri][2] = attractors[ri][2]

    nn = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(a_attractors)
    distances, indices = nn.kneighbors(np.array([translated_vertex]))
    dist_magnitude = np.linalg.norm(distances)

    return dist_magnitude > threshold

def sv_main(source_vertices=[[]], attractors=[[]], threshold=5):
    in_sockets = [
        ['v', 'source vertices', source_vertices],
        ['v', 'attractor centres', attractors],
        ['s', 'distance threshold', threshold]]

    vertices = []
    edges = []
    faces = []

    # translate source vertices using the attractors
    vertices = [ v for vi, v in enumerate(source_vertices[0]) if prune_by_distance(v, attractors[0], vi, threshold) ]

    out_sockets = [
        ['v', 'vertices', [vertices]],
        ['s', 'Debug', []]
    ]

    return in_sockets, out_sockets
