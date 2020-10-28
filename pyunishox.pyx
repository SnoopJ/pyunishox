# distutils: sources = Unishox/unishox1.c
# distutils: include_dirs = Unishox/

from cpython cimport array
cimport unishox

MAXALLOC = 1024

def compress(char* _in):
    cdef array.array out = array.array('b', [0] * MAXALLOC)
    cdef int N = unishox.unishox1_compress(_in, len(_in), out.data.as_chars, NULL)
    return out[:N].tobytes()

def decompress(char* _in):
    cdef array.array _inn = array.array('b', _in)
    cdef array.array out = array.array('b', [0] * MAXALLOC)
    cdef int N = unishox.unishox1_decompress(_inn.data.as_chars, len(_in), out.data.as_chars, NULL)
    return out[:N].tobytes()
