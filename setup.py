from setuptools import Extension, setup
from Cython.Build import cythonize

setup(
    name="pyunishox",
    license="MIT",
    version="0.21",
    ext_modules=cythonize([Extension("pyunishox", ["pyunishox.pyx"])], language_level=3)
)
