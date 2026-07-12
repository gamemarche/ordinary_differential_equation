import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# Part 1: Direction field for y' = y - x  (Example 1.8)
# -----------------------------------------------------------
x_grid = np.linspace(-2, 2, 20)
y_grid = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x_grid, y_grid)
slope = Y - X  # f(x, y) = y - x

# Normalize arrows to equal length so only direction is visible
norm = np.sqrt(1 + slope**2)
U, V = 1 / norm, slope / norm

fig, ax = plt.subplots(figsize=(7, 6))
ax.quiver(X, Y, U, V, angles='xy', color='gray', alpha=0.6, width=0.003)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title("Direction field of y' = y - x")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------
# Part 2: Euler's method for y' = 2y - x, y(0) = 1  (Example 1.9)
# -----------------------------------------------------------
def f(x, y):
    return 2 * y - x

def euler_method(f, x0, y0, h, x_end):
    """Apply Euler's method from x0 to x_end with step size h."""
    xs, ys = [x0], [y0]
    x, y = x0, y0
    n_steps = int(round((x_end - x0) / h))
    for _ in range(n_steps):
        y = y + h * f(x, y)
        x = x + h
        xs.append(x); ys.append(y)
    return np.array(xs), np.array(ys)

def exact_solution(x):
    # y = x/2 + 1/4 + (3/4) e^{2x}, constant fixed by y(0) = 1
    return x / 2 + 1 / 4 + (3 / 4) * np.exp(2 * x)

x0, y0, x_end = 0.0, 1.0, 1.0
step_sizes = [0.5, 0.1, 0.01]

fig, ax = plt.subplots(figsize=(8, 5))
x_fine = np.linspace(x0, x_end, 200)
ax.plot(x_fine, exact_solution(x_fine), color='black', linewidth=2, label='Exact solution')

for h in step_sizes:
    xs, ys = euler_method(f, x0, y0, h, x_end)
    ax.plot(xs, ys, marker='o', markersize=4, label=f'Euler, h = {h}')

ax.set_xlabel('x'); ax.set_ylabel('y(x)')
ax.set_title("Euler's method vs. exact solution for y' = 2y - x")
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------
# Part 3: Error at x = 1 for each step size
# -----------------------------------------------------------
exact_at_1 = exact_solution(1.0)
print(f"Exact value y(1) = {exact_at_1:.6f}")
for h in step_sizes:
    _, ys = euler_method(f, x0, y0, h, x_end)
    error = abs(exact_at_1 - ys[-1])
    print(f"h = {h:5.2f}  ->  Euler y(1) = {ys[-1]:.6f},  error = {error:.6f}")