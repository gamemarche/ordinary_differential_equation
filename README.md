# Ordinary Differential Equations (ODE) - PythonLab Codes

This repository contains the official Python source code for the book *Ordinary Differential Equations for Engineers: Fundamentals and Applications*.

## How to Use

### 1. Requirements
- Python 3.10 or higher
- Required packages:
  ```bash
  pip install numpy scipy sympy matplotlib
  ```

### 2. Clone the Repository
```bash
git clone https://github.com/gamemarche/ordinary_differential_equation.git
cd ordinary_differential_equation
```

### 3. Folder Structure & Chapter Contents

```text
├── vol1/
│   ├── chapter1.py   # Ch.1 — Direction Fields & Euler's Method
│   ├── chapter2.py   # Ch.2 — First-Order ODEs: Solution Methods (sympy dsolve/classify_ode)
│   ├── chapter3.py   # Ch.3 — RC Circuit Simulation & Logistic Growth
│   ├── chapter4.py   # Ch.4 — Wronskian & Linear Independence
│   ├── chapter5.py   # Ch.5 — Verifying Particular Solutions with sympy
│   └── chapter6.py   # Ch.6 — Damped/Forced Vibration & Resonance
└── vol2/
    ├── chapter7.py   # Ch.7 — Systems of Linear ODEs & Phase Portraits (Trace-Determinant Classification)
    ├── chapter8.py   # Ch.8 — Non-linear Systems: Lotka-Volterra Predator-Prey Model & Conservation Law H(x,y)
    ├── chapter9.py   # Ch.9 — Power-Series Solutions of Airy Equation y'' - x*y = 0 vs. Exact Airy Functions
    └── chapter10.py  # Ch.10 — Special Functions: Bessel Functions (J0~J3), Legendre Polynomials (P0~P4) & Orthogonality
```

Each `chapterN.py` file corresponds to the "Python Lab" section at the end of Chapter N in the book, and reproduces the figures/results discussed in that chapter.

#### Detailed Descriptions of Vol. 2
- **`vol2/chapter7.py`**: Phase-plane analysis for 2D linear systems $y' = Ay$. Features automatic phase portrait classification (Stable Node, Saddle Point, Spiral, Center) using the trace-determinant test (Theorem 7.10) and visualizes trajectories via `matplotlib.pyplot.streamplot`.
- **`vol2/chapter8.py`**: Simulation of non-linear ODE systems using the Lotka-Volterra Predator-Prey model (Equations 8.49–8.50). Uses `scipy.integrate.solve_ivp` (RK45) for numerical integration, plots time series and phase-plane orbits, and verifies numerical conservation of energy $H(x, y)$.
- **`vol2/chapter9.py`**: Truncated power-series solution of the Airy differential equation $y'' - xy = 0$ (Example 9.5). Compares series expansions ($N = 10, 20, 40$) against exact $Ai(x)$ from `scipy.special.airy` and analyzes truncation errors.
- **`vol2/chapter10.py`**: Implementation of special functions using `scipy.special`. Features Bessel functions $J_0 \sim J_3$ with positive roots (`jn_zeros`), Legendre polynomials $P_0 \sim P_4$, numerical orthogonality validation via `scipy.integrate.quad`, and root refinement using `scipy.optimize.brentq`.

### 4. Running a Script
```bash
# Run a script from Vol. 1
python vol1/chapter1.py

# Run a script from Vol. 2
python vol2/chapter7.py
```
Each script will:
- Print numerical results (errors, comparisons, symbolic verification, classification parameters, etc.) to the console.
- Display plots (direction fields, phase portraits, solution curves, error graphs, special function plots) via `matplotlib`.

### 5. Notes
- Required libraries for each chapter are listed as imports and comments at the top of each `.py` file.
- These labs are designed as a **companion to the theory** to visualize and numerically verify derived mathematical results. Feel free to modify parameters and rerun to explore the "Exploration Problems" at the end of each lab.
- If you encounter a `ModuleNotFoundError`, make sure all packages from Step 1 (`numpy`, `scipy`, `sympy`, `matplotlib`) are installed in your Python environment.

## License
This project is licensed under the [MIT License](LICENSE).
