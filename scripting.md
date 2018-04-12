## -- Episode I --
# Advanced Scripting

--

## Abandon Bash?

* Python is an ideal glue language
    * Easy to orchestrate programs 
    * Expressive error handling
    * Efficient data forwarding
* ...with all the real bells and whistles <!-- .element: class="fragment" data-fragment-index="1" -->
    * Advanced program flow and constructs <!-- .element: class="fragment" data-fragment-index="1" -->
    * Highly optimised data structures <!-- .element: class="fragment" data-fragment-index="1" -->
    * Extensive, powerful libraries <!-- .element: class="fragment" data-fragment-index="1" -->

--

## Python Calling

* Invoke processes with the ``subprocess`` module
    * Synchronous using ``check_call``, ``check_output``
    * Asynchronously using ``Popen``


    import subprocess
    
    subprocess.check_call(['cat', __file__])

--

## Exercise - I/O Redirection

* Use ``Popen`` to call ``cat``
    * ...with ``subprocess.PIPE`` to receive ``stdout``
* Use ``Popen`` to call ``wc -l``
    * ...and pass ``cat``'s ``stdout`` as ``stdin``
* ...then ``wait`` for both processes


    import subprocess

    cat = subprocess.Popen(['cat', __file__], stdout=subprocess.PIPE)
    counter = subprocess.Popen(['wc', '-l'], stdin=cat.stdout)
    if cat.wait() != 0 or counter.wait() != 0:
        raise RuntimeError
<!-- .element: class="fragment" -->

--

## Command Line Arguments

* CLI parser module ``argparse`` builtin
    * Automatic help messages
    * type conversions and constraints
    * Optional and variadic arguments 


    import argparse
    
    CLI = argparse.ArgumentParser(description="beedo beedo beedo")
    CLI.add_argument('beedo', type=str, help="beedo?")
    options = CLI.parse_args()
    print(options.beedo, options.beedo, options.beedo)

--

## Exercise - Argumentation

* Revisit your ``fibonacci`` script
* Add optional parameter ``--count``
    * type integer *or inf* <!-- .element: class="fragment" -->
    * default value *that is random* <!-- .element: class="fragment" -->
* Optional starting count <!-- .element: class="fragment" -->


    import argparse
    
    CLI = argparse.ArgumentParser(description="Generate Fibonacci Numbers")
    CLI.add_argument('--count', type=int, default=random.randint(20, 50), help="Count of generated Numbers")
    CLI.add_argument('--start', type=int, default=0, help="Index of first generated Numbers")

    ...

    start, count = options.start, options.cout
    for value in itertools.islice(fibonacci(), start, start + count):
        print(value)
<!-- .element: class="fragment" -->

--

## Closing remarks

* Python is an ideal scripting language
    * Do not be afraid to call existing Bash scripts!
* Safe and maintainable, well structured
    * No triple-escaped argument passing
* Easy to extend when requirements change
