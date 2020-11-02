import pytest
from pyunishox import compress, decompress

from hypothesis import assume, given, settings, Verbosity
from hypothesis.strategies import characters, composite, integers, sampled_from, text

import string

alphabet = characters()
input_text = text(max_size=1024, alphabet=alphabet)

def dump_bits(v):
    for num in v:
        print(f"{num:0>8b} ", end="")
    print("\n")

@given(text(max_size=1024))
def test_roundtrip(s):
    payload = s.encode("utf-8")
    cxed = compress(payload)
    final = decompress(cxed)

    assert final == payload

HAS_NULL_WHEN_COMPRESSED = [
    "ۻڧۮاڝۅݘݓٻۺۏصݬؠ𘅥مۮƻی",
    "ΑϓϦЗǬϤϺ",
    "ȬĹÒɁÁÙȲΉƟǷͶԒ",
    "RȤ3ṜǍǮＲƤȀRǬƮɌĞ",
]

@given(sampled_from(HAS_NULL_WHEN_COMPRESSED))
def test_decompress_nulls(s):
    payload = s.encode("utf-8")
    cxed = compress(payload)
    final = decompress(cxed)

    assert final == payload

@composite
def input_text_and_truncation_point(draw):
    the_text = draw(input_text)
    encoded_text = the_text.encode("utf-8")
    assume(len(encoded_text) > 2)
    idx = draw(integers(min_value=1, max_value=len(encoded_text) - 1))
    return the_text, encoded_text, idx

@pytest.mark.xfail
def test_bad_comma_roundtrip():
    s = "Ç、."
    encoded = s.encode("utf-8")
    assert decompress(compress(encoded)) == encoded

@pytest.mark.skip(reason="This will segfault")
@given(input_text_and_truncation_point())
@settings(verbosity=Verbosity.verbose, max_examples=10_000, derandomize=True)
def test_truncation_crasher(t):
    the_text, encoded_text, idx = t
    assume("." not in the_text)  # avoids a class of bug where '.' becomes '。'
    cxed = compress(encoded_text)
    decompress(cxed[:idx])
