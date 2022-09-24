# trontxsize - Calculate tron transaction size in bytes

[![CircleCI](https://circleci.com/gh/bitcartcc/trontxsize.svg?style=svg)](https://circleci.com/gh/bitcartcc/trontxsize)
[![Codecov](https://img.shields.io/codecov/c/github/bitcartcc/trontxsize?style=flat-square)](https://codecov.io/gh/bitcartcc/trontxsize)
[![PyPI version](https://img.shields.io/pypi/v/trontxsize.svg?style=flat-square)](https://pypi.python.org/pypi/trontxsize/)

In Tron (TRX) network, fee calculation algorithm is complex. And the most complex part of it is that it depends on transaction size.

But there's no method existing to calculate it

This library does just this:

```python
import trontxsize

print(trontxsize.get_tx_size({"raw_data": ..., "signatures": [...])) # matches bandwidth you see in block explorer
```

How does it work? The library pre-compiled a trimmed-down version of Tron protobuf and uses it directly to calculate transaction size

## Copyright and License

Copyright (C) 2022 MrNaif2018

Licensed under the [MIT License](LICENSE)
