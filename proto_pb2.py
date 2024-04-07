# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bproto.proto\"\x07\n\x05\x45mpty\"P\n\x0b\x41rtistProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nartistName\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\x10\n\x08realName\x18\x04 \x01(\t\"J\n\x11InsertArtistProto\x12\x12\n\nartistName\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\x12\x10\n\x08realName\x18\x03 \x01(\t\"\x1b\n\rArtistIdProto\x12\n\n\x02id\x18\x01 \x01(\t\"7\n\nLabelProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\"1\n\x10InsertLabelProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x02 \x01(\t\"\x1a\n\x0cLabelIdProto\x12\n\n\x02id\x18\x01 \x01(\t\"\xc7\x01\n\x0bRecordProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x1c\n\x06\x61rtist\x18\x03 \x01(\x0b\x32\x0c.ArtistProto\x12\r\n\x05genre\x18\x04 \x01(\t\x12\r\n\x05style\x18\x05 \x01(\t\x12\x13\n\x0breleaseDate\x18\x06 \x01(\t\x12\x1a\n\x05label\x18\x07 \x01(\x0b\x32\x0b.LabelProto\x12\x0f\n\x07\x63ountry\x18\x08 \x01(\t\x12\r\n\x05price\x18\t \x01(\x01\x12\x10\n\x08quantity\x18\n \x01(\x05\"\xaa\x01\n\x11InsertRecordProto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08\x61rtistId\x18\x02 \x01(\t\x12\r\n\x05genre\x18\x03 \x01(\t\x12\r\n\x05style\x18\x04 \x01(\t\x12\x13\n\x0breleaseDate\x18\x05 \x01(\t\x12\x0f\n\x07labelId\x18\x06 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12\r\n\x05price\x18\x08 \x01(\x01\x12\x10\n\x08quantity\x18\t \x01(\x05\"\x1b\n\rRecordIdProto\x12\n\n\x02id\x18\x01 \x01(\t\":\n\x1aUpdateQuantityRequestProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"4\n\x17UpdatePriceRequestProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x01\x32\xae\x01\n\x11\x41rtistGrpcService\x12\"\n\x06GetAll\x12\x06.Empty\x1a\x0c.ArtistProto\"\x00\x30\x01\x12)\n\x07GetById\x12\x0e.ArtistIdProto\x1a\x0c.ArtistProto\"\x00\x12&\n\x06Insert\x12\x12.InsertArtistProto\x1a\x06.Empty\"\x00\x12\"\n\x06\x44\x65lete\x12\x0e.ArtistIdProto\x1a\x06.Empty\"\x00\x32\x9a\x02\n\x11RecordGrpcService\x12\"\n\x06GetAll\x12\x06.Empty\x1a\x0c.RecordProto\"\x00\x30\x01\x12)\n\x07GetById\x12\x0e.RecordIdProto\x1a\x0c.RecordProto\"\x00\x12&\n\x06Insert\x12\x12.InsertRecordProto\x1a\x06.Empty\"\x00\x12\x37\n\x0eUpdateQuantity\x12\x1b.UpdateQuantityRequestProto\x1a\x06.Empty\"\x00\x12\x31\n\x0bUpdatePrice\x12\x18.UpdatePriceRequestProto\x1a\x06.Empty\"\x00\x12\"\n\x06\x44\x65lete\x12\x0e.RecordIdProto\x1a\x06.Empty\"\x00\x32\xa8\x01\n\x10LabelGrpcService\x12!\n\x06GetAll\x12\x06.Empty\x1a\x0b.LabelProto\"\x00\x30\x01\x12\'\n\x07GetById\x12\r.LabelIdProto\x1a\x0b.LabelProto\"\x00\x12%\n\x06Insert\x12\x11.InsertLabelProto\x1a\x06.Empty\"\x00\x12!\n\x06\x44\x65lete\x12\r.LabelIdProto\x1a\x06.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=15
  _globals['_EMPTY']._serialized_end=22
  _globals['_ARTISTPROTO']._serialized_start=24
  _globals['_ARTISTPROTO']._serialized_end=104
  _globals['_INSERTARTISTPROTO']._serialized_start=106
  _globals['_INSERTARTISTPROTO']._serialized_end=180
  _globals['_ARTISTIDPROTO']._serialized_start=182
  _globals['_ARTISTIDPROTO']._serialized_end=209
  _globals['_LABELPROTO']._serialized_start=211
  _globals['_LABELPROTO']._serialized_end=266
  _globals['_INSERTLABELPROTO']._serialized_start=268
  _globals['_INSERTLABELPROTO']._serialized_end=317
  _globals['_LABELIDPROTO']._serialized_start=319
  _globals['_LABELIDPROTO']._serialized_end=345
  _globals['_RECORDPROTO']._serialized_start=348
  _globals['_RECORDPROTO']._serialized_end=547
  _globals['_INSERTRECORDPROTO']._serialized_start=550
  _globals['_INSERTRECORDPROTO']._serialized_end=720
  _globals['_RECORDIDPROTO']._serialized_start=722
  _globals['_RECORDIDPROTO']._serialized_end=749
  _globals['_UPDATEQUANTITYREQUESTPROTO']._serialized_start=751
  _globals['_UPDATEQUANTITYREQUESTPROTO']._serialized_end=809
  _globals['_UPDATEPRICEREQUESTPROTO']._serialized_start=811
  _globals['_UPDATEPRICEREQUESTPROTO']._serialized_end=863
  _globals['_ARTISTGRPCSERVICE']._serialized_start=866
  _globals['_ARTISTGRPCSERVICE']._serialized_end=1040
  _globals['_RECORDGRPCSERVICE']._serialized_start=1043
  _globals['_RECORDGRPCSERVICE']._serialized_end=1325
  _globals['_LABELGRPCSERVICE']._serialized_start=1328
  _globals['_LABELGRPCSERVICE']._serialized_end=1496
# @@protoc_insertion_point(module_scope)