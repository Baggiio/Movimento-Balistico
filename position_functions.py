import numpy as np
import math as m

def mod(Vx, Vy):
    return m.sqrt((Vx**2) + (Vy**2))

def velocidade(V0, g, t):
    return (V0 - (g*t))

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