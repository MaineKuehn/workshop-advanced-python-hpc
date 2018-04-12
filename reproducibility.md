## -- Episode II --
# Re: producibility

--

## Getting Productive

* Python has a huge productivity ecosystem
    * Development, documentation, deployment, ...
    * Testing, Checking, Linting, ...
    * Profilers, Extensions, Refactoring, Libraries, ...
* Exploit it for productive science <!-- .element: class="fragment" data-fragment-index="1" -->
    * Reproduce your results two weeks from now <!-- .element: class="fragment" data-fragment-index="1" -->
    * Understand the mess you wrote at 2 AM <!-- .element: class="fragment" data-fragment-index="1" -->
    * Free as in "free beer" <!-- .element: class="fragment" data-fragment-index="2" -->

--

## Pulling packages

* Python has a builtin package manager ``pip``
* Let's pull in a linter <!-- .element: class="fragment" data-fragment-index="1" -->

        python3 -m pip install pylint --user
<!-- .element: class="fragment" data-fragment-index="1" -->

* Not that easy in certain environments! <!-- .element: class="fragment" data-fragment-index="2" -->
    * Requires internet access <!-- .element: class="fragment" data-fragment-index="2" -->
    * Defaults to $HOME - use $PYTHONUSERBASE to change <!-- .element: class="fragment" data-fragment-index="2" -->

--

## Exercise - Knives and PyLint

> A linter or lint refers to tools that analyze source code to flag programming errors, bugs, stylistic errors, and suspicious constructs.

    python3 -m pylint solutions/021_argparse.py
<!-- .element: class="fragment"-->

* Pedantic, annoying, stupid, ... <!-- .element: class="fragment"-->
* You will be grateful once: <!-- .element: class="fragment"-->
    * \> 0.5 KLOC <!-- .element: class="fragment"-->
    * any of class, async, Lock, process, ... <!-- .element: class="fragment"-->
    * assumptions change two months later <!-- .element: class="fragment"-->

--

## Packaging

* Trivial to build your own Python package
* Simplifies dependencies and deployment
* Hook for tests, plugins, C extensions, ...

--

## Exercise - Pack Man

* Create a folder with ``sequences.py``
* Put in ``def fibonacci`` *and `def factorial`* <!-- .element: class="fragment"-->
* Create a ``setup.py``

        from setuptools import setup
        
        setup(
            name='sequences',
            version='1.0',
            py_modules=['sequences'],
            install_requires=[],
        )


    python3 setup.py install --user

--

## Closing remarks

* Python has lots of tools to make your life easier
    * Dependencies: ``pip``, ``conda``, ``venv``, ...
    * Maintenance: ``pylint``, ``prospector``, ``nose``, ...
    * ``sphinx``, ``mypy``, ...
* Not all of them are useful to you!
    * Try and use as you see fit
