# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/v1beta1/coin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmpy.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmos/base/v1beta1/coin.proto\x12\x13\x63osmos.base.v1beta1\x1a\x14gogoproto/gogo.proto\"8\n\x04\x43oin\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x1b\n\x06\x61mount\x18\x02 \x01(\tB\x0b\xda\xde\x1f\x03Int\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01\";\n\x07\x44\x65\x63\x43oin\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x1b\n\x06\x61mount\x18\x02 \x01(\tB\x0b\xda\xde\x1f\x03\x44\x65\x63\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01\"$\n\x08IntProto\x12\x18\n\x03int\x18\x01 \x01(\tB\x0b\xda\xde\x1f\x03Int\xc8\xde\x1f\x00\"$\n\x08\x44\x65\x63Proto\x12\x18\n\x03\x64\x65\x63\x18\x01 \x01(\tB\x0b\xda\xde\x1f\x03\x44\x65\x63\xc8\xde\x1f\x00\x42,Z\"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00\x62\x06proto3')



_COIN = DESCRIPTOR.message_types_by_name['Coin']
_DECCOIN = DESCRIPTOR.message_types_by_name['DecCoin']
_INTPROTO = DESCRIPTOR.message_types_by_name['IntProto']
_DECPROTO = DESCRIPTOR.message_types_by_name['DecProto']
Coin = _reflection.GeneratedProtocolMessageType('Coin', (_message.Message,), {
  'DESCRIPTOR' : _COIN,
  '__module__' : 'cosmos.base.v1beta1.coin_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.v1beta1.Coin)
  })
_sym_db.RegisterMessage(Coin)

DecCoin = _reflection.GeneratedProtocolMessageType('DecCoin', (_message.Message,), {
  'DESCRIPTOR' : _DECCOIN,
  '__module__' : 'cosmos.base.v1beta1.coin_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.v1beta1.DecCoin)
  })
_sym_db.RegisterMessage(DecCoin)

IntProto = _reflection.GeneratedProtocolMessageType('IntProto', (_message.Message,), {
  'DESCRIPTOR' : _INTPROTO,
  '__module__' : 'cosmos.base.v1beta1.coin_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.v1beta1.IntProto)
  })
_sym_db.RegisterMessage(IntProto)

DecProto = _reflection.GeneratedProtocolMessageType('DecProto', (_message.Message,), {
  'DESCRIPTOR' : _DECPROTO,
  '__module__' : 'cosmos.base.v1beta1.coin_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.v1beta1.DecProto)
  })
_sym_db.RegisterMessage(DecProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\"github.com/cosmos/cosmos-sdk/types\330\341\036\000\200\342\036\000'
  _COIN.fields_by_name['amount']._options = None
  _COIN.fields_by_name['amount']._serialized_options = b'\332\336\037\003Int\310\336\037\000'
  _COIN._options = None
  _COIN._serialized_options = b'\350\240\037\001'
  _DECCOIN.fields_by_name['amount']._options = None
  _DECCOIN.fields_by_name['amount']._serialized_options = b'\332\336\037\003Dec\310\336\037\000'
  _DECCOIN._options = None
  _DECCOIN._serialized_options = b'\350\240\037\001'
  _INTPROTO.fields_by_name['int']._options = None
  _INTPROTO.fields_by_name['int']._serialized_options = b'\332\336\037\003Int\310\336\037\000'
  _DECPROTO.fields_by_name['dec']._options = None
  _DECPROTO.fields_by_name['dec']._serialized_options = b'\332\336\037\003Dec\310\336\037\000'
  _COIN._serialized_start=77
  _COIN._serialized_end=133
  _DECCOIN._serialized_start=135
  _DECCOIN._serialized_end=194
  _INTPROTO._serialized_start=196
  _INTPROTO._serialized_end=232
  _DECPROTO._serialized_start=234
  _DECPROTO._serialized_end=270
# @@protoc_insertion_point(module_scope)
