import numpy as np
import random
import math

def translate_by_distance(vertex, repulsors, strengths, vertex_id, repulsed):
    translated_vertex = np.array(list(vertex))

    nearest_repulsor_id = 0
    cur_distance = np.linalg.norm(translated_vertex - np.array(list(repulsors[0])))

    for rid, repulsor in enumerate(repulsors):
        distance = np.linalg.norm(translated_vertex - np.array(list(repulsor)))
        if distance < cur_distance:
            nearest_repulsor_id = rid
            cur_distance = distance
    
    nearest_repulsor = repulsors[nearest_repulsor_id]

    if cur_distance < strengths[0][nearest_repulsor_id]:
        repulsed.append(vertex_id)
        r = np.array(list(nearest_repulsor))
        p = translated_vertex

        diff = p - r
        ratio = strengths[0][nearest_repulsor_id] / cur_distance
        translated_vertex = p - (diff - diff * ratio)
    
    translated_vertex[2] = min(translated_vertex[2] + cur_distance, 1.0)

    return tuple(list(translated_vertex))

def sv_main(source_vertices=[[]], source_edges=[[]], source_faces=[[]], repulsors=[[]], repulsor_strengths=[[]]):

    in_sockets = [
        ['v', 'source vertices', source_vertices],
        ['s', 'source edges', source_edges],
        ['s', 'source faces', source_faces],
        ['v', 'repulsor centres', repulsors],
        ['s', 'repulsor strengths', repulsor_strengths]]

    vertices = []
    edges = []
    faces = []

    repulsed = []
    vertices = [ translate_by_distance(v, repulsors[0], repulsor_strengths[0], vi, repulsed) for vi, v in enumerate(source_vertices[0]) ]

    edges = [ edge for edge in source_edges[0] if not (edge[0] in repulsed and edge[1] in repulsed) ]

    faces = [ face for face in source_faces[0] 
                if not (face[0] in repulsed and face[1] in repulsed and face[2] in repulsed and face[3] in repulsed) ]

    out_sockets = [
        ['v', 'vertices', [vertices]],
        ['s', 'edges', [edges]],
        ['s', 'faces', [faces]],
        ['s', 'Debug', repulsor_strengths]
    ]

    return in_sockets, out_sockets
