# /usr/bin/env python3
import itertools


def fibonacci():
    """Generate Fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for value in itertools.islice(fibonacci(), 100):
    print(value)
