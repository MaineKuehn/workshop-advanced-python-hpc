## -- Prologue --
# A Python walks
## into a workshop

--

## Getting started

* We are about to check...
    * ...your working environment
    * ...my assumptions
    * ...pace of the workshop 

--

## Getting on the same Page

* Open a terminal/shell
* Launch ``python3``
* Execute ``print("Hello", "World")``
* Execute ``import antigravity``

--

## Vim, Emacs, Nano, Kate, TextMate, Notepad++, ...

* Write and run this as a script

        #/usr/bin/env python3
        words = "Hello", "World"
        print(*words)
<!-- .element: class="fragment" -->

--

## Generating pace

* Write a generator for the Fibonacci numbers
    * Step 1: ``a, b = 0, 1``
    * Step N: ``a, b = b, a + b``
* Print the first 100 numbers

        def fibonacci():
            a, b = 0, 1
            while True:
                yield a
                a, b = b, a + b

        for value in itertools.islice(fibonacci(), 100):
            print(value)
<!-- .element: class="fragment" -->
