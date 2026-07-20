"""
Chapter 8 -- Python Lab
Lotka-Volterra Predator-Prey Simulation
(Section 8.4, Equations 8.49-8.50, 8.53, 8.58)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Step 1: Define the Lotka-Volterra system
# dx/dt = alpha*x - beta*x*y   (prey)
# dy/dt = delta*x*y - gamma*y  (predator)
def lotka_volterra(t, z, alpha, beta, gamma, delta):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Step 2: Set parameters and initial conditions
alpha, beta, gamma, delta = 1.1, 0.4, 0.4, 0.1
x0, y0 = 10.0, 5.0          # initial prey and predator populations
t_span = (0, 60)
t_eval = np.linspace(*t_span, 3000)

# Step 3: Solve the system numerically
sol = solve_ivp(
    lotka_volterra, t_span, [x0, y0],
    args=(alpha, beta, gamma, delta),
    t_eval=t_eval, method="RK45", rtol=1e-8, atol=1e-8
)

x_sol, y_sol = sol.y

# Step 4: Coexistence equilibrium, for reference on both plots
x_star = gamma / delta
y_star = alpha / beta

# Step 5: Plot time series x(t), y(t)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(sol.t, x_sol, label='Prey $x(t)$', color='steelblue', linewidth=2)
ax.plot(sol.t, y_sol, label='Predator $y(t)$', color='indianred', linewidth=2)
ax.set_xlabel('t')
ax.set_ylabel('Population')
ax.set_title('Ch.8 -- Lotka-Volterra Time Series')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Step 6: Plot phase-plane trajectory (x vs y)
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x_sol, y_sol, color='darkgreen', linewidth=1.5, label='Trajectory')
ax.plot(x_star, y_star, 'ko', markersize=6, label='Coexistence equilibrium')
ax.plot(x0, y0, 'k^', markersize=8, label='Initial condition')
ax.set_xlabel('Prey $x$')
ax.set_ylabel('Predator $y$')
ax.set_title('Ch.8 -- Lotka-Volterra Phase Plane')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Step 7: Numerically verify H(x, y) is (approximately) conserved along the orbit
# H(x, y) = delta*x - gamma*ln(x) + beta*y - alpha*ln(y)   (Eq. 8.58)
H = delta * x_sol - gamma * np.log(x_sol) + beta * y_sol - alpha * np.log(y_sol)
print(f"H(x,y) min = {H.min():.6f}, max = {H.max():.6f}, "
      f"relative spread = {(H.max()-H.min())/H.mean():.2e}")
