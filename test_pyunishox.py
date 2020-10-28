import time
from pyunishox import compress, decompress

from hypothesis import given
from hypothesis.strategies import characters, text

alphabet = characters(whitelist_categories=('Nd', 'Lu'), min_codepoint=128)

@given(text(max_size=1024, alphabet=alphabet))
def test_roundtrip(s):
    print(f"s:\t'{repr(s)}'")
    payload = s.encode("utf-8")
    print(f"payload:\t{payload}\t({len(payload)} bytes)")
    print(f"\t{[num for num in payload]}")
    cxed = compress(payload)
    print(f"cxed:\t{cxed}\t({len(payload)} bytes)")
    print(f"\t{[num for num in cxed]}")
    final = decompress(cxed)
    print(f"decompressed:\t{final}\t({len(payload)} bytes)")
    print(f"\t{[num for num in final]}")

    assert final == payload
