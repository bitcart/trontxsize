import base64
import binascii
import copy

import base58
from google.protobuf.json_format import ParseDict

from trontxsize.tron_pb2 import Transaction

BYTES_DIFF_PROTOBUF = 64  # difference we always get between java and python protobuf for some reason


def normalize_string(v):
    return base64.b64encode(v.encode())


def normalize_string2(v):
    return base64.b64encode(binascii.unhexlify(v))


def get_tx_size(tx: dict) -> int:
    data = copy.deepcopy(tx)
    raw_data = data["raw_data"]
    raw_contracts = raw_data["contract"]
    contracts = []

    for contract in raw_contracts:
        parameter = contract["parameter"]
        for key, value in parameter["value"].items():
            if isinstance(value, str):
                if key.endswith("address") and value[0] == "T":
                    parameter["value"][key] = base58.b58decode_check(parameter["value"][key]).hex()
                if key != "asset_name":
                    parameter["value"][key] = normalize_string2(parameter["value"][key])
                else:
                    parameter["value"][key] = normalize_string(parameter["value"][key])
        parameter.update(parameter.pop("value", {}))
        parameter["@type"] = parameter.pop("type_url", None)
        contracts.append(contract)

    raw_data["contract"] = contracts
    data.pop("txID", None)
    data.pop("permission", None)

    for index, signature in enumerate(data["signature"]):
        if isinstance(signature, str):
            data["signature"][index] = normalize_string2(signature)

    for key in ("data", "ref_block_bytes", "ref_block_hash"):
        if key in data["raw_data"]:
            data["raw_data"][key] = normalize_string2(data["raw_data"][key])

    transaction = Transaction()
    ParseDict(data, transaction)
    return transaction.ByteSize() + BYTES_DIFF_PROTOBUF
