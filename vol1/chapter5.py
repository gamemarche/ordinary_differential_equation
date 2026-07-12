import sympy as sp

# Use a real symbol: log(cos(x)) and Abs(cos(x)) only agree as real expressions
# when sympy knows x is real, which also keeps the simplification in Step 2 clean.
x = sp.symbols('x', real=True)
y = sp.Function('y')

# -----------------------------------------------------------
# Part 1: y'' - 3y' + 2y = e^(3x)  (undetermined coefficients, Example 5.4)
# -----------------------------------------------------------
print("=== Part 1: y'' - 3y' + 2y = e^(3x) ===")

# Step 1: the hand-derived particular solution from Example 5.4, Eq. (5.6)
y_p_hand = sp.Rational(1, 2) * sp.exp(3 * x)
print("By-hand y_p (Example 5.4):", y_p_hand)

# Step 2: substitute directly into L[y] = y'' - 3y' + 2y and check against e^(3x)
lhs_check = sp.simplify(
    y_p_hand.diff(x, 2) - 3 * y_p_hand.diff(x) + 2 * y_p_hand - sp.exp(3 * x)
)
print("L[y_p_hand] - e^(3x) simplifies to:", lhs_check, "(should be 0)")

# Step 3: compare against sympy's own general solution
ode1 = sp.Eq(y(x).diff(x, 2) - 3 * y(x).diff(x) + 2 * y(x), sp.exp(3 * x))
sol1 = sp.dsolve(ode1, y(x))
print("sympy dsolve general solution:", sol1, "\n")

# -----------------------------------------------------------
# Part 2: y'' + y = sec(x)  (variation of parameters, Example 5.12)
# -----------------------------------------------------------
print("=== Part 2: y'' + y = sec(x) ===")

# Step 4: the hand-derived particular solution from Example 5.12, Eq. (5.31)
# (valid on (-pi/2, pi/2), where cos(x) > 0, so log(cos(x)) is real)
y_p_hand2 = sp.cos(x) * sp.log(sp.cos(x)) + x * sp.sin(x)
print("By-hand y_p (Example 5.12):", y_p_hand2)

# Step 5: substitute directly into L[y] = y'' + y and check against sec(x)
lhs_check2 = sp.simplify(y_p_hand2.diff(x, 2) + y_p_hand2 - sp.sec(x))
print("L[y_p_hand] - sec(x) simplifies to:", lhs_check2, "(should be 0)")

# Step 6: compare against sympy's own general solution
ode2 = sp.Eq(y(x).diff(x, 2) + y(x), sp.sec(x))
sol2 = sp.dsolve(ode2, y(x))
print("sympy dsolve general solution:", sol2, "\n")

# -----------------------------------------------------------
# Part 3: y'' + y = 1, y(0) = 3, y'(0) = -1  (Example 5.1, with ICs)
# -----------------------------------------------------------
print("=== Part 3: y'' + y = 1, y(0)=3, y'(0)=-1 ===")

# Step 7: let dsolve impose the initial conditions directly
ode3 = sp.Eq(y(x).diff(x, 2) + y(x), 1)
ics = {y(0): 3, y(x).diff(x).subs(x, 0): -1}
sol3 = sp.dsolve(ode3, y(x), ics=ics)
print("sympy dsolve with ICs:           ", sol3)
print("Hand solution from Example 5.1:  y(x) = 1 + 2*cos(x) - sin(x)")
