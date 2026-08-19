"""
Lift and drag coefficient models for the co-design problem
"""

from src.config import GRAVITY, AIR_DENSITY, CD0, OSWALD_EFF
import math

def lift_coefficient(m, V, S):
    """
    Compute lift coefficient for quasi-steady level flight

    Parameters:
    m: float
    V: float
    S: float

    Returns:
    CL: float
    """

    CL = 2 * m * GRAVITY / (AIR_DENSITY * V**2 * S)
    return CL

def drag_coefficient(CL, AR):
    """
    Compute drag coefficient from parabolic drag polar

    Parameters:
    CL: float
    AR: float

    Returns:
    CD: float
    """

    CD = CD0 + CL**2/(math.pi * AR * OSWALD_EFF)
    return CD