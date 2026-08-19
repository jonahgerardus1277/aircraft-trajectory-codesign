# Joint Optimization of Aircraft Geometry and Climb Trajectory using AeroSandbox and direct collocation

## 1. Purpose & Core Engineering Goal
- Integrated Aircraft Trajectory Co-Design mathematically unifies the vehicle sizing process (wing area, engine size) and operational trajectory (altitude, speed profiles) into a single, coupled optimization problem. Traditional design separates these steps, resulting in performance losses because static vehicle sizing cannot adapt to dynamic operational tradeoffs.

A comparsion between traditional sequential workflow vs integrated co-design workflow:

| Traditional Sequential Workflow (Decoupled) | Integrated Co-Design Workflow (Coupled) |
|-------------------------------------------- | --------------------------------------- |
| - **Sizing Phase:** Optimize wing geometry (S, AR) strictly for peak cruise aerodynamic efficiency | - **Joint Optimization:** solves geometry and flight path simultaneously via direct collocation|
| - **Operations Phase:** Find the optimal climb path for the fixed airframe | - **Synergy:** Accepts a slightly less efficient cruise wing if it yields high lift during climb, enabling a lighter engine |
| - **Flaw:** Cruise-optimized wing may be undersized for steep climbs, forcing oversized, heavy engines | - **Result:** Minimizes total mission fuel burn/ energy across the entire flight envelope| 

## 2. File definitions
- config.py:Top-Level Aircraft Requirements (TLARs) and physical constants for the aircraft-trajectory co-design problem.
- aerodynamics.py: Lift and drag coefficient models for the co-design problem
- dynamics.py: Point-mass flight mechanics: rate equations for altitude and airspeed
- geometry.py: Wing structural mass model: m_wing = f(S,AR)


## 3. Status Updates
- 8/19/2026 Commit: Defining project repository, README.md file, project definition, and added initial simple models defined in: aerodynamics.py, config.py, dynamics.py, geometry.py