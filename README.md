# mendeley2calibre
<p align="center">
  <a href="https://travis-ci.org/bergercookie/mendeley2calibre" alt="Build Status">
  <img src="https://travis-ci.org/bergercookie/mendeley2calibre.svg?branch=master" /></a>

  <a href='http://mendeley2calibre.readthedocs.io/en/latest/?badge=latest'>
  <img src='https://readthedocs.org/projects/mendeley2calibre/badge/?version=latest' alt='Documentation Status' /></a>

  <a href="https://github.com/bergercookie/mendeley2calibre/blob/master/LICENSE" alt="License">
  <img src="https://img.shields.io/pypi/l/Django.svg" /></a>

  <a href="https://www.python.org/" alt="Python">
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" /></a>

</p>


```
                              _        _               ___              _  _  _
                             | |      | |             |__ \            | |(_)| |
  _ __ ___    ___  _ __    __| |  ___ | |  ___  _   _    ) | ___  __ _ | | _ | |__   _ __  ___
 | '_ ` _ \  / _ \| '_ \  / _` | / _ \| | / _ \| | | |  / / / __|/ _` || || || '_ \ | '__|/ _ \
 | | | | | ||  __/| | | || (_| ||  __/| ||  __/| |_| | / /_| (__| (_| || || || |_) || |  |  __/
 |_| |_| |_| \___||_| |_| \__,_| \___||_| \___| \__, ||____|\___|\__,_||_||_||_.__/ |_|   \___|
                                                 __/ |
                                                |___/
```


## Description

Conversion tool for migrating a Mendeley DB to calibre. mendeley2calibre parses
the local mendeley sqlite3 db and imports the files + metadata found there to
the corresponding Calibre db. Parsing of the mendeley db is carried out using
the [bergercookie/pymendeley](https://github.com/bergercookie/pymendeley)
package.

## Setup

Install the package locally using pip:
  ```sh
  pip3 install --user --upgrade git+https://github.com/bergercookie/pymendeley
  pip3 install --user --upgrade git+https://github.com/bergercookie/mendeley2calibre
  ```

## Usage

Migrate the mendeley db using the mendeley2calibre script
  ```sh
  mendeley2calibre --help

  Usage: migrate_to_calibre.py [OPTIONS]

  Options:
    -c, --calibre-lib PATH   Top-level path to the Calibre library  [required]
    -m, --mendeley-lib PATH  Path to the Mendeley sqlite3 DB. If not specified
                             ./migrate_to_calibre.py will try to guess where
                             that is.
    --help                   Show this message and exit.

  ```

## Offline documentation

A developer can also generate the `Sphinx` documentation for `mendeley2calibre` offline:

- Install the related tools:

  ```sh
  apt-get install sphinx sphinx_rtd_theme
  ```
- To update the documentation run `make html` inside the `docs` directory.
    Open the `build/html/index.html` file to view the results

  ```sh
  firefox docs/build/html/index.html
  ```


## Roadmap

- [X] Come up with a working version
- [X] Use mypy for static checking
- [X] Generate Sphinx documentation
- [X] Authors, Document Tags Support
- [X] Optional argument for specifying the mendeley path as well
- [ ] Unittests
  - [ ] pymendeley
  - [ ] calibre2mendeley
- [ ] Basic CI script that runs unittests, flake stats + posting
- [ ] Github badges (pymendeley, mendeley2calibre)
  - [X] pymendeley - pylint badge - https://github.com/mperlet/pybadge
  - [ ] calibre2mendeley - pylint badge - https://github.com/mperlet/pybadge
  - [X] CI
  - [X] Documentation
- [ ] Cleanup Todos
