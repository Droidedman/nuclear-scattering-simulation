import numpy as np
from potential_models import woods_saxon

hbar = 197.327  # MeV*fm
m_nucleon = 938.272  # nucleon mass

def schrodinger_rhs(r, y, l, E, mu, potential_func):
    u, uprime = y
    V = potential_func(r)
    k2 = 2.0 * mu * (E - V) / hbar**2 - l * (l + 1) / r**2
    return np.array([uprime, -k2 * u])

def rk4_step(f, r, y, h, *args):
    k1 = f(r, y, *args)
    k2 = f(r + h/2, y + h*k1/2, *args)
    k3 = f(r + h/2, y + h*k2/2, *args)
    k4 = f(r + h, y + h*k3, *args)
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6

def solve_schrodinger(E, l=0, r_min=0.01, r_max=15.0, dr=0.05, potential_func=woods_saxon, **kwargs):
    """Integrate the radial Schrödinger equation outward."""
    r_vals = np.arange(r_min, r_max, dr)
    u = np.zeros_like(r_vals)
    uprime = np.zeros_like(r_vals)
    u[0], uprime[0] = 0.0, 1e-5
    mu = m_nucleon / 2.0
    y = np.array([u[0], uprime[0]])

    for i in range(1, len(r_vals)):
        y = rk4_step(schrodinger_rhs, r_vals[i-1], y, dr, l, E, mu, lambda r: potential_func(r, **kwargs))
        u[i], uprime[i] = y

    return r_vals, u

def normalize_wavefunction(r, u):
    norm = np.trapz(u**2, r)
    return u / np.sqrt(norm) if norm != 0 else u
