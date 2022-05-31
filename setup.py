from distutils.core import setup
from Cython.Build import cythonize
 
setup(
    ext_modules = cythonize("env.py") # Change this to the name of your obfuscated code file.
)
