def factorial(n):
    if n == 0 or n == 1:
        print(f"n: {n}")
        return 1
    else:
        print(n)
        return n * factorial(n - 1)


n = 5
result = factorial(n)
print(f"The factorial result of {n} is {result}")
