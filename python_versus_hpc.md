## -- Interlude --
# Python su**s
## for HPC

![GUN](resources/240px-Vienna_Convention_road_sign_B2a.svg.png)

--

## Python is not fast

* Python cannot be safely optimised
* Python cannot be sensibly compiled
* Python cannot be easily parallelised
* Fundamental restrictions from mutability <!-- .element: class="fragment" -->
* Will not go away any time soon <!-- .element: class="fragment" -->

--

## Here are the numbers...


![GUN](resources/Gospers_glider_gun.gif)

| Implementation | Speed   | Speedup |
| -------------- | -------:| ------- |
| CPython        | 70 Hz   |         |
| PyPy           | 300 Hz  | x4      |
| C              | 12000Hz | x170    |
<!-- .element: class="fragment" -->

* Image by Johan G. Bonte / [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/)

--

## Why Python for HPC?

* Python is highly productive
* Python is highly maintainable
* Python has bindings for everything
* Python ran that C benchmark... <!-- .element: class="fragment" -->
