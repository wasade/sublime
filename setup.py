#!/usr/bin/env python

__version__ = "0.1.0"

from setuptools import setup


classes = """
    Development Status :: 4 - Beta
    License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
    Topic :: Software Development :: Libraries :: Python Modules
    Topic :: Scientific/Engineering
    Programming Language :: Python
    Programming Language :: Python :: 2.7
    Operating System :: POSIX :: Linux
"""

long_description = """Sublime: easy job submission"""

classifiers = [s.strip() for s in classes.split('\n') if s]

setup(name='sublime',
      version=__version__,
      long_description=long_description,
      license="CC0",
      description='Submission ninja',
      author="Daniel McDonald",
      author_email="mcdonadt@colorado.edu",
      url='http://github.com/wasade/sublime',
      install_requires=['click >= 3.3, < 4.0'],
      classifiers=classifiers,
      scripts=['sub']
      )
