# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: vpn.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'vpn.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tvpn.proto\"\x07\n\x05\x45mpty\"$\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\"M\n\x0c\x44\x61taPengguna\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x04nama\x18\x02 \x01(\x0b\x32\x05.User\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\r\n\x05no_hp\x18\x04 \x01(\x03\"0\n\x10\x44\x61taPenggunaList\x12\x1c\n\x05users\x18\x01 \x03(\x0b\x32\r.DataPengguna2;\n\x0bUserService\x12,\n\x0fGetDataPengguna\x12\x06.Empty\x1a\x11.DataPenggunaListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vpn_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=13
  _globals['_EMPTY']._serialized_end=20
  _globals['_USER']._serialized_start=22
  _globals['_USER']._serialized_end=58
  _globals['_DATAPENGGUNA']._serialized_start=60
  _globals['_DATAPENGGUNA']._serialized_end=137
  _globals['_DATAPENGGUNALIST']._serialized_start=139
  _globals['_DATAPENGGUNALIST']._serialized_end=187
  _globals['_USERSERVICE']._serialized_start=189
  _globals['_USERSERVICE']._serialized_end=248
# @@protoc_insertion_point(module_scope)
