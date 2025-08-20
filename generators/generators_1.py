from time import time

def numbers():
    for i in range(1000000):
        yield i


numbers = numbers()

# print first element
print(next(numbers))

# print second, third and fourth
# generator could only be looped once,
start = time()
for _ in range(100000):
    print(next(numbers))

end = time()
duration = end - start
print(f"Duration in seconds: {duration: .2f}")
