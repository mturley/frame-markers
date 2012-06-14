frame-markers
=============

A tiny tool in python to generate constant-duration timecode markers for video editing.  Useful for synchronizing beats of music to video cuts.

usage
-----

    ./markers.py <framerate> <marker duration in frames> <minutes>

ex.
    ./markers.py 29.97 56 5
will generate 5 minutes of markers 56-frames long each, at 29.97 frames per second.
