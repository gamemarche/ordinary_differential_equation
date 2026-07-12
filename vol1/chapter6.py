import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Step 1: Free-vibration waveforms for three damping regimes (Theorem 6.1)
# Fixed m and k; only c changes between the three cases.
m, k = 1.0, 4.0                      # natural frequency omega0 = sqrt(k/m) = 2 rad/s
omega0 = np.sqrt(k / m)
c_values = {
    "Underdamped (c=1)":          1.0,   # zeta = c / (2*sqrt(m*k)) < 1
    "Critically damped (c=4)":    2 * np.sqrt(m * k),   # zeta = 1 exactly
    "Overdamped (c=8)":           8.0,   # zeta > 1
}

def free_vibration_rhs(t, state, m, c, k):
    # state = [y, y']; returns [y', y'']  from  m*y'' + c*y' + k*y = 0
    y, v = state
    dydt = v
    dvdt = -(c * v + k * y) / m
    return [dydt, dvdt]

t_span = (0, 5)
t_eval = np.linspace(*t_span, 500)
y0 = [1.0, 0.0]   # released from y(0) = 1 m, at rest, as in Examples 6.1/6.3/6.4

fig, ax = plt.subplots(figsize=(8, 5))
linestyles = ['-', '--', '-.']
for idx, (label, c) in enumerate(c_values.items()):
    zeta = c / (2 * np.sqrt(m * k))
    sol = solve_ivp(free_vibration_rhs, t_span, y0, args=(m, c, k), t_eval=t_eval)
    ax.plot(sol.t, sol.y[0], label=f"{label}, " + r"$\zeta$" + f" = {zeta:.2f}", linestyle=linestyles[idx], linewidth=2)

ax.axhline(0, color="gray", linewidth=0.8)
ax.set_xlabel("t (s)")
ax.set_ylabel("y(t) (m)")
ax.set_title("Ch.6 — Free Vibration: Three Damping Regimes (Theorem 6.1)")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Step 2: Steady-state resonance curves for several damping ratios (Theorem 6.2-6.3)
# Closed-form M(omega) from equation (6.23); no numerical integration required.
F0_over_m = 1.0                      # normalize forcing amplitude per unit mass
omega_range = np.linspace(0.01, 4, 400)

def steady_state_amplitude(omega, omega0, zeta, F0_over_m):
    denom = np.sqrt((omega0**2 - omega**2)**2 + (2 * zeta * omega0 * omega)**2)
    return F0_over_m / denom

zeta_list = [0.1, 0.3, 0.7, 1.0]

fig2, ax2 = plt.subplots(figsize=(8, 5))
linestyles2 = ['-', '--', '-.', ':']
for idx, zeta in enumerate(zeta_list):
    M = steady_state_amplitude(omega_range, omega0, zeta, F0_over_m)
    ax2.plot(omega_range, M, label=fr"$\zeta$ = {zeta}", linestyle=linestyles2[idx], linewidth=2)
    # Mark the practical-resonance peak when it exists, per equation (6.29)
    if zeta < 1 / np.sqrt(2):
        omega_r = omega0 * np.sqrt(1 - 2 * zeta**2)
        M_max = steady_state_amplitude(omega_r, omega0, zeta, F0_over_m)
        ax2.plot(omega_r, M_max, "o", color="black", markersize=5)

ax2.axvline(omega0, color="gray", linestyle="--", linewidth=0.8, label=r"$\omega_0$")
ax2.set_xlabel(r"Driving frequency $\omega$ (rad/s)")
ax2.set_ylabel(r"Steady-state amplitude $M(\omega)$")
ax2.set_title("Ch.6 — Resonance Curves for Several Damping Ratios (§6.4)")
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Step 3: Print the resonance frequency and peak amplitude predicted by (6.29)-(6.30)
# for each zeta, for direct numerical comparison against the curves above.
print(f"{'zeta':>6} | {'omega_r (rad/s)':>16} | {'M_max':>10}")
for zeta in zeta_list:
    if zeta < 1 / np.sqrt(2):
        omega_r = omega0 * np.sqrt(1 - 2 * zeta**2)
        M_max = F0_over_m / (2 * zeta * omega0**2 * np.sqrt(1 - zeta**2))
        print(f"{zeta:6.2f} | {omega_r:16.3f} | {M_max:10.3f}")
    else:
        print(f"{zeta:6.2f} | {'no peak (>= 1/sqrt2)':>16} | {'see omega=0':>10}")
