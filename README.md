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

---

### Detailed Descriptions of Vol. 1

- **`vol1/chapter1.py`**:
  - **Direction Fields**: Visualizes the direction field of $y' = y - x$ using `np.meshgrid` and normalized vector arrows via `matplotlib.pyplot.quiver`.
  - **Euler's Method**: Implements Euler's numerical integration for $y' = 2y - x, y(0) = 1$. Compares numerical trajectories across step sizes ($h = 0.5, 0.1, 0.01$) against the exact analytical solution $y(x) = \frac{x}{2} + \frac{1}{4} + \frac{3}{4}e^{2x}$ and evaluates numerical truncation errors at $x = 1$.

- **`vol1/chapter2.py`**:
  - **First-Order ODE Solution Methods**: Uses `sympy` to classify (`classify_ode`) and solve (`dsolve`) three fundamental first-order ODE types: Separable ($y' = x/y$), Linear ($y' + y/x = x^2$), and Bernoulli ($y' + y/x = x y^2$).
  - **Symbolic Verification**: Computes residuals of hand-derived solutions to confirm exact equivalence with SymPy's automated output.

- **`vol1/chapter3.py`**:
  - **RC Circuit Simulation**: Solves the charging equation $R \frac{dQ}{dt} + \frac{Q}{C} = E_0$ using `scipy.integrate.solve_ivp` (RK45) and compares against the theoretical step response $Q(t) = E_0 C (1 - e^{-t/\tau})$ with time constant $\tau = RC$.
  - **Logistic Population Growth**: Simulates $dP/dt = k P (1 - P/M)$ for varying rate constants $k$ and carrying capacities $M$, demonstrating asymptotic convergence toward equilibrium.

- **`vol1/chapter4.py`**:
  - **Wronskian & Linear Independence**: Implements a symbolic Wronskian function $W(y_1, y_2)(x) = y_1 y_2' - y_1' y_2$ in SymPy and evaluates it at test points (Theorem 4.3) to test linear independence of solution pairs.
  - **Characteristic Equation Case Analysis**: Verifies solutions corresponding to distinct real roots ($y'' - 3y' + 2y = 0$) and repeated real roots ($y'' - 4y' + 4y = 0$, Theorem 4.5).

- **`vol1/chapter5.py`**:
  - **Nonhomogeneous Linear ODEs**: Verifies particular solutions $y_p(x)$ derived by hand via Undetermined Coefficients ($y'' - 3y' + 2y = e^{3x}$) and Variation of Parameters ($y'' + y = \sec x$).
  - **Symbolic Residue Check**: Substitutes $y_p$ back into differential operators $L[y]$ to prove $L[y_p] - f(x) = 0$, and solves Initial Value Problems (IVPs) using `sympy.dsolve`.

- **`vol1/chapter6.py`**:
  - **Free Damped Vibrations**: Simulates second-order mechanical system $m y'' + c y' + k y = 0$ under three damping regimes: Underdamped ($\zeta < 1$), Critically Damped ($\zeta = 1$), and Overdamped ($\zeta > 1$), illustrating transient decay behavior (Theorem 6.1).
  - **Forced Vibration & Resonance Curves**: Computes steady-state response amplitude $M(\omega)$ across driving frequencies $\omega$ and damping ratios $\zeta$, marking practical resonance peaks $\omega_r = \omega_0 \sqrt{1 - 2\zeta^2}$ (Sections 6.4).

---

### Detailed Descriptions of Vol. 2

- **`vol2/chapter7.py`**:
  - **Phase-Plane Analysis**: Visualizes 2D linear systems $y' = Ay$ using `matplotlib.pyplot.streamplot`.
  - **Trace-Determinant Classification**: Implements automatic phase portrait classification (Stable/Unstable Node, Saddle Point, Stable/Unstable Spiral, Degenerate Node, Center) using the trace-determinant test (Theorem 7.10).

- **`vol2/chapter8.py`**:
  - **Nonlinear Systems & Predator-Prey Model**: Simulates the Lotka-Volterra equations ($dx/dt = \alpha x - \beta xy$, $dy/dt = \delta xy - \gamma y$) using `scipy.integrate.solve_ivp` (RK45).
  - **Conservation Law**: Plots time series and closed phase-space orbits, and numerically verifies the conservation of the invariant $H(x, y) = \delta x - \gamma \ln x + \beta y - \alpha \ln y$.

- **`vol2/chapter9.py`**:
  - **Power-Series Solutions of Airy Equation**: Solves $y'' - xy = 0$ (Example 9.5) using power-series recurrence relations ($a_{n+2} = a_{n-1} / [(n+2)(n+1)]$).
  - **Error & Convergence Analysis**: Compares truncated series approximations ($N = 10, 20, 40$) with the exact Airy function `scipy.special.airy` across $x \in [-6, 4]$ and analyzes logarithmic error decay with respect to series order $N$.

- **`vol2/chapter10.py`**:
  - **Special Functions**: Computes Bessel functions of the first kind $J_0(x) \sim J_3(x)$ with exact positive roots marked using `scipy.special.jn_zeros`.
  - **Legendre Polynomials & Orthogonality**: Generates Legendre polynomials $P_0(x) \sim P_4(x)$ and numerically verifies orthogonality $\int_{-1}^1 P_m(x) P_n(x) dx = \frac{2}{2n+1}\delta_{mn}$ using `scipy.integrate.quad`.
  - **Root Refinement**: Finds roots of $J_0(x)$ manually using `scipy.optimize.brentq` and compares results against `scipy.special`.

---

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

---

### 5. Notes
- Required libraries for each chapter are listed as imports and comments at the top of each `.py` file.
- These labs are designed as a **companion to the theory** to visualize and numerically verify derived mathematical results. Feel free to modify parameters and rerun to explore the "Exploration Problems" at the end of each lab.
- If you encounter a `ModuleNotFoundError`, make sure all packages from Step 1 (`numpy`, `scipy`, `sympy`, `matplotlib`) are installed in your Python environment.

---

## License
This project is licensed under the [MIT License](LICENSE).
