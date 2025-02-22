# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ibc/applications/transfer/v1/query.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a+ibc/applications/transfer/v1/transfer.proto\x1a\x1cgoogle/api/annotations.proto\"&\n\x16QueryDenomTraceRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\"X\n\x17QueryDenomTraceResponse\x12=\n\x0b\x64\x65nom_trace\x18\x01 \x01(\x0b\x32(.ibc.applications.transfer.v1.DenomTrace\"U\n\x17QueryDenomTracesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xa7\x01\n\x18QueryDenomTracesResponse\x12N\n\x0c\x64\x65nom_traces\x18\x01 \x03(\x0b\x32(.ibc.applications.transfer.v1.DenomTraceB\x0e\xaa\xdf\x1f\x06Traces\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x14\n\x12QueryParamsRequest\"K\n\x13QueryParamsResponse\x12\x34\n\x06params\x18\x01 \x01(\x0b\x32$.ibc.applications.transfer.v1.Params\"&\n\x15QueryDenomHashRequest\x12\r\n\x05trace\x18\x01 \x01(\t\"&\n\x16QueryDenomHashResponse\x12\x0c\n\x04hash\x18\x01 \x01(\t\"@\n\x19QueryEscrowAddressRequest\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\"4\n\x1aQueryEscrowAddressResponse\x12\x16\n\x0e\x65scrow_address\x18\x01 \x01(\t2\xfd\x06\n\x05Query\x12\xac\x01\n\nDenomTrace\x12\x34.ibc.applications.transfer.v1.QueryDenomTraceRequest\x1a\x35.ibc.applications.transfer.v1.QueryDenomTraceResponse\"1\x82\xd3\xe4\x93\x02+\x12)/ibc/apps/transfer/v1/denom_traces/{hash}\x12\xa8\x01\n\x0b\x44\x65nomTraces\x12\x35.ibc.applications.transfer.v1.QueryDenomTracesRequest\x1a\x36.ibc.applications.transfer.v1.QueryDenomTracesResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/ibc/apps/transfer/v1/denom_traces\x12\x93\x01\n\x06Params\x12\x30.ibc.applications.transfer.v1.QueryParamsRequest\x1a\x31.ibc.applications.transfer.v1.QueryParamsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/transfer/v1/params\x12\xaa\x01\n\tDenomHash\x12\x33.ibc.applications.transfer.v1.QueryDenomHashRequest\x1a\x34.ibc.applications.transfer.v1.QueryDenomHashResponse\"2\x82\xd3\xe4\x93\x02,\x12*/ibc/apps/transfer/v1/denom_hashes/{trace}\x12\xd6\x01\n\rEscrowAddress\x12\x37.ibc.applications.transfer.v1.QueryEscrowAddressRequest\x1a\x38.ibc.applications.transfer.v1.QueryEscrowAddressResponse\"R\x82\xd3\xe4\x93\x02L\x12J/ibc/apps/transfer/v1/channels/{channel_id}/ports/{port_id}/escrow_addressB9Z7github.com/cosmos/ibc-go/v3/modules/apps/transfer/typesb\x06proto3')



_QUERYDENOMTRACEREQUEST = DESCRIPTOR.message_types_by_name['QueryDenomTraceRequest']
_QUERYDENOMTRACERESPONSE = DESCRIPTOR.message_types_by_name['QueryDenomTraceResponse']
_QUERYDENOMTRACESREQUEST = DESCRIPTOR.message_types_by_name['QueryDenomTracesRequest']
_QUERYDENOMTRACESRESPONSE = DESCRIPTOR.message_types_by_name['QueryDenomTracesResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYDENOMHASHREQUEST = DESCRIPTOR.message_types_by_name['QueryDenomHashRequest']
_QUERYDENOMHASHRESPONSE = DESCRIPTOR.message_types_by_name['QueryDenomHashResponse']
_QUERYESCROWADDRESSREQUEST = DESCRIPTOR.message_types_by_name['QueryEscrowAddressRequest']
_QUERYESCROWADDRESSRESPONSE = DESCRIPTOR.message_types_by_name['QueryEscrowAddressResponse']
QueryDenomTraceRequest = _reflection.GeneratedProtocolMessageType('QueryDenomTraceRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMTRACEREQUEST,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomTraceRequest)
  })
_sym_db.RegisterMessage(QueryDenomTraceRequest)

QueryDenomTraceResponse = _reflection.GeneratedProtocolMessageType('QueryDenomTraceResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMTRACERESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomTraceResponse)
  })
