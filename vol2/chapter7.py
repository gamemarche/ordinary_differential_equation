import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# Part 1: Trace-determinant classifier (Theorem 7.10)
def classify(A):
    """
    Classify the origin of y' = Ay using the trace-determinant
    test of Theorem 7.10. Assumes det(A) != 0.
    """
    p = np.trace(A)
    q = np.linalg.det(A)
    disc = p**2 - 4 * q

    if q < 0:
        return "Saddle point (unstable)"
    elif disc > 0:
        return "Node (stable)" if p < 0 else "Node (unstable)"
    elif disc == 0:
        return "Degenerate node (stable)" if p < 0 else "Degenerate node (unstable)"
    else:  # disc < 0 -> complex eigenvalues
        if np.isclose(p, 0):
            return "Center"
        return "Spiral (stable)" if p < 0 else "Spiral (unstable)"

# -----------------------------------------------------------
# Part 2: Phase portrait via streamplot
def phase_portrait(A, title, ax, span=3):
    """Draw a streamplot phase portrait for y' = Ay on the given axes."""
    y1 = np.linspace(-span, span, 30)
    y2 = np.linspace(-span, span, 30)
    Y1, Y2 = np.meshgrid(y1, y2)
    dY1 = A[0, 0] * Y1 + A[0, 1] * Y2
    dY2 = A[1, 0] * Y1 + A[1, 1] * Y2

    ax.streamplot(Y1, Y2, dY1, dY2, color="steelblue", density=1.2, linewidth=1)
    ax.set_xlabel("y1")
    ax.set_ylabel("y2")
    ax.set_title(title, fontsize=10)
    ax.set_aspect("equal")
    ax.axhline(0, color="gray", linewidth=0.5)
    ax.axvline(0, color="gray", linewidth=0.5)

# -----------------------------------------------------------
# Part 3: One example each of a node, a saddle, and a spiral
matrices = {
    "Stable node": np.array([[-2.0, 1.0], [0.0, -3.0]]),
    "Saddle point (Example 7.14)": np.array([[1.0, 3.0], [3.0, 1.0]]),
    "Stable spiral": np.array([[0.0, -1.0], [4.0, -1.0]]),
}

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, (label, A) in zip(axes, matrices.items()):
    eigenvalues = np.linalg.eig(A)[0]
    kind = classify(A)
    subtitle = f"{label}\neig = {np.round(eigenvalues, 2)}\n{kind}"
    phase_portrait(A, subtitle, ax)

plt.tight_layout()
plt.show()

# -----------------------------------------------------------
# Part 4: Print trace, determinant, and classification for each
print("Automatic classification via Theorem 7.10:\n")
for label, A in matrices.items():
    p = np.trace(A)
    q = np.linalg.det(A)
    print(f"{label}")
    print(f"  A = {A.tolist()}")
    print(f"  trace p = {p:.2f}, det q = {q:.2f}")
    print(f"  classification: {classify(A)}\n")
