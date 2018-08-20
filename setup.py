#!/usr/bin/env python
# Filename: setup.py
"""
Harmonia setup script.

"""

from setuptools import setup

from harmonia import version    # noqa

with open('requirements.txt') as fobj:
    requirements = [l.strip() for l in fobj.readlines()]

setup(
    name='harmonia',
    version=version,
    url='http://git.km3net.de/tgal/harmonia/',
    description='A dispatcher for online processing and reconstruction.',
    author='Tamas Gal',
    author_email='tgal@km3net.de',
    packages=['harmonia'],
    include_package_data=True,
    platforms='any',
    setup_requires=[],
    install_requires=requirements,
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'harmonia=harmonia.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
    ],
)

__author__ = 'Tamas Gal'
