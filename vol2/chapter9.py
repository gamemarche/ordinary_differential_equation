"""
chapter9.py
Python Lab 9 -- Ch.9 Power-Series Solutions of the Airy Equation vs. scipy.special.airy

Compares the truncated power-series solutions of the Airy equation y'' - x*y = 0
(Example 9.5, Section 9.2) against the exact Airy function from scipy.special.airy.

Figure 9.1: truncated series (N = 10, 20, 40 terms) vs. exact Ai(x) over x in [-6, 4].
Figure 9.2: truncation error at x = 3 as a function of the number of series terms N.
"""

import numpy as np
from scipy.special import airy
import matplotlib.pyplot as plt


def airy_series_coeffs(n_terms, a0, a1):
    """
    Return power-series coefficients a_0..a_{n_terms} for the solution of
    y'' - x*y = 0 with y(0)=a0, y'(0)=a1, using the recurrence from
    Example 9.5 (Section 9.2): a_2 = 0, and for n >= 1,
        a_{n+2} = a_{n-1} / [(n+2)(n+1)].    (Eq. 9.8)
    """
    a = np.zeros(n_terms + 1)
    a[0] = a0
    if n_terms >= 1:
        a[1] = a1
    if n_terms >= 2:
        a[2] = 0.0
    for n in range(1, n_terms - 1):
        a[n + 2] = a[n - 1] / ((n + 2) * (n + 1))
    return a


def eval_series(coeffs, x):
    """Evaluate sum_k coeffs[k] * x**k at (array) x via Horner's method."""
    result = np.zeros_like(x, dtype=float)
    for c in coeffs[::-1]:
        result = result * x + c
    return result


# Step 1: connection constants Ai(0), Ai'(0) -- see Concept Connection above
ai0, aip0, _, _ = airy(0.0)


def airy_approx(x, n_terms):
    """Approximate Ai(x) as Ai(0)*y1(x) + Ai'(0)*y2(x), truncated at n_terms."""
    a_y1 = airy_series_coeffs(n_terms, a0=1.0, a1=0.0)  # y1 of Example 9.5
    a_y2 = airy_series_coeffs(n_terms, a0=0.0, a1=1.0)  # y2 of Example 9.5
    return ai0 * eval_series(a_y1, x) + aip0 * eval_series(a_y2, x)


# -----------------------------------------------------------
# Part 1: Figure 9.1 -- truncated series vs. exact Ai(x)
# -----------------------------------------------------------
x_vals = np.linspace(-6, 4, 400)
ai_exact, _, _, _ = airy(x_vals)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x_vals, ai_exact, color='black', linewidth=2, label='Exact Ai(x), scipy')
for n_terms in [10, 20, 40]:
    ax.plot(x_vals, airy_approx(x_vals, n_terms), '--', label=f'Series, N = {n_terms}')
ax.set_xlabel('x'); ax.set_ylabel('Ai(x)')
ax.set_ylim(-0.6, 0.8)
ax.set_title("Truncated power-series solutions vs. exact Ai(x) (Example 9.5)")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------
# Part 2: Figure 9.2 -- error vs. number of terms N, at fixed x = 3
# -----------------------------------------------------------
x_test = 3.0
ai_exact_test, _, _, _ = airy(x_test)
n_range = np.arange(2, 41)
errors = [abs(ai_exact_test - airy_approx(np.array([x_test]), int(n))[0]) for n in n_range]

fig, ax = plt.subplots(figsize=(8, 5))
ax.semilogy(n_range, errors, marker='o', markersize=3, color='steelblue')
ax.set_xlabel('Number of series terms, N')
ax.set_ylabel(f'|Ai({x_test:.0f}) - series approximation|  (log scale)')
ax.set_title(f'Truncation error at x = {x_test:.0f} vs. number of terms')
ax.grid(True, alpha=0.3, which='both')
plt.tight_layout()
plt.show()

# Step 2: print the exact values requested in the Exploration Problem below
print(f"Exact Ai({x_test:.0f}) = {ai_exact_test:.8f}")
for n_terms in [5, 10, 20, 30]:
    approx = airy_approx(np.array([x_test]), n_terms)[0]
    print(f"N = {n_terms:2d} terms -> approx = {approx: .8f}, "
          f"error = {abs(ai_exact_test - approx):.3e}")
