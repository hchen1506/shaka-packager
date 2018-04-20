# Copyright 2015 Google Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

{
  'variables': {
    'shaka_code': 1,
  },
  'targets': [
    {
      'target_name': 'webvtt',
      'type': '<(component)',
      'sources': [
        'webvtt_media_parser.cc',
        'webvtt_media_parser.h',
      ],
      'dependencies': [
        '../../../base/base.gyp:base',
        '../../base/media_base.gyp:media_base',
      ],
    },
    {
      'target_name': 'webvtt_unittest',
      'type': '<(gtest_target_type)',
      'sources': [
        'webvtt_media_parser_unittest.cc',
      ],
      'dependencies': [
        '../../../testing/gmock.gyp:gmock',
        '../../../testing/gtest.gyp:gtest',
        '../../test/media_test.gyp:media_test_support',
        'webvtt',
      ]
    },
  ],
}
