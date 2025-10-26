
# Nuclear Scattering Simulation

This repository contains a Python-based numerical solver for the **radial Schrödinger equation** in a **Woods–Saxon potential**, using the **fourth-order Runge–Kutta (RK4)** integration method.  
It models **nucleon–nucleus scattering**, computes **normalized wavefunctions**, and performs a **simple phase shift analysis** for various incident energies.

---

## 🧠 Background

For a spherically symmetric potential, the radial Schrödinger equation is given by:

\[
\frac{d^2u}{dr^2} = \frac{2\mu}{\hbar^2}[V(r) - E]u + \frac{l(l+1)}{r^2}u
\]

where:
- \( u(r) \) is the reduced radial wavefunction,
- \( \mu \) is the reduced mass of the system,
- \( E \) is the kinetic energy of the incident particle,
- \( V(r) \) is the nuclear potential, modeled here as a Woods–Saxon function.

The **Woods–Saxon potential** is defined as:

\[
V(r) = -\frac{V_0}{1 + e^{(r - R)/a}}
\]

---

## 🧩 Features

- Modular Python design — clean separation of solver, potentials, visualization, and phase-shift analysis.
- Supports **multiple potentials**:
  - Woods–Saxon
  - Square Well
  - Harmonic Oscillator
- Computes **bound and scattering wavefunctions**
- Produces **phase shift vs. energy** plots
- Can be easily extended to test parameter dependencies or fit experimental data

---

## 📂 Directory Structure

