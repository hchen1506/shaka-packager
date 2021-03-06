DASH
====

Dynamic Adaptive Streaming over HTTP (DASH) is an adaptive bitrate streaming
technique that enables high quality streaming of media content over HTTP.

Shaka Packager supports DASH content packaging. This tutorial covers DASH
packaging of VOD content without encryption. For live content packaging, see
:doc:`live`; for content encryption, see :doc:`drm`.

Synopsis
--------

::

    $ packager {stream_descriptor} [stream_descriptor] ... \
      --mpd_output {manifest output path} \
      [Other DASH options] \
      [Other options, e.g. DRM options, HLS options]

See `DASH options`_ for the available DASH related options.

.. note::

    DASH and HLS options can both be specified to output DASH and HLS manifests
    at the same time. Note that it works only for MP4 outputs.

Examples
--------

The examples below uses the H264 streams created in :doc:`encoding`. It can be
applied to VP9 in the same way.

* on-demand::

    $ packager \
      in=h264_baseline_360p_600.mp4,stream=audio,output=audio.mp4 \
      in=h264_baseline_360p_600.mp4,stream=video,output=h264_360p.mp4 \
      in=h264_main_480p_1000.mp4,stream=video,output=h264_480p.mp4 \
      in=h264_main_720p_3000.mp4,stream=video,output=h264_720p.mp4 \
      in=h264_high_1080p_6000.mp4,stream=video,output=h264_1080p.mp4 \
      --mpd_output h264.mpd

The above packaging command creates five single track fragmented mp4 streams
(4 video, 1 audio) and a manifest, which describes the streams.

* static-live::

    $ packager \
      'in=h264_baseline_360p_600.mp4,stream=audio,init_segment=audio_init.mp4,segment_template=audio_$Number$.m4s' \
      'in=h264_baseline_360p_600.mp4,stream=video,init_segment=h264_360p_init.mp4,segment_template=h264_360p_$Number$.m4s' \
      'in=h264_main_480p_1000.mp4,stream=video,init_segment=h264_480p_init.mp4,segment_template=h264_480p_$Number$.m4s' \
      'in=h264_main_720p_3000.mp4,stream=video,init_segment=h264_720p_init.mp4,segment_template=h264_720p_$Number$.m4s' \
      'in=h264_main_1080p_6000.mp4,stream=video,init_segment=h264_1080p_init.mp4,segment_template=h264_1080p_$Number$.m4s' \
      --generate_static_mpd --mpd_output h264.mpd

The above packaging command creates five groups of segments (each with an init
segment and a series of media segments) for the five streams and a manifest,
which describes the streams.

.. include:: /tutorials/dash_hls_example.rst

.. include:: /options/dash_options.rst

.. include:: /options/segment_template_formatting.rst
