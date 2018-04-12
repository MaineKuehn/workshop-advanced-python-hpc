# /usr/bin/env python3
import argparse
import itertools
import random

CLI = argparse.ArgumentParser(description="Generate Fibonacci Numbers")
# add_argument --count


def fibonacci():
    """Generate Fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():  # ask me about __main__!
    # parse CLI
    # print values from fibonacci
    ...


if __name__ == "__main__":
    main()
