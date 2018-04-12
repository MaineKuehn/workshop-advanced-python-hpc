# /usr/bin/env python3
import itertools


def fibonacci():
    while True:
        yield 1


for value in fibonacci():
    print(value)
