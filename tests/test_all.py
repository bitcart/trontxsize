import pytest
from tronpy import Tron

import trontxsize

tron = Tron(network="nile")


@pytest.mark.parametrize(
    "tx_hash,size",
    [
        ["29e7d53e7b1463d354d1d7d90172fba89673e7bc5b0c7c441c14152a897ee363", 267],
        ["546b52f2fe19955ba57cd431752e0e290d33a3b1670d1ad0820eb765110295bc", 283],
        ["cd0fc9dbe9999c7beee2cee0bcd1af39bd797802d85af4e35ded9adddcd9d764", 314],
        ["293f00a9f5415617a9889218ffed86f1d2bf78552557d2562eaa3358160c43c1", 346],
        ["9c533f0257397642f10573676f0769b5d58d68c767c661fbf9405a032a55cb6a", 345],
    ],
)
def test_tx_size_works(tx_hash, size):
    tx_data = tron.get_transaction(tx_hash)
    data = {"raw_data": tx_data["raw_data"], "signature": tx_data["signature"]}
    assert trontxsize.get_tx_size(data) == size


def test_deep_copy():
    tx_data = tron.get_transaction("29e7d53e7b1463d354d1d7d90172fba89673e7bc5b0c7c441c14152a897ee363")
    data = {"raw_data": tx_data["raw_data"], "signature": tx_data["signature"]}
    assert trontxsize.get_tx_size(data) == 267
    assert "value" in data["raw_data"]["contract"][0]["parameter"]
