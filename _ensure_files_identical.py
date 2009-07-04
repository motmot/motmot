#!/usr/bin/env python

"""Periodically run this script to ensure that files that should be
identical haven't diverged. This would be a non-issue if all operating
systems, version control systems, and editors supported symlinks in a
sane way. But they don't.

"""
import os, sys

same=[('pycamiface/src/c_lib.pxd', 'imops/src/c_lib.pxd'),
      ('pycamiface/src/c_lib.pxd', 'FastImage/src/c_lib.pxd'),
      ('pycamiface/src/c_lib.pxd', 'realtime_image_analysis/src/c_lib.pxd'),

      ('pycamiface/src/c_python.pxd', 'imops/src/c_python.pxd'),
      ('pycamiface/src/c_python.pxd', 'FastImage/src/c_python.pxd'),
      ('pycamiface/src/c_python.pxd', 'realtime_image_analysis/src/c_python.pxd'),

      ('pycamiface/src/ads_wrap_system.h','imops/src/ads_wrap_system.h'),
      ('pycamiface/src/ads_wrap_system.h','realtime_image_analysis/src/ads_wrap_system.h'),
      ('pycamiface/src/ads_wrap_system.h','FastImage/src/ads_wrap_system.h'),

      ('FastImage/src/FastImage.pxd','realtime_image_analysis/src/motmot.FastImage.FastImage.pxd'),
      ('FastImage/src/fic.c','realtime_image_analysis/src/fic.c'),
      ('FastImage/src/fic.h','realtime_image_analysis/src/fic.h'),
      ('FastImage/src/fic.pxd','realtime_image_analysis/src/fic.pxd'),
      ('FastImage/src/fi_fw.h','realtime_image_analysis/src/fi_fw.h'),
      ('FastImage/src/fw.pxd','realtime_image_analysis/src/fw.pxd'),
      ('FastImage/src/FastImage.pxd','realtime_image_analysis/src/motmot.FastImage.FastImage.pxd'),
      ]

def my_compare(_from, _to):
    # Copy the file data from _from to _to
    s = open(_from).read()
    if not os.path.exists(_to):
        return False
    s2 = open(_to).read()
    if s != s2:
        return False
    return True

def main():
    any_different = False
    for (f1,f2) in same:
        f1 = os.path.normpath(f1)
        f2 = os.path.normpath(f2)
        if not my_compare(f1,f2):
            any_different = True
            print >> sys.stderr,f1,'!=',f2
    if any_different:
        sys.exit(1)

if __name__=='__main__':
    main()
