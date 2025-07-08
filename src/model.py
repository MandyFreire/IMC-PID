import numpy as np

def process_model(y, t, u, Kp, tau, theta):
    """
    Modelo de um sistema de primeira ordem com tempo morto.
    """
    dydt = (-(y - u) + Kp * u) / tau
    if t < theta:
        dydt = 0
    return dydt
