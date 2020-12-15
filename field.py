import random
import math

def generate_random_point(scale=1):
    radius = random.random() * scale
    angle = random.random() * math.pi * 2

    point = (
            math.sin(angle) * radius,
            math.cos(angle) * radius,
            0
        );
    return point

def randscale(vertices):
    scale = random.random()
    new_vertices = []
    for v in vertices:
        new_vertices.append(tuple([ dim * scale for dim in v ]))
    return new_vertices

def translate(vertex, point):
    out_vertex = [ vertex[dim] + point[dim] for dim, v in enumerate(vertex) ]
    return tuple(out_vertex)

def translate_vertices_to_point(vertices, point):
    translated_vertices = [ translate(v, point) for v in randscale(vertices) ]
    return translated_vertices

def translate_edges(edges, i):
    offset = i * (len(edges))
    return [ [e[0] + offset, e[1] + offset] for e in edges ]

def translate_faces(faces, i):
    offset = i * (len(faces))
    return [ [dim + offset for dim in f] for f in faces ]

def sv_main(in_vertices=[[]], in_edges=[[]], in_faces=[[]], N=100, scale=1, seed=0):
    in_sockets = [
        ['v', 'in_vertices', in_vertices],
        ['s', 'in_edges', in_edges],
        ['s', 'in_faces', in_faces],
        ['s', 'N', N],
        ['s', 'scale', scale],
        ['s', 'Random Seed', seed]]

    random.seed(seed)

    # press Ctrl+I, look in console
    vertices=[]
    edges=[]
    faces=[]
    for i in range(N):
        point = generate_random_point(scale=scale)
        vertices = vertices + translate_vertices_to_point(in_vertices[0], point)
        edges = edges + translate_edges(in_edges[0], i)
        for ei in range(len(edges)):
            faces = faces + translate_faces(in_faces[0], i)

    out_sockets = [
        ['v', 'Vertices', [vertices]],
        ['s', 'Edges', [edges]],
        ['s', 'Faces', [faces]],
        ['s', 'Debug', translate_edges(in_edges[0], 1)]
    ]

    return in_sockets, out_sockets
