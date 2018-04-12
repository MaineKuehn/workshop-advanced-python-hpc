def fibonacci():
    """Generate Fibonacci numbers"""
    cdef long long a = 0, b = 1
    while True:
        yield a
        a, b = b, a + b


cpdef int fibonacci_number(const long long which):
    cdef long long a = 0, b = 1
    for _ in range(which):
        a, b = b, a + b
    return a


def factorial():
    """Generate factorial numbers, starting at 0!"""
    product, n = 1, 0
    while True:
        yield product
        n += 1
        product *= n
