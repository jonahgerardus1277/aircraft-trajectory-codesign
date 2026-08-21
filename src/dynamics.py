"""
Point-mass flight mechanics: rate equations for altitude and airspeed
"""

from src.config import GRAVITY, AIR_DENSITY
import math

def drag_force(CD, V, S):
    """
    Compute drag force from drag coefficient

    Parameters:
    CD: float
    V: float
    S: float

    Returns:
    D: float
    """
    D = 0.5 * AIR_DENSITY * V**2 * S * CD
    return D


def climb_rate(V, gamma):
    """
    Rate of change of altitude (dh/dt)
    """

    dh_dt = V * math.sin(gamma)
    return dh_dt

def acceleration(T, D, m, gamma):
    """
    Rate of change of airspeed (dV/dt)
    """

    dV_dt = (T - D)/m - GRAVITY*math.sin(gamma)
    return dV_dt

def downrange_rat(V, gamma):
    """
    Rate of change of downrange distance (dx/dt)
    """
    dx_dt = V * math.cos(gamma)
    return dx_dt

def power_required(T, V, eta_prop):
    """
    Electrical power draw from the battery
    """

    P = T * V/eta_prop
    return P