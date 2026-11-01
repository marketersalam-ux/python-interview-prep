def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


count = 10
print("Fibonacci sequence:")
for i in range(count):
    print(fibonacci(i), end=" ")
print()
