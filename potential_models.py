import numpy as np

# Woods-Saxon potential
def woods_saxon(r, V0=50.0, R=5.0, a=0.65):
    """Woods-Saxon nuclear potential."""
    return -V0 / (1.0 + np.exp((r - R) / a))

# Square well potential
def square_well(r, V0=50.0, R=5.0):
    """Square well potential for testing."""
    return np.where(r < R, -V0, 0.0)

# Harmonic oscillator potential
def harmonic_oscillator(r, k=5.0):
    """Simple harmonic oscillator potential."""
    return 0.5 * k * r**2
