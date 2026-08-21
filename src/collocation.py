def trapezoidal_defect(state, rate, dt, N):
    """
    Computes the resulting integration using the trapezoidal method
    """
    defects = []
    for i in range(N):
        defect = (state[i+1] - state[i]) - (dt/2) * (rate[i] + rate[i+1])
        defects.append(defect)
    return defects