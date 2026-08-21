"""
Coupled aircraft geometry and trajectory optimization via direct collocation
"""

import aerosandbox as asb
import aerosandbox.numpy as np

from src.config import PAYLOAD_MASS, RANGE, CRUISE_ALTITUDE, GRAVITY, BATTERY_SPECIFIC_ENERGY, PROP_EFFICIENCY

from src.geometry import wing_mass


"""
Problem setup and initializations
"""
N = 50          # Number of collocation intervals or discretization step size

opti = asb.Opti()

#-------- Static design variables --------
S = opti.variable(init_guess = 0.5 , lower_bound = 0.1)
AR = opti.variable(init_guess = 12, lower_bound = 5)
m_battery = opti.variable(init_guess = 1, lower_bound = 0.5)

#-------- Free mission duration --------
total_time = opti.variable(init_guess = 1000, lower_bound = 100)
dt = total_time / N

#-------- Trajectory decision variables --------
h = opti.variable(init_guess = 10, n_vars = N+1)
V = opti.variable(init_guess = 20, n_vars = N+1)
gamma = opti.variable(init_guess = 0.05, n_vars = N+1)
T = opti.variable(init_guess = 50, n_vars = N+1)
E = opti.variable(init_guess = 60000, n_vars = N+1)
x = opti.variable(init_guess = 1000, n_vars = N+1)

# ---- Derived total mass (constant, not per-point) ----- 
m_total = PAYLOAD_MASS + wing_mass(S) + m_battery

# ---- Boundary conditions ----                                
opti.subject_to(E[0] == m_battery * BATTERY_SPECIFIC_ENERGY)
opti.subject_to(E[N] >= 0)
opti.subject_to(h[0] == 0)
opti.subject_to(h[N] == CRUISE_ALTITUDE)
opti.subject_to(x[0] == 0)
opti.subject_to(x[N] == RANGE)