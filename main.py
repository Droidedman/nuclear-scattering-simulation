import numpy as np
from schrodinger_solver import solve_schrodinger, normalize_wavefunction
from phase_shift_analysis import phase_shift_spectrum
from visualize_results import plot_wavefunction, plot_phase_shifts
from potential_models import woods_saxon

def main():
    E = 10.0
    l = 0
    r, u = solve_schrodinger(E, l, potential_func=woods_saxon, V0=50.0, R=5.0, a=0.65)
    u_norm = normalize_wavefunction(r, u)
    plot_wavefunction(r, u_norm, E, l)

    energies = np.linspace(5, 30, 6)
    E_vals, shifts = phase_shift_spectrum(energies, l, potential_func=woods_saxon, V0=50.0, R=5.0, a=0.65)
    plot_phase_shifts(E_vals, shifts, l)

if __name__ == "__main__":
    main()
