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

## Known bugs

Decompression sometimes fails with a segfault. It's not clear to me why this
happens, but here are some strings that reliably cause this behavior:

```python
failing_strings = [
    "ۻڧۮاڝۅݘݓٻۺۏصݬؠ𘅥مۮƻی",
    "ΑϓϦЗǬϤϺ",
    "ȬĹÒɁÁÙȲΉƟǷͶԒ",
    "RȤ3ṜǍǮＲƤȀRǬƮɌĞ",
]
```
