import numpy as np
from schrodinger_solver import solve_schrodinger
from potential_models import woods_saxon

hbar = 197.327
m_nucleon = 938.272

def phase_shift(E, l=0, potential_func=woods_saxon, **kwargs):
    """Rough estimate of phase shift from asymptotic wavefunction."""
    r, u = solve_schrodinger(E, l, potential_func=potential_func, **kwargs)
    r_tail = r[-100:]
    u_tail = u[-100:]
    k = np.sqrt(2 * m_nucleon * E) / hbar
    phase = np.arctan2(np.sin(k * r_tail[-1]), np.cos(k * r_tail[-1]))
    return np.degrees(phase)

def phase_shift_spectrum(E_values, l=0, potential_func=woods_saxon, **kwargs):
    shifts = []
    for E in E_values:
        shift = phase_shift(E, l, potential_func, **kwargs)
        shifts.append(shift)
    return np.array(E_values), np.array(shifts)
