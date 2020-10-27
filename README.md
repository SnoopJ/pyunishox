# PyUnishox

Python wrapper of the [Unishox](https://github.com/siara-cc/Unishox) encoder.

See `test_pyunishox.py` for an example of the usage, but  
**tl;dr: you want `from pyunishox import compress, decompress`**

## Installation

**NOTE:** you need to have [Cython](https://cython.readthedocs.io/en/latest/src/quickstart/install.html) installed

To build, clone this repository, then clone the Unishox source into the subdirectory `Unishox/`, then run `pip`.

* `git clone https://github.com/SnoopJeDi/pyunishox pyunishox/`
* `git clone https://github.com/siara-cc/Unishox pyunishox/Unishox`
* `python3 -m pip install pyunishox/`
