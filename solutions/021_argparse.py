# /usr/bin/env python3
import argparse
import itertools
import random

CLI = argparse.ArgumentParser(description="Generate Fibonacci Numbers")
CLI.add_argument('--count', type=int, default=random.randint(20, 50), help="Count of generated Numbers")
CLI.add_argument('--start', type=int, default=0, help="Index of first generated Numbers")


def fibonacci():
    """Generate Fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():  # ask me about __main__!
    options = CLI.parse_args()
    start, count = options.start, options.cout
    for value in itertools.islice(fibonacci(), start, start + count):
        print(value)


if __name__ == "__main__":
    main()
