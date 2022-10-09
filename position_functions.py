import numpy as np

def svt(S0, v, t):
    return (S0 + (v*t))

def svt2(S0, v, t, g):
    return (S0 + (v*t) - ((g*(t**2))/2))

def t_trajetoria(S0y, Sfy, Vy, g):
    a = g/2
    b = -(Vy)
    c = (Sfy - S0y)
    p = np.array([a, b, c])
    return np.roots(p)[0]