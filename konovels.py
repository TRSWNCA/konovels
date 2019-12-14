#!/usr/bin/env python
"""
Launcher
"""

import os
import sys

_srcdir = '%s/' % os.path.dirname(os.path.realpath(__file__))
_filepath = os.path.dirname(sys.argv[0])
sys.path.insert(1, os.path.join(_filepath, _srcdir))

if sys.version_info[0] == 3:
    import core
    if __name__ == '__main__':
        core.main()
else:  # Python 2
    print('Python3 Only')
