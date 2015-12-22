#!/usr/bin/env python

from distutils.core import setup

setup(name='anifs',
      version='0.1',
      packages=['anifs'],
      scripts=['bin/anifs'],
      install_requires=[
          "adba",
      ],
     )
