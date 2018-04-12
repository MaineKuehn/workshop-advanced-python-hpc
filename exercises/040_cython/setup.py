from setuptools import setup
from Cython.Distutils import build_ext as cython_build_ext
from distutils.extension import Extension

setup(
    name=...,
    version=...,
    py_modules=['sequences'],
    install_requires=...,
    ext_modules=[
        Extension(name=..., sources=[...])
    ],
    cmdclass={'build_ext': cython_build_ext},
)
