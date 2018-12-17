# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='param.proto',
  package='esa.egos.ares.dataprovision.model.param',
  serialized_pb=_b('\n\x0bparam.proto\x12\'esa.egos.ares.dataprovision.model.param\"\xf5\x01\n\x0fParamDefinition\x12\x0b\n\x03pid\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04unit\x18\x04 \x01(\t\x12;\n\x04type\x18\x05 \x02(\x0e\x32-.esa.egos.ares.dataprovision.model.param.Type\x12?\n\x08raw_type\x18\x06 \x02(\x0e\x32-.esa.egos.ares.dataprovision.model.param.Type\x12\x0e\n\x06\x61\x63tive\x18\x07 \x01(\x08\x12\x16\n\x0esystem_element\x18\x08 \x01(\t\"\xb6\x04\n\x0bParamSample\x12\x0b\n\x03pid\x18\x01 \x02(\x05\x12\x10\n\x08gen_time\x18\x02 \x02(\x03\x12\x14\n\x0cstorage_time\x18\x03 \x01(\x03\x12O\n\x08validity\x18\x04 \x02(\x0e\x32=.esa.egos.ares.dataprovision.model.param.ParamSample.Validity\x12\r\n\x05state\x18\x05 \x01(\x05\x12;\n\x04type\x18\x06 \x01(\x0e\x32-.esa.egos.ares.dataprovision.model.param.Type\x12\r\n\x05v_bit\x18\x07 \x01(\x08\x12\x0e\n\x06v_long\x18\x08 \x01(\x12\x12\r\n\x05v_flt\x18\t \x01(\x02\x12\r\n\x05v_dbl\x18\n \x01(\x01\x12\r\n\x05v_str\x18\x0b \x01(\t\x12?\n\x08raw_type\x18\x0c \x01(\x0e\x32-.esa.egos.ares.dataprovision.model.param.Type\x12\x11\n\traw_v_bit\x18\r \x01(\x08\x12\x12\n\nraw_v_long\x18\x0e \x01(\x12\x12\x11\n\traw_v_flt\x18\x0f \x01(\x02\x12\x11\n\traw_v_dbl\x18\x10 \x01(\x01\x12\x11\n\traw_v_str\x18\x11 \x01(\t\x12\x11\n\tparent_id\x18\x12 \x01(\r\x12\x17\n\x0fparent_gen_time\x18\x13 \x01(\x03\"<\n\x08Validity\x12\t\n\x05VALID\x10\x00\x12\x0b\n\x07INVALID\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x12\x0b\n\x07\x45XPIRED\x10\x03\"\xb2\x01\n\x17\x41ggregateParamStatistic\x12\x0b\n\x03pid\x18\x01 \x02(\x05\x12\x12\n\nstart_time\x18\x02 \x02(\x03\x12\x14\n\x0cstorage_time\x18\x03 \x01(\x03\x12\x10\n\x08no_valid\x18\x04 \x02(\x03\x12\x12\n\nno_invalid\x18\x05 \x02(\x03\x12\x0b\n\x03min\x18\x06 \x01(\x01\x12\x0b\n\x03max\x18\x07 \x01(\x01\x12\x0f\n\x07\x61verage\x18\x08 \x01(\x01\x12\x0f\n\x07std_dev\x18\t \x01(\x01*\xcd\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03\x42IT\x10\x01\x12\x0c\n\x08UTINYINT\x10\x02\x12\r\n\tUSMALLINT\x10\x04\x12\x0e\n\nUMEDIUMINT\x10\x06\x12\x08\n\x04UINT\x10\t\x12\x0c\n\x08STINYINT\x10\x03\x12\r\n\tSSMALLINT\x10\x05\x12\x0e\n\nSMEDIUMINT\x10\x07\x12\x08\n\x04SINT\x10\x08\x12\t\n\x05\x46LOAT\x10\n\x12\n\n\x06\x44OUBLE\x10\x0b\x12\x0c\n\x08\x44\x41TETIME\x10\r\x12\n\n\x06STRING\x10\x0c\x12\x07\n\x03JOB\x10\x0e\x12\x07\n\x03LOG\x10\x0f')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='esa.egos.ares.dataprovision.model.param.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UTINYINT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USMALLINT', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UMEDIUMINT', index=4, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT', index=5, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STINYINT', index=6, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSMALLINT', index=7, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMEDIUMINT', index=8, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINT', index=9, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=13, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOB', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=15, number=15,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1055,
  serialized_end=1260,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
