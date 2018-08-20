#!/usr/bin/env python
# Filename: __version__.py
# pylint: disable=C0103
"""
Pep 386 compliant version info.

    (major, minor, micro, alpha/beta/rc/final, #)
    (1, 1, 2, 'alpha', 0) => "1.1.2.dev"
    (1, 2, 0, 'beta', 2) => "1.2b2"

"""
from __future__ import absolute_import, print_function, division

import subprocess
import os
from os.path import dirname, join, exists

VERSION_INFO = (0, 0, 1, 'final', 0)

__author__ = 'Tamas Gal'


def _get_version(version_info):
    """Return a PEP 386-compliant version number."""
    assert len(version_info) == 5
    assert version_info[3] in ('alpha', 'beta', 'rc', 'final')

    parts = 2 if version_info[2] == 0 else 3
    main = '.'.join(map(str, version_info[:parts]))

    sub = ''
    if version_info[3] == 'alpha' and version_info[4] == 0:
        sub = '.dev'
    elif version_info[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version_info[3]] + str(version_info[4])

    return str(main + sub)


version = _get_version(VERSION_INFO)
