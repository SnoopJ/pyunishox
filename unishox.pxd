cdef extern from "Unishox/unishox1.h":
    cdef struct us_lnk_lst: 
        char *data
        us_lnk_lst *previous
    #NOTE: we can't use the identifier `in` here, so we rename it
    int unishox1_compress(const char* _in, int len, char* out, us_lnk_lst *prev_lines)
    int unishox1_decompress(const char* _in, int len, char* out, us_lnk_lst *prev_lines)


