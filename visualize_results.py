import matplotlib.pyplot as plt

def plot_wavefunction(r, u, E, l):
    plt.figure(figsize=(7,5))
    plt.plot(r, u, lw=1.5)
    plt.title(f"Radial Wavefunction (E = {E} MeV, l = {l})")
    plt.xlabel("r (fm)")
    plt.ylabel("u(r)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_phase_shifts(E_values, shifts, l):
    plt.figure(figsize=(7,5))
    plt.plot(E_values, shifts, marker='o')
    plt.title(f"Phase Shift vs Energy (l = {l})")
    plt.xlabel("Energy (MeV)")
    plt.ylabel("Phase Shift (degrees)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
