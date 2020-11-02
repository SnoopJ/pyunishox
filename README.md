# PyUnishox

**NOTE: IN ITS CURRENT STATE, THIS WRAPPER WILL DEFINITELY SEGFAULT FOR SOME INPUTS**

Python wrapper of the [Unishox](https://github.com/siara-cc/Unishox) encoder.

## Example usage

```python
from pyunishox import compress, decompress

s = "おはようございます！"
payload = s.encode("utf-8")

print(f"Compressing payload: {s}...")
c = compress(payload)
print(f"Result: {c}")

print("Decompressing...")
d = decompress(c)
print(f"Result: {d.decode('utf-8')}")
```

## Installation

**NOTE:** you need to have [Cython](https://cython.readthedocs.io/en/latest/src/quickstart/install.html) installed

To build, clone this repository, then run `pip`.

* `git clone https://github.com/SnoopJeDi/pyunishox pyunishox/`
* `python3 -m pip install pyunishox/`

## Changelog

**`0.21`**
* Squelched Unishox debug information
* Fix mismatched buffer length due to implicit casting by Cython

## Known bugs

* Some truncated inputs can cause a segfault (see `test_pyunishox.py:test_truncation_crasher()`)
* Some inputs are not round-trippable (see `test_pyunishox.py:test_bad_comma_roundtrip()`)
  * This behavior is from [Unishox itself](https://github.com/siara-cc/Unishox/issues/6)

## Acknowledgements

Thanks to [habnabit](https://github.com/habnabit/) for their work identifying
the wrapper's crashing behavior when decompressing strings with `NUL` bytes and
for discovering the other bugs.
