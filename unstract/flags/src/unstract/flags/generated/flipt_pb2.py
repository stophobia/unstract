# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unstract/flags/src/unstract/flags/protos/flipt.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n4unstract/flags/src/unstract/flags/protos/flipt.proto\x12\x05\x66lipt\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcb\x01\n\x11\x45valuationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x11\n\tentity_id\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x03(\x0b\x32%.flipt.EvaluationRequest.ContextEntry\x12\x15\n\rnamespace_key\x18\x05 \x01(\t\x1a.\n\x0c\x43ontextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x8a\x01\n\x16\x42\x61tchEvaluationRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12*\n\x08requests\x18\x02 \x03(\x0b\x32\x18.flipt.EvaluationRequest\x12\x19\n\x11\x65xclude_not_found\x18\x03 \x01(\x08\x12\x15\n\rnamespace_key\x18\x04 \x01(\t"|\n\x17\x42\x61tchEvaluationResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12,\n\tresponses\x18\x02 \x03(\x0b\x32\x19.flipt.EvaluationResponse\x12\x1f\n\x17request_duration_millis\x18\x03 \x01(\x01"\xbd\x03\n\x12\x45valuationResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x11\n\tentity_id\x18\x02 \x01(\t\x12\x46\n\x0frequest_context\x18\x03 \x03(\x0b\x32-.flipt.EvaluationResponse.RequestContextEntry\x12\r\n\x05match\x18\x04 \x01(\x08\x12\x10\n\x08\x66lag_key\x18\x05 \x01(\t\x12\x17\n\x0bsegment_key\x18\x06 \x01(\tB\x02\x18\x01\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x08 \x01(\t\x12\x1f\n\x17request_duration_millis\x18\t \x01(\x01\x12\x12\n\nattachment\x18\n \x01(\t\x12\'\n\x06reason\x18\x0b \x01(\x0e\x32\x17.flipt.EvaluationReason\x12\x15\n\rnamespace_key\x18\x0c \x01(\t\x12\x14\n\x0csegment_keys\x18\r \x03(\t\x1a\x35\n\x13RequestContextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xae\x01\n\tNamespace\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tprotected\x18\x04 \x01(\x08\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"c\n\rNamespaceList\x12$\n\nnamespaces\x18\x01 \x03(\x0b\x32\x10.flipt.Namespace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0btotal_count\x18\x03 \x01(\x05"5\n\x13GetNamespaceRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\treference\x18\x02 \x01(\t"`\n\x14ListNamespaceRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x12\n\x06offset\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\treference\x18\x04 \x01(\t"H\n\x16\x43reateNamespaceRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t"H\n\x16UpdateNamespaceRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t"%\n\x16\x44\x65leteNamespaceRequest\x12\x0b\n\x03key\x18\x01 \x01(\t"\xff\x01\n\x04\x46lag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12 \n\x08variants\x18\x07 \x03(\x0b\x32\x0e.flipt.Variant\x12\x15\n\rnamespace_key\x18\x08 \x01(\t\x12\x1d\n\x04type\x18\t \x01(\x0e\x32\x0f.flipt.FlagType"T\n\x08\x46lagList\x12\x1a\n\x05\x66lags\x18\x01 \x03(\x0b\x32\x0b.flipt.Flag\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0btotal_count\x18\x03 \x01(\x05"G\n\x0eGetFlagRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t"r\n\x0fListFlagRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x12\n\x06offset\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x15\n\rnamespace_key\x18\x04 \x01(\t\x12\x11\n\treference\x18\x05 \x01(\t"\x8a\x01\n\x11\x43reateFlagRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x15\n\rnamespace_key\x18\x05 \x01(\t\x12\x1d\n\x04type\x18\x06 \x01(\x0e\x32\x0f.flipt.FlagType"k\n\x11UpdateFlagRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x15\n\rnamespace_key\x18\x05 \x01(\t"7\n\x11\x44\x65leteFlagRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t"\xe2\x01\n\x07Variant\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nattachment\x18\x08 \x01(\t\x12\x15\n\rnamespace_key\x18\t \x01(\t"\x83\x01\n\x14\x43reateVariantRequest\x12\x10\n\x08\x66lag_key\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\nattachment\x18\x05 \x01(\t\x12\x15\n\rnamespace_key\x18\x06 \x01(\t"\x8f\x01\n\x14UpdateVariantRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x12\n\nattachment\x18\x06 \x01(\t\x12\x15\n\rnamespace_key\x18\x07 \x01(\t"K\n\x14\x44\x65leteVariantRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x15\n\rnamespace_key\x18\x03 \x01(\t"\xfe\x01\n\x07Segment\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x0b\x63onstraints\x18\x06 \x03(\x0b\x32\x11.flipt.Constraint\x12$\n\nmatch_type\x18\x07 \x01(\x0e\x32\x10.flipt.MatchType\x12\x15\n\rnamespace_key\x18\x08 \x01(\t"]\n\x0bSegmentList\x12 \n\x08segments\x18\x01 \x03(\x0b\x32\x0e.flipt.Segment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0btotal_count\x18\x03 \x01(\x05"J\n\x11GetSegmentRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t"u\n\x12ListSegmentRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x12\n\x06offset\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x15\n\rnamespace_key\x18\x04 \x01(\t\x12\x11\n\treference\x18\x05 \x01(\t"\x83\x01\n\x14\x43reateSegmentRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12$\n\nmatch_type\x18\x04 \x01(\x0e\x32\x10.flipt.MatchType\x12\x15\n\rnamespace_key\x18\x05 \x01(\t"\x83\x01\n\x14UpdateSegmentRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12$\n\nmatch_type\x18\x04 \x01(\x0e\x32\x10.flipt.MatchType\x12\x15\n\rnamespace_key\x18\x05 \x01(\t":\n\x14\x44\x65leteSegmentRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t"\x91\x02\n\nConstraint\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bsegment_key\x18\x02 \x01(\t\x12#\n\x04type\x18\x03 \x01(\x0e\x32\x15.flipt.ComparisonType\x12\x10\n\x08property\x18\x04 \x01(\t\x12\x10\n\x08operator\x18\x05 \x01(\t\x12\r\n\x05value\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rnamespace_key\x18\t \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\n \x01(\t"\xb2\x01\n\x17\x43reateConstraintRequest\x12\x13\n\x0bsegment_key\x18\x01 \x01(\t\x12#\n\x04type\x18\x02 \x01(\x0e\x32\x15.flipt.ComparisonType\x12\x10\n\x08property\x18\x03 \x01(\t\x12\x10\n\x08operator\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\t\x12\x15\n\rnamespace_key\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t"\xbe\x01\n\x17UpdateConstraintRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bsegment_key\x18\x02 \x01(\t\x12#\n\x04type\x18\x03 \x01(\x0e\x32\x15.flipt.ComparisonType\x12\x10\n\x08property\x18\x04 \x01(\t\x12\x10\n\x08operator\x18\x05 \x01(\t\x12\r\n\x05value\x18\x06 \x01(\t\x12\x15\n\rnamespace_key\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t"Q\n\x17\x44\x65leteConstraintRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bsegment_key\x18\x02 \x01(\t\x12\x15\n\rnamespace_key\x18\x03 \x01(\t"\xc3\x02\n\x07Rollout\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x03 \x01(\t\x12 \n\x04type\x18\x04 \x01(\x0e\x32\x12.flipt.RolloutType\x12\x0c\n\x04rank\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x07segment\x18\x14 \x01(\x0b\x32\x15.flipt.RolloutSegmentH\x00\x12,\n\tthreshold\x18\x15 \x01(\x0b\x32\x17.flipt.RolloutThresholdH\x00\x42\x06\n\x04rule"\x80\x01\n\x0eRolloutSegment\x12\x17\n\x0bsegment_key\x18\x01 \x01(\tB\x02\x18\x01\x12\r\n\x05value\x18\x02 \x01(\x08\x12\x14\n\x0csegment_keys\x18\x03 \x03(\t\x12\x30\n\x10segment_operator\x18\x04 \x01(\x0e\x32\x16.flipt.SegmentOperator"5\n\x10RolloutThreshold\x12\x12\n\npercentage\x18\x01 \x01(\x02\x12\r\n\x05value\x18\x02 \x01(\x08"Z\n\x0bRolloutList\x12\x1d\n\x05rules\x18\x01 \x03(\x0b\x32\x0e.flipt.Rollout\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0btotal_count\x18\x03 \x01(\x05"s\n\x12ListRolloutRequest\x12\x15\n\rnamespace_key\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\treference\x18\x05 \x01(\t"[\n\x11GetRolloutRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x03 \x01(\t\x12\x11\n\treference\x18\x04 \x01(\t"\xc2\x01\n\x14\x43reateRolloutRequest\x12\x15\n\rnamespace_key\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x0c\n\x04rank\x18\x03 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12(\n\x07segment\x18\x14 \x01(\x0b\x32\x15.flipt.RolloutSegmentH\x00\x12,\n\tthreshold\x18\x15 \x01(\x0b\x32\x17.flipt.RolloutThresholdH\x00\x42\x06\n\x04rule"\xc0\x01\n\x14UpdateRolloutRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12(\n\x07segment\x18\x14 \x01(\x0b\x32\x15.flipt.RolloutSegmentH\x00\x12,\n\tthreshold\x18\x15 \x01(\x0b\x32\x17.flipt.RolloutThresholdH\x00\x42\x06\n\x04rule"K\n\x14\x44\x65leteRolloutRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x03 \x01(\t"T\n\x14OrderRolloutsRequest\x12\x10\n\x08\x66lag_key\x18\x01 \x01(\t\x12\x15\n\rnamespace_key\x18\x02 \x01(\t\x12\x13\n\x0brollout_ids\x18\x03 \x03(\t"\xb2\x02\n\x04Rule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x13\n\x0bsegment_key\x18\x03 \x01(\t\x12*\n\rdistributions\x18\x04 \x03(\x0b\x32\x13.flipt.Distribution\x12\x0c\n\x04rank\x18\x05 \x01(\x05\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rnamespace_key\x18\x08 \x01(\t\x12\x14\n\x0csegment_keys\x18\t \x03(\t\x12\x30\n\x10segment_operator\x18\n \x01(\x0e\x32\x16.flipt.SegmentOperator"T\n\x08RuleList\x12\x1a\n\x05rules\x18\x01 \x03(\x0b\x32\x0b.flipt.Rule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0btotal_count\x18\x03 \x01(\x05"\x84\x01\n\x0fListRuleRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x12\n\x06offset\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x10\n\x08\x66lag_key\x18\x03 \x01(\t\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x15\n\rnamespace_key\x18\x05 \x01(\t\x12\x11\n\treference\x18\x06 \x01(\t"X\n\x0eGetRuleRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x15\n\rnamespace_key\x18\x03 \x01(\t\x12\x11\n\treference\x18\x04 \x01(\t"\xab\x01\n\x11\x43reateRuleRequest\x12\x10\n\x08\x66lag_key\x18\x01 \x01(\t\x12\x17\n\x0bsegment_key\x18\x02 \x01(\tB\x02\x18\x01\x12\x0c\n\x04rank\x18\x03 \x01(\x05\x12\x15\n\rnamespace_key\x18\x04 \x01(\t\x12\x14\n\x0csegment_keys\x18\x05 \x03(\t\x12\x30\n\x10segment_operator\x18\x06 \x01(\x0e\x32\x16.flipt.SegmentOperator"\xa9\x01\n\x11UpdateRuleRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x17\n\x0bsegment_key\x18\x03 \x01(\tB\x02\x18\x01\x12\x15\n\rnamespace_key\x18\x04 \x01(\t\x12\x14\n\x0csegment_keys\x18\x05 \x03(\t\x12\x30\n\x10segment_operator\x18\x06 \x01(\x0e\x32\x16.flipt.SegmentOperator"H\n\x11\x44\x65leteRuleRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x15\n\rnamespace_key\x18\x03 \x01(\t"N\n\x11OrderRulesRequest\x12\x10\n\x08\x66lag_key\x18\x01 \x01(\t\x12\x10\n\x08rule_ids\x18\x02 \x03(\t\x12\x15\n\rnamespace_key\x18\x03 \x01(\t"\xb0\x01\n\x0c\x44istribution\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07rule_id\x18\x02 \x01(\t\x12\x12\n\nvariant_id\x18\x03 \x01(\t\x12\x0f\n\x07rollout\x18\x04 \x01(\x02\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"z\n\x19\x43reateDistributionRequest\x12\x10\n\x08\x66lag_key\x18\x01 \x01(\t\x12\x0f\n\x07rule_id\x18\x02 \x01(\t\x12\x12\n\nvariant_id\x18\x03 \x01(\t\x12\x0f\n\x07rollout\x18\x04 \x01(\x02\x12\x15\n\rnamespace_key\x18\x05 \x01(\t"\x86\x01\n\x19UpdateDistributionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x0f\n\x07rule_id\x18\x03 \x01(\t\x12\x12\n\nvariant_id\x18\x04 \x01(\t\x12\x0f\n\x07rollout\x18\x05 \x01(\x02\x12\x15\n\rnamespace_key\x18\x06 \x01(\t"u\n\x19\x44\x65leteDistributionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x66lag_key\x18\x02 \x01(\t\x12\x0f\n\x07rule_id\x18\x03 \x01(\t\x12\x12\n\nvariant_id\x18\x04 \x01(\t\x12\x15\n\rnamespace_key\x18\x05 \x01(\t*\xb6\x01\n\x10\x45valuationReason\x12\x1d\n\x19UNKNOWN_EVALUATION_REASON\x10\x00\x12#\n\x1f\x46LAG_DISABLED_EVALUATION_REASON\x10\x01\x12$\n FLAG_NOT_FOUND_EVALUATION_REASON\x10\x02\x12\x1b\n\x17MATCH_EVALUATION_REASON\x10\x03\x12\x1b\n\x17\x45RROR_EVALUATION_REASON\x10\x04*8\n\x08\x46lagType\x12\x15\n\x11VARIANT_FLAG_TYPE\x10\x00\x12\x15\n\x11\x42OOLEAN_FLAG_TYPE\x10\x01*3\n\tMatchType\x12\x12\n\x0e\x41LL_MATCH_TYPE\x10\x00\x12\x12\n\x0e\x41NY_MATCH_TYPE\x10\x01*\xbf\x01\n\x0e\x43omparisonType\x12\x1b\n\x17UNKNOWN_COMPARISON_TYPE\x10\x00\x12\x1a\n\x16STRING_COMPARISON_TYPE\x10\x01\x12\x1a\n\x16NUMBER_COMPARISON_TYPE\x10\x02\x12\x1b\n\x17\x42OOLEAN_COMPARISON_TYPE\x10\x03\x12\x1c\n\x18\x44\x41TETIME_COMPARISON_TYPE\x10\x04\x12\x1d\n\x19\x45NTITY_ID_COMPARISON_TYPE\x10\x05*]\n\x0bRolloutType\x12\x18\n\x14UNKNOWN_ROLLOUT_TYPE\x10\x00\x12\x18\n\x14SEGMENT_ROLLOUT_TYPE\x10\x01\x12\x1a\n\x16THRESHOLD_ROLLOUT_TYPE\x10\x02*D\n\x0fSegmentOperator\x12\x17\n\x13OR_SEGMENT_OPERATOR\x10\x00\x12\x18\n\x14\x41ND_SEGMENT_OPERATOR\x10\x01\x32\xdb\x13\n\x05\x46lipt\x12\x44\n\x08\x45valuate\x12\x18.flipt.EvaluationRequest\x1a\x19.flipt.EvaluationResponse"\x03\x88\x02\x01\x12S\n\rBatchEvaluate\x12\x1d.flipt.BatchEvaluationRequest\x1a\x1e.flipt.BatchEvaluationResponse"\x03\x88\x02\x01\x12>\n\x0cGetNamespace\x12\x1a.flipt.GetNamespaceRequest\x1a\x10.flipt.Namespace"\x00\x12\x45\n\x0eListNamespaces\x12\x1b.flipt.ListNamespaceRequest\x1a\x14.flipt.NamespaceList"\x00\x12\x44\n\x0f\x43reateNamespace\x12\x1d.flipt.CreateNamespaceRequest\x1a\x10.flipt.Namespace"\x00\x12\x44\n\x0fUpdateNamespace\x12\x1d.flipt.UpdateNamespaceRequest\x1a\x10.flipt.Namespace"\x00\x12J\n\x0f\x44\x65leteNamespace\x12\x1d.flipt.DeleteNamespaceRequest\x1a\x16.google.protobuf.Empty"\x00\x12/\n\x07GetFlag\x12\x15.flipt.GetFlagRequest\x1a\x0b.flipt.Flag"\x00\x12\x36\n\tListFlags\x12\x16.flipt.ListFlagRequest\x1a\x0f.flipt.FlagList"\x00\x12\x35\n\nCreateFlag\x12\x18.flipt.CreateFlagRequest\x1a\x0b.flipt.Flag"\x00\x12\x35\n\nUpdateFlag\x12\x18.flipt.UpdateFlagRequest\x1a\x0b.flipt.Flag"\x00\x12@\n\nDeleteFlag\x12\x18.flipt.DeleteFlagRequest\x1a\x16.google.protobuf.Empty"\x00\x12>\n\rCreateVariant\x12\x1b.flipt.CreateVariantRequest\x1a\x0e.flipt.Variant"\x00\x12>\n\rUpdateVariant\x12\x1b.flipt.UpdateVariantRequest\x1a\x0e.flipt.Variant"\x00\x12\x46\n\rDeleteVariant\x12\x1b.flipt.DeleteVariantRequest\x1a\x16.google.protobuf.Empty"\x00\x12/\n\x07GetRule\x12\x15.flipt.GetRuleRequest\x1a\x0b.flipt.Rule"\x00\x12\x36\n\tListRules\x12\x16.flipt.ListRuleRequest\x1a\x0f.flipt.RuleList"\x00\x12\x35\n\nCreateRule\x12\x18.flipt.CreateRuleRequest\x1a\x0b.flipt.Rule"\x00\x12\x35\n\nUpdateRule\x12\x18.flipt.UpdateRuleRequest\x1a\x0b.flipt.Rule"\x00\x12@\n\nOrderRules\x12\x18.flipt.OrderRulesRequest\x1a\x16.google.protobuf.Empty"\x00\x12@\n\nDeleteRule\x12\x18.flipt.DeleteRuleRequest\x1a\x16.google.protobuf.Empty"\x00\x12\x38\n\nGetRollout\x12\x18.flipt.GetRolloutRequest\x1a\x0e.flipt.Rollout"\x00\x12?\n\x0cListRollouts\x12\x19.flipt.ListRolloutRequest\x1a\x12.flipt.RolloutList"\x00\x12>\n\rCreateRollout\x12\x1b.flipt.CreateRolloutRequest\x1a\x0e.flipt.Rollout"\x00\x12>\n\rUpdateRollout\x12\x1b.flipt.UpdateRolloutRequest\x1a\x0e.flipt.Rollout"\x00\x12\x46\n\rDeleteRollout\x12\x1b.flipt.DeleteRolloutRequest\x1a\x16.google.protobuf.Empty"\x00\x12\x46\n\rOrderRollouts\x12\x1b.flipt.OrderRolloutsRequest\x1a\x16.google.protobuf.Empty"\x00\x12M\n\x12\x43reateDistribution\x12 .flipt.CreateDistributionRequest\x1a\x13.flipt.Distribution"\x00\x12M\n\x12UpdateDistribution\x12 .flipt.UpdateDistributionRequest\x1a\x13.flipt.Distribution"\x00\x12P\n\x12\x44\x65leteDistribution\x12 .flipt.DeleteDistributionRequest\x1a\x16.google.protobuf.Empty"\x00\x12\x38\n\nGetSegment\x12\x18.flipt.GetSegmentRequest\x1a\x0e.flipt.Segment"\x00\x12?\n\x0cListSegments\x12\x19.flipt.ListSegmentRequest\x1a\x12.flipt.SegmentList"\x00\x12>\n\rCreateSegment\x12\x1b.flipt.CreateSegmentRequest\x1a\x0e.flipt.Segment"\x00\x12>\n\rUpdateSegment\x12\x1b.flipt.UpdateSegmentRequest\x1a\x0e.flipt.Segment"\x00\x12\x46\n\rDeleteSegment\x12\x1b.flipt.DeleteSegmentRequest\x1a\x16.google.protobuf.Empty"\x00\x12G\n\x10\x43reateConstraint\x12\x1e.flipt.CreateConstraintRequest\x1a\x11.flipt.Constraint"\x00\x12G\n\x10UpdateConstraint\x12\x1e.flipt.UpdateConstraintRequest\x1a\x11.flipt.Constraint"\x00\x12L\n\x10\x44\x65leteConstraint\x12\x1e.flipt.DeleteConstraintRequest\x1a\x16.google.protobuf.Empty"\x00\x42\x1dZ\x1bgo.flipt.io/flipt/rpc/fliptb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "unstract.flags.src.unstract.flags.protos.flipt_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = b"Z\033go.flipt.io/flipt/rpc/flipt"
    _globals["_EVALUATIONREQUEST_CONTEXTENTRY"]._options = None
    _globals["_EVALUATIONREQUEST_CONTEXTENTRY"]._serialized_options = b"8\001"
    _globals["_EVALUATIONRESPONSE_REQUESTCONTEXTENTRY"]._options = None
    _globals["_EVALUATIONRESPONSE_REQUESTCONTEXTENTRY"]._serialized_options = b"8\001"
    _globals["_EVALUATIONRESPONSE"].fields_by_name["segment_key"]._options = None
    _globals["_EVALUATIONRESPONSE"].fields_by_name[
        "segment_key"
    ]._serialized_options = b"\030\001"
    _globals["_LISTNAMESPACEREQUEST"].fields_by_name["offset"]._options = None
    _globals["_LISTNAMESPACEREQUEST"].fields_by_name[
        "offset"
    ]._serialized_options = b"\030\001"
    _globals["_LISTFLAGREQUEST"].fields_by_name["offset"]._options = None
    _globals["_LISTFLAGREQUEST"].fields_by_name[
        "offset"
    ]._serialized_options = b"\030\001"
    _globals["_LISTSEGMENTREQUEST"].fields_by_name["offset"]._options = None
    _globals["_LISTSEGMENTREQUEST"].fields_by_name[
        "offset"
    ]._serialized_options = b"\030\001"
    _globals["_ROLLOUTSEGMENT"].fields_by_name["segment_key"]._options = None
    _globals["_ROLLOUTSEGMENT"].fields_by_name[
        "segment_key"
    ]._serialized_options = b"\030\001"
    _globals["_LISTRULEREQUEST"].fields_by_name["offset"]._options = None
    _globals["_LISTRULEREQUEST"].fields_by_name[
        "offset"
    ]._serialized_options = b"\030\001"
    _globals["_CREATERULEREQUEST"].fields_by_name["segment_key"]._options = None
    _globals["_CREATERULEREQUEST"].fields_by_name[
        "segment_key"
    ]._serialized_options = b"\030\001"
    _globals["_UPDATERULEREQUEST"].fields_by_name["segment_key"]._options = None
    _globals["_UPDATERULEREQUEST"].fields_by_name[
        "segment_key"
    ]._serialized_options = b"\030\001"
    _globals["_FLIPT"].methods_by_name["Evaluate"]._options = None
    _globals["_FLIPT"].methods_by_name["Evaluate"]._serialized_options = b"\210\002\001"
    _globals["_FLIPT"].methods_by_name["BatchEvaluate"]._options = None
    _globals["_FLIPT"].methods_by_name[
        "BatchEvaluate"
    ]._serialized_options = b"\210\002\001"
    _globals["_EVALUATIONREASON"]._serialized_start = 7747
    _globals["_EVALUATIONREASON"]._serialized_end = 7929
    _globals["_FLAGTYPE"]._serialized_start = 7931
    _globals["_FLAGTYPE"]._serialized_end = 7987
    _globals["_MATCHTYPE"]._serialized_start = 7989
    _globals["_MATCHTYPE"]._serialized_end = 8040
    _globals["_COMPARISONTYPE"]._serialized_start = 8043
    _globals["_COMPARISONTYPE"]._serialized_end = 8234
    _globals["_ROLLOUTTYPE"]._serialized_start = 8236
    _globals["_ROLLOUTTYPE"]._serialized_end = 8329
    _globals["_SEGMENTOPERATOR"]._serialized_start = 8331
    _globals["_SEGMENTOPERATOR"]._serialized_end = 8399
    _globals["_EVALUATIONREQUEST"]._serialized_start = 126
    _globals["_EVALUATIONREQUEST"]._serialized_end = 329
    _globals["_EVALUATIONREQUEST_CONTEXTENTRY"]._serialized_start = 283
    _globals["_EVALUATIONREQUEST_CONTEXTENTRY"]._serialized_end = 329
    _globals["_BATCHEVALUATIONREQUEST"]._serialized_start = 332
    _globals["_BATCHEVALUATIONREQUEST"]._serialized_end = 470
    _globals["_BATCHEVALUATIONRESPONSE"]._serialized_start = 472
    _globals["_BATCHEVALUATIONRESPONSE"]._serialized_end = 596
    _globals["_EVALUATIONRESPONSE"]._serialized_start = 599
    _globals["_EVALUATIONRESPONSE"]._serialized_end = 1044
    _globals["_EVALUATIONRESPONSE_REQUESTCONTEXTENTRY"]._serialized_start = 991
    _globals["_EVALUATIONRESPONSE_REQUESTCONTEXTENTRY"]._serialized_end = 1044
    _globals["_NAMESPACE"]._serialized_start = 1047
    _globals["_NAMESPACE"]._serialized_end = 1221
    _globals["_NAMESPACELIST"]._serialized_start = 1223
    _globals["_NAMESPACELIST"]._serialized_end = 1322
    _globals["_GETNAMESPACEREQUEST"]._serialized_start = 1324
    _globals["_GETNAMESPACEREQUEST"]._serialized_end = 1377
    _globals["_LISTNAMESPACEREQUEST"]._serialized_start = 1379
    _globals["_LISTNAMESPACEREQUEST"]._serialized_end = 1475
    _globals["_CREATENAMESPACEREQUEST"]._serialized_start = 1477
    _globals["_CREATENAMESPACEREQUEST"]._serialized_end = 1549
    _globals["_UPDATENAMESPACEREQUEST"]._serialized_start = 1551
    _globals["_UPDATENAMESPACEREQUEST"]._serialized_end = 1623
    _globals["_DELETENAMESPACEREQUEST"]._serialized_start = 1625
    _globals["_DELETENAMESPACEREQUEST"]._serialized_end = 1662
    _globals["_FLAG"]._serialized_start = 1665
    _globals["_FLAG"]._serialized_end = 1920
    _globals["_FLAGLIST"]._serialized_start = 1922
    _globals["_FLAGLIST"]._serialized_end = 2006
    _globals["_GETFLAGREQUEST"]._serialized_start = 2008
    _globals["_GETFLAGREQUEST"]._serialized_end = 2079
    _globals["_LISTFLAGREQUEST"]._serialized_start = 2081
    _globals["_LISTFLAGREQUEST"]._serialized_end = 2195
    _globals["_CREATEFLAGREQUEST"]._serialized_start = 2198
    _globals["_CREATEFLAGREQUEST"]._serialized_end = 2336
    _globals["_UPDATEFLAGREQUEST"]._serialized_start = 2338
    _globals["_UPDATEFLAGREQUEST"]._serialized_end = 2445
    _globals["_DELETEFLAGREQUEST"]._serialized_start = 2447
    _globals["_DELETEFLAGREQUEST"]._serialized_end = 2502
    _globals["_VARIANT"]._serialized_start = 2505
    _globals["_VARIANT"]._serialized_end = 2731
    _globals["_CREATEVARIANTREQUEST"]._serialized_start = 2734
    _globals["_CREATEVARIANTREQUEST"]._serialized_end = 2865
    _globals["_UPDATEVARIANTREQUEST"]._serialized_start = 2868
    _globals["_UPDATEVARIANTREQUEST"]._serialized_end = 3011
    _globals["_DELETEVARIANTREQUEST"]._serialized_start = 3013
    _globals["_DELETEVARIANTREQUEST"]._serialized_end = 3088
    _globals["_SEGMENT"]._serialized_start = 3091
    _globals["_SEGMENT"]._serialized_end = 3345
    _globals["_SEGMENTLIST"]._serialized_start = 3347
    _globals["_SEGMENTLIST"]._serialized_end = 3440
    _globals["_GETSEGMENTREQUEST"]._serialized_start = 3442
    _globals["_GETSEGMENTREQUEST"]._serialized_end = 3516
    _globals["_LISTSEGMENTREQUEST"]._serialized_start = 3518
    _globals["_LISTSEGMENTREQUEST"]._serialized_end = 3635
    _globals["_CREATESEGMENTREQUEST"]._serialized_start = 3638
    _globals["_CREATESEGMENTREQUEST"]._serialized_end = 3769
    _globals["_UPDATESEGMENTREQUEST"]._serialized_start = 3772
    _globals["_UPDATESEGMENTREQUEST"]._serialized_end = 3903
    _globals["_DELETESEGMENTREQUEST"]._serialized_start = 3905
    _globals["_DELETESEGMENTREQUEST"]._serialized_end = 3963
    _globals["_CONSTRAINT"]._serialized_start = 3966
    _globals["_CONSTRAINT"]._serialized_end = 4239
    _globals["_CREATECONSTRAINTREQUEST"]._serialized_start = 4242
    _globals["_CREATECONSTRAINTREQUEST"]._serialized_end = 4420
    _globals["_UPDATECONSTRAINTREQUEST"]._serialized_start = 4423
    _globals["_UPDATECONSTRAINTREQUEST"]._serialized_end = 4613
    _globals["_DELETECONSTRAINTREQUEST"]._serialized_start = 4615
    _globals["_DELETECONSTRAINTREQUEST"]._serialized_end = 4696
    _globals["_ROLLOUT"]._serialized_start = 4699
    _globals["_ROLLOUT"]._serialized_end = 5022
    _globals["_ROLLOUTSEGMENT"]._serialized_start = 5025
    _globals["_ROLLOUTSEGMENT"]._serialized_end = 5153
    _globals["_ROLLOUTTHRESHOLD"]._serialized_start = 5155
    _globals["_ROLLOUTTHRESHOLD"]._serialized_end = 5208
    _globals["_ROLLOUTLIST"]._serialized_start = 5210
    _globals["_ROLLOUTLIST"]._serialized_end = 5300
    _globals["_LISTROLLOUTREQUEST"]._serialized_start = 5302
    _globals["_LISTROLLOUTREQUEST"]._serialized_end = 5417
    _globals["_GETROLLOUTREQUEST"]._serialized_start = 5419
    _globals["_GETROLLOUTREQUEST"]._serialized_end = 5510
    _globals["_CREATEROLLOUTREQUEST"]._serialized_start = 5513
    _globals["_CREATEROLLOUTREQUEST"]._serialized_end = 5707
    _globals["_UPDATEROLLOUTREQUEST"]._serialized_start = 5710
    _globals["_UPDATEROLLOUTREQUEST"]._serialized_end = 5902
    _globals["_DELETEROLLOUTREQUEST"]._serialized_start = 5904
    _globals["_DELETEROLLOUTREQUEST"]._serialized_end = 5979
    _globals["_ORDERROLLOUTSREQUEST"]._serialized_start = 5981
    _globals["_ORDERROLLOUTSREQUEST"]._serialized_end = 6065
    _globals["_RULE"]._serialized_start = 6068
    _globals["_RULE"]._serialized_end = 6374
    _globals["_RULELIST"]._serialized_start = 6376
    _globals["_RULELIST"]._serialized_end = 6460
    _globals["_LISTRULEREQUEST"]._serialized_start = 6463
    _globals["_LISTRULEREQUEST"]._serialized_end = 6595
    _globals["_GETRULEREQUEST"]._serialized_start = 6597
    _globals["_GETRULEREQUEST"]._serialized_end = 6685
    _globals["_CREATERULEREQUEST"]._serialized_start = 6688
    _globals["_CREATERULEREQUEST"]._serialized_end = 6859
    _globals["_UPDATERULEREQUEST"]._serialized_start = 6862
    _globals["_UPDATERULEREQUEST"]._serialized_end = 7031
    _globals["_DELETERULEREQUEST"]._serialized_start = 7033
    _globals["_DELETERULEREQUEST"]._serialized_end = 7105
    _globals["_ORDERRULESREQUEST"]._serialized_start = 7107
    _globals["_ORDERRULESREQUEST"]._serialized_end = 7185
    _globals["_DISTRIBUTION"]._serialized_start = 7188
    _globals["_DISTRIBUTION"]._serialized_end = 7364
    _globals["_CREATEDISTRIBUTIONREQUEST"]._serialized_start = 7366
    _globals["_CREATEDISTRIBUTIONREQUEST"]._serialized_end = 7488
    _globals["_UPDATEDISTRIBUTIONREQUEST"]._serialized_start = 7491
    _globals["_UPDATEDISTRIBUTIONREQUEST"]._serialized_end = 7625
    _globals["_DELETEDISTRIBUTIONREQUEST"]._serialized_start = 7627
    _globals["_DELETEDISTRIBUTIONREQUEST"]._serialized_end = 7744
    _globals["_FLIPT"]._serialized_start = 8402
    _globals["_FLIPT"]._serialized_end = 10925
# @@protoc_insertion_point(module_scope)