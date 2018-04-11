#!/usr/bin/env python
import os
from setuptools import setup
# from setuptools.command.develop import develop
# from setuptools.command.install import install

PKG_NAME = "mendeley2calibre"


# Utility function to read the README file.
# Used for the long_description.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name=PKG_NAME,
      version='0.1',
      description='Conversion tool for migrating a Mendeley DB to calibre',
      long_description=read('README.md'),
      author='Nikos Koukis',
      author_email='nickkouk@gmail.com',
      maintainer='Nikos Koukis',
      maintainer_email='nickkouk@gmail.com',
      license='BSD 3-clause',
      install_requires=(
          "mendeley",
      ),
      url='https://github.org/bergercookie/calibration_automaton',
      download_url='https://github.org/bergercookie/calibration_automaton',
      scripts=['vmendeley2calibre.py', ],
      platforms="Linux",
      )

