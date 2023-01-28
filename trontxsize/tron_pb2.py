# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tron.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ntron.proto\x12\x08protocol\x1a\x19google/protobuf/any.proto"*\n\tAccountId\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c"J\n\tauthority\x12$\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x13.protocol.AccountId\x12\x17\n\x0fpermission_name\x18\x02 \x01(\x0c"l\n\x15\x41\x63\x63ountCreateContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61\x63\x63ount_address\x18\x02 \x01(\x0c\x12#\n\x04type\x18\x03 \x01(\x0e\x32\x15.protocol.AccountType"M\n\x10TransferContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x12\n\nto_address\x18\x02 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03"f\n\x15TransferAssetContract\x12\x12\n\nasset_name\x18\x01 \x01(\x0c\x12\x15\n\rowner_address\x18\x02 \x01(\x0c\x12\x12\n\nto_address\x18\x03 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03"\x95\x01\n\x14TriggerSmartContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x18\n\x10\x63ontract_address\x18\x02 \x01(\x0c\x12\x12\n\ncall_value\x18\x03 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x18\n\x10\x63\x61ll_token_value\x18\x05 \x01(\x03\x12\x10\n\x08token_id\x18\x06 \x01(\x03"\xc8\x0b\n\x0bTransaction\x12+\n\x08raw_data\x18\x01 \x01(\x0b\x32\x19.protocol.Transaction.raw\x12\x11\n\tsignature\x18\x02 \x03(\x0c\x1a\xf9\x08\n\x08\x43ontract\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32+.protocol.Transaction.Contract.ContractType\x12\'\n\tparameter\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x10\n\x08provider\x18\x03 \x01(\x0c\x12\x14\n\x0c\x43ontractName\x18\x04 \x01(\x0c\x12\x15\n\rPermission_id\x18\x05 \x01(\x05"\xc9\x07\n\x0c\x43ontractType\x12\x19\n\x15\x41\x63\x63ountCreateContract\x10\x00\x12\x14\n\x10TransferContract\x10\x01\x12\x19\n\x15TransferAssetContract\x10\x02\x12\x15\n\x11VoteAssetContract\x10\x03\x12\x17\n\x13VoteWitnessContract\x10\x04\x12\x19\n\x15WitnessCreateContract\x10\x05\x12\x16\n\x12\x41ssetIssueContract\x10\x06\x12\x19\n\x15WitnessUpdateContract\x10\x08\x12!\n\x1dParticipateAssetIssueContract\x10\t\x12\x19\n\x15\x41\x63\x63ountUpdateContract\x10\n\x12\x19\n\x15\x46reezeBalanceContract\x10\x0b\x12\x1b\n\x17UnfreezeBalanceContract\x10\x0c\x12\x1b\n\x17WithdrawBalanceContract\x10\r\x12\x19\n\x15UnfreezeAssetContract\x10\x0e\x12\x17\n\x13UpdateAssetContract\x10\x0f\x12\x1a\n\x16ProposalCreateContract\x10\x10\x12\x1b\n\x17ProposalApproveContract\x10\x11\x12\x1a\n\x16ProposalDeleteContract\x10\x12\x12\x18\n\x14SetAccountIdContract\x10\x13\x12\x12\n\x0e\x43ustomContract\x10\x14\x12\x17\n\x13\x43reateSmartContract\x10\x1e\x12\x18\n\x14TriggerSmartContract\x10\x1f\x12\x0f\n\x0bGetContract\x10 \x12\x19\n\x15UpdateSettingContract\x10!\x12\x1a\n\x16\x45xchangeCreateContract\x10)\x12\x1a\n\x16\x45xchangeInjectContract\x10*\x12\x1c\n\x18\x45xchangeWithdrawContract\x10+\x12\x1f\n\x1b\x45xchangeTransactionContract\x10,\x12\x1d\n\x19UpdateEnergyLimitContract\x10-\x12#\n\x1f\x41\x63\x63ountPermissionUpdateContract\x10.\x12\x14\n\x10\x43learABIContract\x10\x30\x12\x1b\n\x17UpdateBrokerageContract\x10\x31\x12\x1c\n\x18ShieldedTransferContract\x10\x33\x12\x1b\n\x17MarketSellAssetContract\x10\x34\x12\x1d\n\x19MarketCancelOrderContract\x10\x35\x1a\xfc\x01\n\x03raw\x12\x17\n\x0fref_block_bytes\x18\x01 \x01(\x0c\x12\x15\n\rref_block_num\x18\x03 \x01(\x03\x12\x16\n\x0eref_block_hash\x18\x04 \x01(\x0c\x12\x12\n\nexpiration\x18\x08 \x01(\x03\x12"\n\x05\x61uths\x18\t \x03(\x0b\x32\x13.protocol.authority\x12\x0c\n\x04\x64\x61ta\x18\n \x01(\x0c\x12\x30\n\x08\x63ontract\x18\x0b \x03(\x0b\x32\x1e.protocol.Transaction.Contract\x12\x0f\n\x07scripts\x18\x0c \x01(\x0c\x12\x11\n\ttimestamp\x18\x0e \x01(\x03\x12\x11\n\tfee_limit\x18\x12 \x01(\x03*7\n\x0b\x41\x63\x63ountType\x12\n\n\x06Normal\x10\x00\x12\x0e\n\nAssetIssue\x10\x01\x12\x0c\n\x08\x43ontract\x10\x02\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "tron_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ACCOUNTTYPE._serialized_start = 2099
    _ACCOUNTTYPE._serialized_end = 2154
    _ACCOUNTID._serialized_start = 51
    _ACCOUNTID._serialized_end = 93
    _AUTHORITY._serialized_start = 95
    _AUTHORITY._serialized_end = 169
    _ACCOUNTCREATECONTRACT._serialized_start = 171
    _ACCOUNTCREATECONTRACT._serialized_end = 279
    _TRANSFERCONTRACT._serialized_start = 281
    _TRANSFERCONTRACT._serialized_end = 358
    _TRANSFERASSETCONTRACT._serialized_start = 360
    _TRANSFERASSETCONTRACT._serialized_end = 462
    _TRIGGERSMARTCONTRACT._serialized_start = 465
    _TRIGGERSMARTCONTRACT._serialized_end = 614
    _TRANSACTION._serialized_start = 617
    _TRANSACTION._serialized_end = 2097
    _TRANSACTION_CONTRACT._serialized_start = 697
    _TRANSACTION_CONTRACT._serialized_end = 1842
    _TRANSACTION_CONTRACT_CONTRACTTYPE._serialized_start = 873
    _TRANSACTION_CONTRACT_CONTRACTTYPE._serialized_end = 1842
    _TRANSACTION_RAW._serialized_start = 1845
    _TRANSACTION_RAW._serialized_end = 2097
# @@protoc_insertion_point(module_scope)
