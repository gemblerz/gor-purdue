# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goras_goal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='goras_goal.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10goras_goal.proto\"\xa9\x01\n\tGorasGoal\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x30\n\x0fmaintenanceGoal\x18\x03 \x01(\x0b\x32\x15.GorasMaintenanceGoalH\x00\x12(\n\x0bperformGoal\x18\x04 \x01(\x0b\x32\x11.GorasPerformGoalH\x00\x12\x0e\n\x06parent\x18\x05 \x01(\x05\x12\x0e\n\x06\x63hilds\x18\x06 \x03(\x05\x42\x06\n\x04goal\"\x16\n\x14GorasMaintenanceGoal\"\x12\n\x10GorasPerformGoalb\x06proto3')
)




_GORASGOAL = _descriptor.Descriptor(
  name='GorasGoal',
  full_name='GorasGoal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GorasGoal.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='GorasGoal.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maintenanceGoal', full_name='GorasGoal.maintenanceGoal', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='performGoal', full_name='GorasGoal.performGoal', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent', full_name='GorasGoal.parent', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='childs', full_name='GorasGoal.childs', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='goal', full_name='GorasGoal.goal',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=21,
  serialized_end=190,
)


_GORASMAINTENANCEGOAL = _descriptor.Descriptor(
  name='GorasMaintenanceGoal',
  full_name='GorasMaintenanceGoal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=214,
)


_GORASPERFORMGOAL = _descriptor.Descriptor(
  name='GorasPerformGoal',
  full_name='GorasPerformGoal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=234,
)

_GORASGOAL.fields_by_name['maintenanceGoal'].message_type = _GORASMAINTENANCEGOAL
_GORASGOAL.fields_by_name['performGoal'].message_type = _GORASPERFORMGOAL
_GORASGOAL.oneofs_by_name['goal'].fields.append(
  _GORASGOAL.fields_by_name['maintenanceGoal'])
_GORASGOAL.fields_by_name['maintenanceGoal'].containing_oneof = _GORASGOAL.oneofs_by_name['goal']
_GORASGOAL.oneofs_by_name['goal'].fields.append(
  _GORASGOAL.fields_by_name['performGoal'])
_GORASGOAL.fields_by_name['performGoal'].containing_oneof = _GORASGOAL.oneofs_by_name['goal']
DESCRIPTOR.message_types_by_name['GorasGoal'] = _GORASGOAL
DESCRIPTOR.message_types_by_name['GorasMaintenanceGoal'] = _GORASMAINTENANCEGOAL
DESCRIPTOR.message_types_by_name['GorasPerformGoal'] = _GORASPERFORMGOAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GorasGoal = _reflection.GeneratedProtocolMessageType('GorasGoal', (_message.Message,), dict(
  DESCRIPTOR = _GORASGOAL,
  __module__ = 'goras_goal_pb2'
  # @@protoc_insertion_point(class_scope:GorasGoal)
  ))
_sym_db.RegisterMessage(GorasGoal)

GorasMaintenanceGoal = _reflection.GeneratedProtocolMessageType('GorasMaintenanceGoal', (_message.Message,), dict(
  DESCRIPTOR = _GORASMAINTENANCEGOAL,
  __module__ = 'goras_goal_pb2'
  # @@protoc_insertion_point(class_scope:GorasMaintenanceGoal)
  ))
_sym_db.RegisterMessage(GorasMaintenanceGoal)

GorasPerformGoal = _reflection.GeneratedProtocolMessageType('GorasPerformGoal', (_message.Message,), dict(
  DESCRIPTOR = _GORASPERFORMGOAL,
  __module__ = 'goras_goal_pb2'
  # @@protoc_insertion_point(class_scope:GorasPerformGoal)
  ))
_sym_db.RegisterMessage(GorasPerformGoal)


# @@protoc_insertion_point(module_scope)