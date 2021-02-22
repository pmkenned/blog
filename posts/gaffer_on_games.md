# Gaffer On Games Notes
TIMESTAMP: 1613719817

## Integration Basics

- [Source](https://gafferongames.com/post/integration_basics/)

### Semi-implicit Euler

- Update velocity before updating position
- This makes it a [symplectic integrator](https://en.wikipedia.org/wiki/Symplectic_integrator)

### Other integrations methods

- Implicit Euler
  - Good for stiff equations
  - Requires solving a system of equations per timestep
- Verlet integration
  - Greater accuracy, less memory when simulating large number of particles
  - Second order integrator, also symplectic
- Runge Kutta family
  - RK4 is much more accurate
  - Not necessarily the best

### RK4 Implementation in C++

### Semi-implicit euler vs. RK4

- In example of simple harmonic oscillator with no damping:
  - RK4 maintains the correct frequency but loses energy
  - Semi-implicit euler does a better job at conserving energy but drifts out of phase

### Summary

- Use semi-implicit euler

## What Every Programmer Needs To Know About Game Networking

- [Source](https://gafferongames.com/post/what_every_programmer_needs_to_know_about_game_networking/)
