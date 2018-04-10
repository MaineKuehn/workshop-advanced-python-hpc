# Prologue: A Python walks into a workshop

* We are about to check...
    * ...your working environment
    * ...my assumptions
    * ...pace of the workshop 

--

## Getting on the same Page

* Open a terminal/shell  <!-- .element: class="fragment" -->
* Launch ``python3`` <!-- .element: class="fragment" -->
* Execute ``print("Hello", "World")`` <!-- .element: class="fragment" -->
* Execute ``import antigravity`` <!-- .element: class="fragment" -->

--

## Vim, Emacs, Nano, Kate, TextMate, Notepad++, ...

* Write and run this script

        #/usr/bin/env python3
        words = "Hello", "World"
        print(*words)

--

## Generating pace

* Write a generator for the Fibonacci numbers
    * Step 1: ``a, b = 0, 1``
    * Step N: ``a, b = b, a + b``
* Print the first 100 numbers

--

    #/usr/bin/env python3
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    for count, value in enumerate(fibonacci()):
        if count == 100:
            break
        print(value)
