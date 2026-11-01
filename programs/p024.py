count = 10

a = 0
b = 1
print("Fibonacci sequence:")
for i in range(count):
    print(a, end=" ")
    a, b = b, a + b
print()
