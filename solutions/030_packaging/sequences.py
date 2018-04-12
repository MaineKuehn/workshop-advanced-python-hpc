def fibonacci():
    """Generate Fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def factorial():
    """Generate factorial numbers, starting at 0!"""
    product, n = 1, 0
    while True:
        yield product
        n += 1
        product *= n
