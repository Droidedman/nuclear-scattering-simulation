# Nuclear Scattering Simulation

This repository provides a **numerical solver for the radial Schrödinger equation** using the **fourth-order Runge–Kutta (RK4)** method.  
It models **nucleon–nucleus scattering** in a **Woods–Saxon potential**, computes **radial wavefunctions**, and performs a **basic phase shift analysis** for multiple energies.

The project is built as a modular, reproducible codebase for theoretical and computational nuclear physics research.

---

## 🧠 Background

In nuclear physics, understanding scattering behavior between nucleons and nuclei helps extract information about the **nuclear optical potential**.  
The radial Schrödinger equation for a spherically symmetric potential is given by:

\[
\frac{d^2u}{dr^2} = \frac{2\mu}{\hbar^2}[V(r) - E]u + \frac{l(l+1)}{r^2}u
\]

where:

- \(u(r)\): reduced radial wavefunction  
- \(\mu\): reduced mass  
- \(E\): projectile energy (MeV)  
- \(l\): angular momentum quantum number  
- \(V(r)\): potential (MeV)

This solver integrates the equation using **Runge–Kutta 4th order** and visualizes results for various partial waves.

---

## 🧩 Features

- Solves the **radial Schrödinger equation** using RK4 integration  
- Supports **multiple potentials**:
  - Woods–Saxon (default)
  - Square well
  - Harmonic oscillator
- Computes **normalized wavefunctions**  
- Performs **phase shift analysis vs. energy**  
- Modular file structure for easy research extensions  

---

## 📂 Directory Structure

nuclear-scattering-simulation/
│
├── main.py # Entry point to run the simulation
├── schrodinger_solver.py # Core solver using RK4
├── potential_models.py # Contains potential definitions
├── phase_shift_analysis.py # Calculates phase shifts vs. energy
├── visualize_results.py # Handles plotting and visualization
└── README.md # Documentation (this file)

yaml
Copy code

---

## ⚙️ Installation

Requires **Python 3.8+** and the following dependencies:

```bash
pip install numpy matplotlib
▶️ Running the Simulation
Execute the main script to compute the wavefunction and phase shift:

bash
Copy code
python main.py
It will:

Integrate the radial Schrödinger equation for 
𝐸
=
10
E=10 MeV, 
𝑙
=
0
l=0

Plot the normalized radial wavefunction

Compute and plot the phase shift vs. energy curve for multiple energies

📊 Example Output
1. Radial Wavefunction (E = 10 MeV, l = 0)
Shows the shape of the normalized wavefunction inside and outside the potential well.

Copy code
u(r)
│         /‾‾‾‾‾\
│       /         \__
│     /
└─────────────────────────── r (fm)
2. Phase Shift vs Energy
Displays variation of phase shift with increasing energy — helpful to identify resonance-like behavior.

Energy (MeV)	Phase Shift (deg)
5.0	18.5
10.0	29.2
15.0	41.6
20.0	50.7
25.0	58.0

🧮 Physics & Numerical Details
Woods–Saxon Potential
𝑉
(
𝑟
)
=
−
𝑉
0
1
+
𝑒
(
𝑟
−
𝑅
)
/
𝑎
V(r)=− 
1+e 
(r−R)/a
 
V 
0
​
 
​
 
Typical parameters:

𝑉
0
=
50
V 
0
​
 =50 MeV

𝑅
=
5.0
R=5.0 fm

𝑎
=
0.65
a=0.65 fm

Integration Details
Range: 
𝑟
=
0.01
r=0.01–
15.0
15.0 fm

Step size: 
𝑑
𝑟
=
0.05
dr=0.05 fm

Normalization via numerical integration using trapezoidal rule

🧰 Function Overview
File	Purpose
potential_models.py	Defines potential models (Woods–Saxon, Square Well, Harmonic Oscillator)
schrodinger_solver.py	RK4 solver for the radial equation and normalization routines
phase_shift_analysis.py	Extracts approximate phase shift from asymptotic behavior
visualize_results.py	Handles all plotting and graph generation
main.py	Central script — runs solver, normalization, and visualization

💡 Applications
Study of optical model and scattering phenomena

Foundation for nuclear reaction theory analysis

Ideal example for computational physics coursework

Serves as a base for extending toward cross-section calculations

🧩 Example Configuration (editable in main.py)
python
Copy code
E = 20.0       # Energy in MeV
l = 1          # Angular momentum
V0 = 50.0      # Potential depth
R = 5.0        # Nuclear radius
a = 0.65       # Diffuseness
You can change these values to simulate different physical systems or test numerical convergence.

👨‍🔬 Author
Dewang Sukhadare
Ph.D. Candidate — Theoretical Nuclear Physics
Amity University, Mumbai, India

Email: sukhadarewango38@gmail.com

LinkedIn: linkedin.com/in/dewang-sukhadare

⚖️ License
Released under the MIT License (2025) — free for educational and research use with attribution.

🧭 Keywords
nuclear-physics • scattering • radial-schrodinger • woods-saxon • computational-physics • phase-shift • rk4 • wavefunction

pgsql
Copy code