UNKNOWN = 0
BIT = 1
UTINYINT = 2
USMALLINT = 4
UMEDIUMINT = 6
UINT = 9
STINYINT = 3
SSMALLINT = 5
SMEDIUMINT = 7
SINT = 8
FLOAT = 10
DOUBLE = 11
DATETIME = 13
STRING = 12
JOB = 14
LOG = 15


_PARAMSAMPLE_VALIDITY = _descriptor.EnumDescriptor(
  name='Validity',
  full_name='esa.egos.ares.dataprovision.model.param.ParamSample.Validity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=811,
  serialized_end=871,
)
_sym_db.RegisterEnumDescriptor(_PARAMSAMPLE_VALIDITY)


_PARAMDEFINITION = _descriptor.Descriptor(
  name='ParamDefinition',
  full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition.pid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit', full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition.unit', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition.type', index=4,
      number=5, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_type', full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition.raw_type', index=5,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active', full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition.active', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_element', full_name='esa.egos.ares.dataprovision.model.param.ParamDefinition.system_element', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=302,
)


_PARAMSAMPLE = _descriptor.Descriptor(
  name='ParamSample',
  full_name='esa.egos.ares.dataprovision.model.param.ParamSample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.pid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gen_time', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.gen_time', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='storage_time', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.storage_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validity', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.validity', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.state', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_bit', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.v_bit', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_long', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.v_long', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_flt', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.v_flt', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_dbl', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.v_dbl', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_str', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.v_str', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_type', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.raw_type', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_v_bit', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.raw_v_bit', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_v_long', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.raw_v_long', index=13,
      number=14, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_v_flt', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.raw_v_flt', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_v_dbl', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.raw_v_dbl', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_v_str', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.raw_v_str', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.parent_id', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_gen_time', full_name='esa.egos.ares.dataprovision.model.param.ParamSample.parent_gen_time', index=18,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PARAMSAMPLE_VALIDITY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=871,
)


_AGGREGATEPARAMSTATISTIC = _descriptor.Descriptor(
  name='AggregateParamStatistic',
  full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.pid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.start_time', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='storage_time', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.storage_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no_valid', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.no_valid', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no_invalid', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.no_invalid', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.min', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.max', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.average', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='std_dev', full_name='esa.egos.ares.dataprovision.model.param.AggregateParamStatistic.std_dev', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=874,
  serialized_end=1052,
)

_PARAMDEFINITION.fields_by_name['type'].enum_type = _TYPE
_PARAMDEFINITION.fields_by_name['raw_type'].enum_type = _TYPE
_PARAMSAMPLE.fields_by_name['validity'].enum_type = _PARAMSAMPLE_VALIDITY
_PARAMSAMPLE.fields_by_name['type'].enum_type = _TYPE
_PARAMSAMPLE.fields_by_name['raw_type'].enum_type = _TYPE
_PARAMSAMPLE_VALIDITY.containing_type = _PARAMSAMPLE
DESCRIPTOR.message_types_by_name['ParamDefinition'] = _PARAMDEFINITION
DESCRIPTOR.message_types_by_name['ParamSample'] = _PARAMSAMPLE
DESCRIPTOR.message_types_by_name['AggregateParamStatistic'] = _AGGREGATEPARAMSTATISTIC
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE

ParamDefinition = _reflection.GeneratedProtocolMessageType('ParamDefinition', (_message.Message,), dict(
  DESCRIPTOR = _PARAMDEFINITION,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:esa.egos.ares.dataprovision.model.param.ParamDefinition)
  ))
_sym_db.RegisterMessage(ParamDefinition)

ParamSample = _reflection.GeneratedProtocolMessageType('ParamSample', (_message.Message,), dict(
  DESCRIPTOR = _PARAMSAMPLE,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:esa.egos.ares.dataprovision.model.param.ParamSample)
  ))
_sym_db.RegisterMessage(ParamSample)

AggregateParamStatistic = _reflection.GeneratedProtocolMessageType('AggregateParamStatistic', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATEPARAMSTATISTIC,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:esa.egos.ares.dataprovision.model.param.AggregateParamStatistic)
  ))
_sym_db.RegisterMessage(AggregateParamStatistic)


# @@protoc_insertion_point(module_scope)