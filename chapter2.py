import sympy as sp
from sympy import symbols, Function, Eq, classify_ode, dsolve, simplify

# Step 1: Set up symbols and the unknown function y(x)
x = symbols('x')
y = Function('y')
 
# Step 2: Define the three example ODEs from this lab
#   L2.1 - Separable:   y' = x/y,        y(1) = 2
#   L2.4 - Linear:      y' + y/x = x**2
#   L2.8 - Bernoulli:   y' + y/x = x*y**2   (n = 2)
ode_separable = Eq(y(x).diff(x), x / y(x))
ode_linear    = Eq(y(x).diff(x) + y(x) / x, x**2)
ode_bernoulli = Eq(y(x).diff(x) + y(x) / x, x * y(x)**2)
 
examples = {
    "Separable (L2.1)": (ode_separable, {y(1): 2}),
    "Linear (L2.4)":     (ode_linear, None),
    "Bernoulli (L2.8)":  (ode_bernoulli, None),
}
 
# Step 3: Classify and solve each ODE automatically
for name, (ode, ics) in examples.items():
    print(f"--- {name} ---")
    print("ODE:           ", ode)
    print("classify_ode:  ", classify_ode(ode, y(x)))
 
    if ics is not None:
        solution = dsolve(ode, y(x), ics=ics)
    else:
        solution = dsolve(ode, y(x))
 
    print("dsolve result: ", simplify(solution))
    print()
 
# Step 4: Verify the hand-derived solutions match SymPy's output
# Hand solution for L2.1:  y(x) = sqrt(x**2 + 3)
hand_L21 = sp.sqrt(x**2 + 3)
check_L21 = sp.simplify(ode_separable.lhs.subs(y(x), hand_L21).doit()
                        - ode_separable.rhs.subs(y(x), hand_L21))
print("L2.1 hand-solution residual (should be 0):", check_L21)
 
# Hand solution for L2.4:  y(x) = x**3/4 + C/x
C = symbols('C')
hand_L24 = x**3 / 4 + C / x
check_L24 = sp.simplify(ode_linear.lhs.subs(y(x), hand_L24).doit()
                        - ode_linear.rhs.subs(y(x), hand_L24))
print("L2.4 hand-solution residual (should be 0):", check_L24)
