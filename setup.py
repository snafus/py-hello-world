#!/usr/bin/env python

from distutils.core import setup

setup(name='py-hello-world',
      version='0.1.0',
      description='Sample hello world app',
      long_description="""Examplar application to exercise all aspects of packaging, intergration and unit testing, etc.
      Intended to have minimal external use of helper packages.""",
      author='',
      author_email='',
      license='GPL 3',
      classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 2.7'],
      keywords = 'sample exemplar',
      #url='https://www.python.org/sigs/distutils-sig/',
      packages=['py_hello_world'],
      #packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      install_requires=[],
     )


