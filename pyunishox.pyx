# distutils: sources = Unishox/unishox1.c
# distutils: include_dirs = Unishox/

from cpython cimport array
cimport unishox

MAXALLOC = 1024

def compress(_in):
    cdef array.array out = array.array('b', [0] * len(_in))  # on the way in, we can safely allocate...
    cdef int N = unishox.unishox1_compress(_in, len(_in), out.data.as_chars, NULL)
    return out[:N].tobytes()

def decompress(_in):
    cdef array.array _inn = array.array('b', _in)
    cdef array.array out = array.array('b', [0] * MAXALLOC)  # on the way out, it's a crapshoot
    cdef int N = unishox.unishox1_decompress(_inn.data.as_chars, len(_in), out.data.as_chars, NULL)
    return out[:N].tobytes()
