from setuptools import setup
from Cython.Distutils import build_ext as cython_build_ext
from distutils.extension import Extension

setup(
    name='sequences',
    version='1.1',
    py_modules=['sequences'],
    install_requires=['cython'],
    ext_modules=[
        Extension(name=module, sources=['%s.pyx' % module])
        for module in ('sequences', 'vector')
    ],
    cmdclass={'build_ext': cython_build_ext},
)
