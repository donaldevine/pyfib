fibonacci_cache = {}

def fibonacci(n):

    if type(n) != int:
        raise TypeError("n must be a positive ineger")

    if n < 1:
        raise ValueError("n must be a postive ineger")

    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the nth term
    if n <= 2:
        value = 1    
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

# testing
for n in range(1, 10):    
    print(n, ":", fibonacci(n))
