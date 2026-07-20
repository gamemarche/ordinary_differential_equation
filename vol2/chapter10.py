"""
Ch.10 -- Python Lab: Bessel and Legendre Functions with scipy.special
=======================================================================

Part 1: Bessel functions J0-J3, with zeros marked (Section 10.2, 10.4)
Part 2: Legendre polynomials P0-P4, orthogonality check (Section 10.6)
Exploration: first five zeros of J0(x) via scipy.optimize.brentq
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, jn_zeros, legendre
from scipy.integrate import quad
from scipy.optimize import brentq

# -----------------------------------------------------------
# Part 1: Bessel functions J0-J3, with zeros marked
# -----------------------------------------------------------
x = np.linspace(0, 15, 1000)

fig, ax = plt.subplots(figsize=(8, 5))
colors = ['steelblue', 'darkorange', 'seagreen', 'crimson']
for n, c in zip(range(4), colors):
    ax.plot(x, jn(n, x), color=c, linewidth=2, label=fr'$J_{n}(x)$')
    zeros_n = jn_zeros(n, 3)  # first 3 positive zeros of J_n (Section 10.4, Eq. 10.30)
    ax.plot(zeros_n, np.zeros_like(zeros_n), 'o', color=c, markersize=6)

ax.axhline(0, color='gray', linewidth=0.6)
ax.set_xlabel('x')
ax.set_ylabel(r'$J_n(x)$')
ax.set_title('Ch.10 -- Bessel Functions J0-J3 with Zeros Marked')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("First 3 positive zeros of each J_n:")
for n in range(4):
    print(f"  J_{n}: {jn_zeros(n, 3)}")

# -----------------------------------------------------------
# Part 2: Legendre polynomials P0-P4
# -----------------------------------------------------------
xL = np.linspace(-1, 1, 400)
fig, ax = plt.subplots(figsize=(8, 5))
colors2 = ['steelblue', 'darkorange', 'seagreen', 'crimson', 'purple']
for n, c in zip(range(5), colors2):
    Pn = legendre(n)          # returns a numpy poly1d object (Definition 10.6)
    ax.plot(xL, Pn(xL), color=c, linewidth=2, label=fr'$P_{n}(x)$')

ax.axhline(0, color='gray', linewidth=0.6)
ax.set_xlabel('x')
ax.set_ylabel(r'$P_n(x)$')
ax.set_title('Ch.10 -- Legendre Polynomials P0-P4')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Numerical orthogonality check: integral of P_m * P_n over [-1, 1] (Theorem 10.10)
print("\nOrthogonality / normalization check (integral of P_m * P_n dx):")
pairs = [(0, 2), (1, 3), (2, 2), (3, 3)]
for m, n in pairs:
    Pm, Pn = legendre(m), legendre(n)
    val, err = quad(lambda t: Pm(t) * Pn(t), -1, 1)
    expected = 0.0 if m != n else 2.0 / (2 * n + 1)
    print(f"  m={m}, n={n}: integral = {val:.10f}   (expected {expected:.10f})")

# -----------------------------------------------------------
# Exploration Problem: first five zeros of J0(x) via brentq
# -----------------------------------------------------------
def bracket_and_find_zeros(f, x_max, n_zeros, n_scan=2000):
    """Scan for sign changes of f on (0, x_max] and refine each with brentq."""
    xs = np.linspace(1e-6, x_max, n_scan)
    fs = f(xs)
    found = []
    for i in range(len(xs) - 1):
        if fs[i] * fs[i+1] < 0:
            root = brentq(f, xs[i], xs[i+1])
            found.append(root)
            if len(found) == n_zeros:
                break
    return found


J0 = lambda t: jn(0, t)
zeros_brentq = bracket_and_find_zeros(J0, 20.0, 5)
print("\nFirst five positive zeros of J0(x), found manually via brentq:")
for i, z in enumerate(zeros_brentq, start=1):
    print(f"  alpha_0,{i} = {z:.6f}")

print("\nFor comparison, scipy.special.jn_zeros(0, 5):")
print(" ", jn_zeros(0, 5))
