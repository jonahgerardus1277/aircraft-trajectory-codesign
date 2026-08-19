"""
Wing structural mass model: m_wing = f(S,AR)
"""

from src.config import WING_MASS_PER_AREA



def wing_mass(S):
    """
    Estimate wing structural mass from wing area

    Parameters:
    S: float 

    Returns:
    m_wing: float

    """

    m_wing = WING_MASS_PER_AREA * S

    return m_wing