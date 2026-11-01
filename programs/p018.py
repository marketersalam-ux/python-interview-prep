import cmath

a = 1
b = -5
c = 6

d = b ** 2 - 4 * a * c
root1 = (-b + cmath.sqrt(d)) / (2 * a)
root2 = (-b - cmath.sqrt(d)) / (2 * a)

print(f"Equation: {a}x^2 + ({b})x + ({c}) = 0")
print("Root 1:", root1.real)
print("Root 2:", root2.real)
