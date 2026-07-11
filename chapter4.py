import sympy as sp

x = sp.symbols('x')

# -----------------------------------------------------------
# Part 1: A Wronskian function and an independence checker
# -----------------------------------------------------------
def wronskian(y1, y2, var):
    """Compute W(y1, y2)(x) = y1*y2' - y1'*y2 as a simplified sympy expression."""
    M = sp.Matrix([[y1, y2], [sp.diff(y1, var), sp.diff(y2, var)]])
    return sp.simplify(M.det())

def check_independence(y1, y2, var, test_point=0):
    """
    Report whether y1, y2 appear linearly independent on (-oo, oo),
    using Theorem 4.3: it suffices to evaluate W at a single point.
    """
    W_expr = wronskian(y1, y2, var)
    W_at_point = sp.simplify(W_expr.subs(var, test_point))
    independent = W_at_point != 0
    return W_expr, W_at_point, independent

# -----------------------------------------------------------
# Part 2: Three pairs from Sections 4.2-4.4
# -----------------------------------------------------------
pairs = {
    "e^x, e^(2x)":        (sp.exp(x), sp.exp(2 * x)),
    "e^(2x), x*e^(2x)":   (sp.exp(2 * x), x * sp.exp(2 * x)),
    "e^(2x), 3*e^(2x)":   (sp.exp(2 * x), 3 * sp.exp(2 * x)),
}

print("Wronskian and independence check for pairs of solutions:\n")
for label, (y1, y2) in pairs.items():
    W_expr, W_at_0, indep = check_independence(y1, y2, x, test_point=0)
    print(f"  y1, y2 = {label}")
    print(f"    W(y1,y2)(x) = {W_expr}")
    print(f"    W(y1,y2)(0) = {W_at_0}")
    print(f"    Linearly independent on (-oo, oo)? {indep}\n")

# -----------------------------------------------------------
# Part 3: Confirming the case distinction of Theorem 4.5
# -----------------------------------------------------------
# y1 = e^x, y2 = e^(2x) solve y'' - 3y' + 2y = 0 (Case 1, distinct real roots)
y2_case1 = sp.exp(2 * x)
lhs1 = sp.diff(y2_case1, x, 2) - 3 * sp.diff(y2_case1, x) + 2 * y2_case1
print("Check y2 = e^(2x) solves y'' - 3y' + 2y = 0:", sp.simplify(lhs1) == 0)

# y1 = e^(2x), y2 = x*e^(2x) solve y'' - 4y' + 4y = 0 (Case 2, repeated root)
y2_case2 = x * sp.exp(2 * x)
lhs2 = sp.diff(y2_case2, x, 2) - 4 * sp.diff(y2_case2, x) + 4 * y2_case2
print("Check y2 = x*e^(2x) solves y'' - 4y' + 4y = 0:", sp.simplify(lhs2) == 0)
