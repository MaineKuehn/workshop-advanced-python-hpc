## -- Episode III --
# The Binding of C

--

## See-Pie-Thon

* Default Python implementation is written in C
* Actually pretty fast for what it does


    # my_list[24]
    static PyObject *
    list_subscript(PyListObject* self, PyObject* item)
    {
        if (PyIndex_Check(item)) {
            Py_ssize_t i;
            i = PyNumber_AsSsize_t(item, PyExc_IndexError);
            if (i == -1 && PyErr_Occurred())
                return NULL;
            if (i < 0)
                i += PyList_GET_SIZE(self);
            return list_item(self, i);
        }
        else if (PySlice_Check(item)) {
            Py_ssize_t start, stop, step, slicelength, cur, i;
            PyObject* result;
            PyObject* it;
            PyObject **src, **dest;
    
            if (PySlice_Unpack(item, &start, &stop, &step) < 0) {
                return NULL;
            }
            slicelength = PySlice_AdjustIndices(Py_SIZE(self), &start, &stop,
                                                step);
    
            if (slicelength <= 0) {
                return PyList_New(0);
            }
            else if (step == 1) {
                return list_slice(self, start, stop);
            }
            else {
                result = PyList_New(slicelength);
                if (!result) return NULL;
    
                src = self->ob_item;
                dest = ((PyListObject *)result)->ob_item;
                for (cur = start, i = 0; i < slicelength;
                     cur += (size_t)step, i++) {
                    it = src[cur];
                    Py_INCREF(it);
                    dest[i] = it;
                }
    
                return result;
            }
        }
        else {
            PyErr_Format(PyExc_TypeError,
                         "list indices must be integers or slices, not %.200s",
                         item->ob_type->tp_name);
            return NULL;
        }
    }
<!-- .element: class="fragment" -->

--

## C and Speed and Python

* Python is fast(er) if you stay in its C layer
* Compare: <!-- .element: class="fragment" data-fragment-index="1" -->
    * Python loop <!-- .element: class="fragment" data-fragment-index="1" -->
    
          time python3 -c 'total = 0
          for val in range(2000000):
              total += val'
      <!-- .element: class="fragment" data-fragment-index="1" -->

    * C loop <!-- .element: class="fragment" data-fragment-index="1" -->

           time python3 -c 'sum(range(2000000))'
       <!-- .element: class="fragment" data-fragment-index="1" -->

--

## Put the C back in Python

* You generally want consecutive chunks of C
    * \*mumble\*\*mumble\*profiling\*mumble\*
* Many libraries for common tasks
    * ``numpy``, ``mpi4py``, ...
* Write your own C libraries as needed <!-- .element: class="fragment" -->
    * Don't!<!-- .element: class="fragment" -->** Seriously!**<!-- .element: class="fragment" -->
    * Convert Python to C using Cython.<!-- .element: class="fragment" -->

--

## Cython != CPython

* Python to C transpiler<!-- .element: class="fragment" data-fragment-index="1" -->
    * Functions, Classes, Modules, ...<!-- .element: class="fragment" data-fragment-index="1" -->
* Compile time optimisations<!-- .element: class="fragment" data-fragment-index="2" -->
    * Inlining, constant folding, loop unrolling, ...<!-- .element: class="fragment" data-fragment-index="2" -->
* Creates "Extension Types"<!-- .element: class="fragment" data-fragment-index="3" -->
    * Like builtins (sum, dict, pickle)<!-- .element: class="fragment" data-fragment-index="3" -->
    * Often indistinguishable from Python objects<!-- .element: class="fragment" data-fragment-index="3" -->

![Cython](resources/cythonlogo.png)

--

## Cython on a beer mat

*  

        cpdef bint is_normalized(Vector3 vector):
          return vector.magnitude2() == 1

*  

        cdef class Vector3(object):
            cdef public double x, y, z

            def __init__(self, x, y, z):
                self.x, self.y, self.z = x, y, z
            
            def __add__(self, other):
                if isinstance(self, Vector3) and isinstance(other, Vector3):
                    return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
                return NotImplemented

            cpdef double magnitude2(self):
                return self.x ** 2 + self.y ** 2 + self.z ** 2

--

## Yellow lines hint at Python interaction

* Transpile from Python to C using ``cython``
* Use annotation mode (``-a``) to see what happens
* Let's try! <!-- .element: class="fragment" data-fragment-index="1" -->


    cython -a solutions/040_cython/vector.pyx
    open solutions/040_cython/vector.html
<!-- .element: class="fragment" data-fragment-index="1" -->

--

## Exercise - Fibonacci, Part Deux

* Move your ``sequences.py`` to a ``.pyx`` file
* Add Cython declarations to generators **and functional versions** <!-- .element: class="fragment" -->


    cpdef int fibonacci_number(const long long which):
        cdef long long a = 0, b = 1
        for _ in range(which):
            a, b = b, a + b
        return a
<!-- .element: class="fragment" -->

--

## Packaging Extensions

* Usable modules require compiling twice
    * Cython -> C -> Library
* A ``setup.py`` can do it automatically
    * and take along headers, dependencies, ...


    from Cython.Distutils import build_ext as cython_build_ext
    from distutils.extension import Extension

    setup(
        ...
        ext_modules=[Extension(name='package.module',
                               sources=['package/module.pyx'])],
        cmdclass={'build_ext': cython_build_ext},
        ...
    )

--

## Exercise - Wrapping up

* Enhance your ``setup.py`` **add Vector3 class**<!-- .element: class="fragment" data-fragment-index="1" -->


    from Cython.Distutils import build_ext as cython_build_ext
    from distutils.extension import Extension

    setup(
        ...
        ext_modules=[Extension(name=..., sources=[...])],
        cmdclass={'build_ext': cython_build_ext},
        ...
    )

* Install and test
<!-- .element: class="fragment" data-fragment-index="2" -->

      $ python3 setup.py install --user 
      $ python3
      >>> import sequences
<!-- .element: class="fragment" data-fragment-index="2" -->

--

## Conclusions

* Python is fast with prebuilt primitives
    * Builtins, libraries, ...
* Build your own using ``Cython``
    * Python productivity, C performance
    * **Profile before you optimise**
* Gradually improve your code as needed
