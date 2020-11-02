# distutils: sources = Unishox/unishox1.c
# distutils: include_dirs = Unishox/

from cpython cimport array
cimport unishox

# This is how Cython spells compile-time definitions, ugh
# https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html#compile-time-definitions
DEF MAXALLOC = 1024

def compress(bytes _in):
    cdef char[MAXALLOC] out
    cdef int N = unishox.unishox1_compress(<char *>_in, len(_in), out, NULL)
    return out[:N]

def decompress(bytes _in):
    cdef char[MAXALLOC] out
    cdef int N = unishox.unishox1_decompress(<char *>_in, len(_in), out, NULL)
    out[N] = 0  # from unishox1.c: `dbuf[dlen] = 0;`
    return out[:N]
