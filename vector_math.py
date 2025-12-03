import numpy as np

def add_vectors(v1, v2):
    return np.array(v1) + np.array(v2)

def subtract_vectors(v1, v2):
    return np.array(v1) - np.array(v2)

def dot_product(v1, v2):
    return np.dot(v1, v2)

def magnitude(v):
    return np.linalg.norm(v)

def normalize(v):
    v = np.array(v)
    mag = np.linalg.norm(v)
    if mag == 0:
        return np.array([0, 0, 0])
    return v / mag
