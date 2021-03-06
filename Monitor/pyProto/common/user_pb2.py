# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/user.proto',
  package='common',
  syntax='proto3',
  serialized_options=_b('\n\020frame.game.proto'),
  serialized_pb=_b('\n\x11\x63ommon/user.proto\x12\x06\x63ommon\"\x98\x06\n\x08UserInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x17\n\x0fparentAccountId\x18\x02 \x01(\x05\x12\x0f\n\x07\x61\x63\x63ount\x18\x03 \x01(\t\x12\x11\n\taccountId\x18\x04 \x01(\x05\x12\r\n\x05state\x18\x06 \x01(\x05\x12\x0e\n\x06status\x18\x07 \x01(\x05\x12\x0f\n\x07levelId\x18\x08 \x01(\x05\x12\x10\n\x08portrait\x18\t \x01(\t\x12\x10\n\x08realName\x18\n \x01(\t\x12\r\n\x05phone\x18\x0b \x01(\t\x12\x0e\n\x06gender\x18\x0c \x01(\x05\x12\x0e\n\x06weixin\x18\x0f \x01(\t\x12\x10\n\x08\x62\x61nkName\x18\x11 \x01(\t\x12\x14\n\x0c\x62\x61nkProvince\x18\x12 \x01(\t\x12\x13\n\x0b\x62\x61nkAccount\x18\x14 \x01(\t\x12\x17\n\x0f\x62\x61nkAccountName\x18\x15 \x01(\t\x12\x10\n\x08nickName\x18\x17 \x01(\t\x12\x12\n\nsafeStatus\x18\x19 \x01(\x05\x12\x0e\n\x06siteId\x18\x1a \x01(\x05\x12\x0e\n\x06modeId\x18\x1b \x01(\x05\x12\x0e\n\x06playId\x18\x1c \x01(\x05\x12\x14\n\x0c\x61liAccountId\x18\x1d \x01(\t\x12\x16\n\x0e\x61liAccountName\x18\x1e \x01(\t\x12\x13\n\x0bpayBankFlag\x18! \x01(\x05\x12\x15\n\rpayAlipayFlag\x18\" \x01(\x05\x12\x0b\n\x03vip\x18# \x01(\t\x12\r\n\x05money\x18$ \x01(\x03\x12\x10\n\x08integral\x18% \x01(\x05\x12\x10\n\x08uniqueId\x18& \x01(\x03\x12\x14\n\x0c\x63ontrolMoney\x18\' \x01(\x05\x12\x16\n\x0e\x63ontrolBetRate\x18( \x01(\x05\x12\x17\n\x0f\x63ontrolFishRate\x18) \x01(\x05\x12\x18\n\x10leftControlMoney\x18* \x01(\x05\x12\x0f\n\x07\x66ishWin\x18+ \x01(\x05\x12\x0c\n\x04safe\x18, \x01(\x03\x12\n\n\x02ip\x18- \x01(\x05\x12\x17\n\x0f\x61\x63\x63ountRecharge\x18. \x01(\x05\x12\x19\n\x11\x61\x63\x63ountWithdrawal\x18/ \x01(\x05\x12\x12\n\naccountBet\x18\x30 \x01(\x05\x12\x16\n\x0e\x61\x63\x63ountBalance\x18\x31 \x01(\x05\x12\x0e\n\x06\x62\x61nkId\x18\x32 \x01(\x05\x42\x12\n\x10\x66rame.game.protob\x06proto3')
)




_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='common.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='common.UserInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentAccountId', full_name='common.UserInfo.parentAccountId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account', full_name='common.UserInfo.account', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accountId', full_name='common.UserInfo.accountId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='common.UserInfo.state', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='common.UserInfo.status', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='levelId', full_name='common.UserInfo.levelId', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='common.UserInfo.portrait', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='realName', full_name='common.UserInfo.realName', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone', full_name='common.UserInfo.phone', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='common.UserInfo.gender', index=10,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weixin', full_name='common.UserInfo.weixin', index=11,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bankName', full_name='common.UserInfo.bankName', index=12,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bankProvince', full_name='common.UserInfo.bankProvince', index=13,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bankAccount', full_name='common.UserInfo.bankAccount', index=14,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bankAccountName', full_name='common.UserInfo.bankAccountName', index=15,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nickName', full_name='common.UserInfo.nickName', index=16,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='safeStatus', full_name='common.UserInfo.safeStatus', index=17,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='siteId', full_name='common.UserInfo.siteId', index=18,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modeId', full_name='common.UserInfo.modeId', index=19,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playId', full_name='common.UserInfo.playId', index=20,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aliAccountId', full_name='common.UserInfo.aliAccountId', index=21,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aliAccountName', full_name='common.UserInfo.aliAccountName', index=22,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payBankFlag', full_name='common.UserInfo.payBankFlag', index=23,
      number=33, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payAlipayFlag', full_name='common.UserInfo.payAlipayFlag', index=24,
      number=34, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vip', full_name='common.UserInfo.vip', index=25,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='common.UserInfo.money', index=26,
      number=36, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integral', full_name='common.UserInfo.integral', index=27,
      number=37, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uniqueId', full_name='common.UserInfo.uniqueId', index=28,
      number=38, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controlMoney', full_name='common.UserInfo.controlMoney', index=29,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controlBetRate', full_name='common.UserInfo.controlBetRate', index=30,
      number=40, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controlFishRate', full_name='common.UserInfo.controlFishRate', index=31,
      number=41, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leftControlMoney', full_name='common.UserInfo.leftControlMoney', index=32,
      number=42, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fishWin', full_name='common.UserInfo.fishWin', index=33,
      number=43, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='safe', full_name='common.UserInfo.safe', index=34,
      number=44, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='common.UserInfo.ip', index=35,
      number=45, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accountRecharge', full_name='common.UserInfo.accountRecharge', index=36,
      number=46, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accountWithdrawal', full_name='common.UserInfo.accountWithdrawal', index=37,
      number=47, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accountBet', full_name='common.UserInfo.accountBet', index=38,
      number=48, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accountBalance', full_name='common.UserInfo.accountBalance', index=39,
      number=49, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bankId', full_name='common.UserInfo.bankId', index=40,
      number=50, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=822,
)

DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'common.user_pb2'
  # @@protoc_insertion_point(class_scope:common.UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
