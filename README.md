# Ordinary Differential Equations (ODE) - PythonLab Codes
This repository contains the official Python source code for the book *Ordinary Differential Equations for Engineers: Fundamentals and Applications*

## How to Use

### 1. Requirements
- Python 3.10 or higher
- Required packages:
  ```bash
  pip install numpy scipy sympy matplotlib
  ```

### 2. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 3. Folder structure
```
├── vol1/
│   ├── chapter1.py   # Ch.1 — Direction Fields & Euler's Method
│   ├── chapter2.py   # Ch.2 — First-Order ODEs: Solution Methods (sympy dsolve/classify_ode)
│   ├── chapter3.py   # Ch.3 — RC Circuit Simulation & Logistic Growth
│   ├── chapter4.py   # Ch.4 — Wronskian & Linear Independence
│   ├── chapter5.py   # Ch.5 — Verifying Particular Solutions with sympy
│   └── chapter6.py   # Ch.6 — Damped/Forced Vibration & Resonance
└── vol2/             # (coming soon — Ch.7~10: Systems of ODEs, Series Solutions)
```
Each `chapterN.py` file corresponds to the "Python Lab" section at the end of Chapter N in the book, and reproduces the figures/results discussed in that chapter.

> **Note:** Vol. 2 (Ch.7–10: systems of ODEs, power series, Bessel/Legendre functions) has not been added yet and will be uploaded separately once complete.

### 4. Running a script
```bash
cd vol1
python chapter1.py
```
Each script will:
- Print numerical results (errors, comparisons, symbolic verification, etc.) to the console
- Display plots (direction fields, solution curves, error graphs, etc.) via `matplotlib`

### 5. Notes
- Required libraries for each chapter are listed as comments at the top of the corresponding `.py` file.
- These labs are meant to be a **companion to the theory**, not a programming exercise — the code lets you visualize and numerically verify results derived by hand in each chapter. Feel free to modify parameters and rerun to explore the "Exploration Problem" at the end of each lab.
- If you encounter a `ModuleNotFoundError`, make sure all packages from Step 1 are installed in your active environment.

## License
This project is licensed under the [MIT License](LICENSE).