_sym_db.RegisterMessage(QueryDenomTraceResponse)

QueryDenomTracesRequest = _reflection.GeneratedProtocolMessageType('QueryDenomTracesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMTRACESREQUEST,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomTracesRequest)
  })
_sym_db.RegisterMessage(QueryDenomTracesRequest)

QueryDenomTracesResponse = _reflection.GeneratedProtocolMessageType('QueryDenomTracesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMTRACESRESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomTracesResponse)
  })
_sym_db.RegisterMessage(QueryDenomTracesResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryDenomHashRequest = _reflection.GeneratedProtocolMessageType('QueryDenomHashRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMHASHREQUEST,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomHashRequest)
  })
_sym_db.RegisterMessage(QueryDenomHashRequest)

QueryDenomHashResponse = _reflection.GeneratedProtocolMessageType('QueryDenomHashResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMHASHRESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryDenomHashResponse)
  })
_sym_db.RegisterMessage(QueryDenomHashResponse)

QueryEscrowAddressRequest = _reflection.GeneratedProtocolMessageType('QueryEscrowAddressRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYESCROWADDRESSREQUEST,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryEscrowAddressRequest)
  })
_sym_db.RegisterMessage(QueryEscrowAddressRequest)

QueryEscrowAddressResponse = _reflection.GeneratedProtocolMessageType('QueryEscrowAddressResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYESCROWADDRESSRESPONSE,
  '__module__' : 'ibc.applications.transfer.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:ibc.applications.transfer.v1.QueryEscrowAddressResponse)
  })
_sym_db.RegisterMessage(QueryEscrowAddressResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/ibc-go/v3/modules/apps/transfer/types'
  _QUERYDENOMTRACESRESPONSE.fields_by_name['denom_traces']._options = None
  _QUERYDENOMTRACESRESPONSE.fields_by_name['denom_traces']._serialized_options = b'\252\337\037\006Traces\310\336\037\000'
  _QUERY.methods_by_name['DenomTrace']._options = None
  _QUERY.methods_by_name['DenomTrace']._serialized_options = b'\202\323\344\223\002+\022)/ibc/apps/transfer/v1/denom_traces/{hash}'
  _QUERY.methods_by_name['DenomTraces']._options = None
  _QUERY.methods_by_name['DenomTraces']._serialized_options = b'\202\323\344\223\002$\022\"/ibc/apps/transfer/v1/denom_traces'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\036\022\034/ibc/apps/transfer/v1/params'
  _QUERY.methods_by_name['DenomHash']._options = None
  _QUERY.methods_by_name['DenomHash']._serialized_options = b'\202\323\344\223\002,\022*/ibc/apps/transfer/v1/denom_hashes/{trace}'
  _QUERY.methods_by_name['EscrowAddress']._options = None
  _QUERY.methods_by_name['EscrowAddress']._serialized_options = b'\202\323\344\223\002L\022J/ibc/apps/transfer/v1/channels/{channel_id}/ports/{port_id}/escrow_address'
  _QUERYDENOMTRACEREQUEST._serialized_start=215
  _QUERYDENOMTRACEREQUEST._serialized_end=253
  _QUERYDENOMTRACERESPONSE._serialized_start=255
  _QUERYDENOMTRACERESPONSE._serialized_end=343
  _QUERYDENOMTRACESREQUEST._serialized_start=345
  _QUERYDENOMTRACESREQUEST._serialized_end=430
  _QUERYDENOMTRACESRESPONSE._serialized_start=433
  _QUERYDENOMTRACESRESPONSE._serialized_end=600
  _QUERYPARAMSREQUEST._serialized_start=602
  _QUERYPARAMSREQUEST._serialized_end=622
  _QUERYPARAMSRESPONSE._serialized_start=624
  _QUERYPARAMSRESPONSE._serialized_end=699
  _QUERYDENOMHASHREQUEST._serialized_start=701
  _QUERYDENOMHASHREQUEST._serialized_end=739
  _QUERYDENOMHASHRESPONSE._serialized_start=741
  _QUERYDENOMHASHRESPONSE._serialized_end=779
  _QUERYESCROWADDRESSREQUEST._serialized_start=781
  _QUERYESCROWADDRESSREQUEST._serialized_end=845
  _QUERYESCROWADDRESSRESPONSE._serialized_start=847
  _QUERYESCROWADDRESSRESPONSE._serialized_end=899
  _QUERY._serialized_start=902
  _QUERY._serialized_end=1795
# @@protoc_insertion_point(module_scope)
