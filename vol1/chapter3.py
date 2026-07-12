import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# Part 1: RC circuit charging -- numerical vs. analytical
# -----------------------------------------------------------
# Step 1: Define circuit parameters (same as Example 3.3)
R, C, E0 = 1000.0, 5e-4, 12.0     # ohms, farads, volts
tau_rc = R * C                    # time constant (s), Eq. (3.15)

def rc_rhs(t, Q):
    """Right-hand side of R dQ/dt + Q/C = E0, Eq. (3.11)."""
    return [(E0 - Q[0] / C) / R]

t_span = (0.0, 3.0)
t_eval = np.linspace(*t_span, 300)
sol_rc = solve_ivp(rc_rhs, t_span, [0.0], t_eval=t_eval, rtol=1e-8)

# Step 2: Analytical solution from Eq. (3.15)
Q_exact = E0 * C * (1 - np.exp(-t_eval / tau_rc))

# Step 3: Plot numerical vs. analytical charge curves
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(t_eval, Q_exact * 1e3, color='black', linewidth=2, label='Analytical (Eq. 3.15)')
ax.plot(t_eval, sol_rc.y[0] * 1e3, 'o', markersize=3, color='steelblue',
        markevery=8, label='solve_ivp (numerical)')
ax.set_xlabel('t (s)'); ax.set_ylabel('Q(t) (mC)')
ax.set_title('Ch.3 -- RC Circuit Charging: Numerical vs. Analytical')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Time constant tau = RC = {tau_rc:.2f} s")
print(f"Max |numerical - analytical| = {np.max(np.abs(sol_rc.y[0]-Q_exact)):.2e} C")

# -----------------------------------------------------------
# Part 2: Logistic growth -- comparing (k, M) combinations
# -----------------------------------------------------------
def logistic_rhs(t, P, k, M):
    """Right-hand side of dP/dt = kP(1 - P/M), Eq. (3.26)."""
    return [k * P[0] * (1 - P[0] / M)]

P0 = 200.0                                 # same initial population as Example 3.8
t_eval_log = np.linspace(0, 20, 300)
# Step 4: Base case, then doubled k, then doubled M (see Exploration Problem)
param_sets = [(0.4, 800.0, 'k=0.4, M=800 (base, Ex. 3.8)'),
              (0.8, 800.0, 'k=0.8, M=800 (k doubled)'),
              (0.4, 1600.0, 'k=0.4, M=1600 (M doubled)')]

fig, ax = plt.subplots(figsize=(8, 5))
linestyles = ['-', '--', '-.']
label_positions_x = [9.0, 3.0, 15.0]

for idx, (k, M, label) in enumerate(param_sets):
    num = idx + 1
    new_label = f"{num}. {label}"
    sol = solve_ivp(logistic_rhs, (0, 20), [P0], args=(k, M),
                     t_eval=t_eval_log, rtol=1e-8)
    ax.plot(t_eval_log, sol.y[0], linewidth=2, linestyle=linestyles[idx], label=new_label)
    ax.axhline(M, linestyle='--', color='gray', linewidth=1, alpha=0.5)
    
    # Find y value on the curve at the designated x position
    x_pos = label_positions_x[idx]
    closest_idx = np.argmin(np.abs(sol.t - x_pos))
    y_pos = sol.y[0][closest_idx]
    
    # Place text label on the curve
    ax.annotate(f"({num})", xy=(x_pos, y_pos), xytext=(0, 10), 
                textcoords="offset points", ha='center', va='bottom',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", lw=0.5, alpha=0.8))

ax.set_xlabel('t (years)'); ax.set_ylabel('P(t)')
ax.set_title('Ch.3 -- Logistic Growth for Different (k, M)')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
