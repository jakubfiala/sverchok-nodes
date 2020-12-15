"""Gauss Map
"""
import numpy as np
import random
import math
from scipy.stats import multivariate_normal

def pdfmap(vertex, norms, index):
    translated_vertex = np.array(list(vertex))
    pdf = 0

    for norm in norms:
        pdf = pdf + norm.pdf(translated_vertex[:2])

    return (0, 0, pdf)


def sv_main(source_vertices=[[]], means=[[]], standard_deviations=[[]]):
    in_sockets = [
        ['v', 'source vertices', source_vertices],
        ['v', 'gaussian means', means],
        ['s', 'standard devs', standard_deviations]]

    norms = [ multivariate_normal(list(mean[:2]), standard_deviations[0][0][m_index])
              for m_index, mean in enumerate(means[0]) ]

    # translate source vertices using the attractors
    gauss_map = [ pdfmap(v, norms, vi) for vi, v in enumerate(source_vertices[0]) ]

    out_sockets = [
        ['v', 'Density map', [gauss_map]],
        ['s', 'Debug', []]
    ]

    return in_sockets, out_sockets
