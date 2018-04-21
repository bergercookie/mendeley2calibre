#!/usr/bin/env python
import os
from setuptools import setup

PKG_NAME = "mendeley2calibre"

author = "Nikos Koukis"
author_email = "nickkouk@gmail.com"


# Utility function to read the README file.
# Used for the long_description.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name=PKG_NAME,
      version='0.1.1',
      description='Conversion tool for migrating a Mendeley DB to calibre',
      long_description=read('README.md'),
      author=author,
      author_email=author_email,
      maintainer=author,
      maintainer_email=author_email,
      license='BSD 3-clause',
      install_requires=(
          "pymendeley",
          "sh",
          "click",
          "colorlog",
      ),
      url='https://github.org/bergercookie/{}'.format(PKG_NAME),
      download_url='https://github.org/bergercookie/{}'.format(PKG_NAME),
      dependency_links=["https://github.com/bergercookie/pymendeley", ],
      scripts=['migrate_to_calibre.py', ],
      packages=[PKG_NAME, ],
      platforms="Linux",
      )

