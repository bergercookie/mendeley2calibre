# mendeley2calibre

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

**Current project is a work in progress. Do not expect it to work.**

Conversion tool for migrating a Mendeley DB to calibre. mendeley2calibre parses
the local mendeley sqlite3 db and imports the files + metadata found there to
the corresponding Calibre db. Parsing of the mendeley db is carried out using
the [bergercookie/pymendeley](https://github.com/bergercookie/pymendeley)
package.

## Setup

Install the package locally using pip:

    ```sh
    pip3 install --user --upgrade git+https://github.com/bergercookie/pymendeley
    ```

## Usage

Migrate the mendeley db using the mendeley2calibre script

    ```sh
    mendeley2calibre --help
    mendeley2calibre  # Run the script
    ```

## Offline documentation

A developer can also generate the `Sphinx` documentation for `mendeley2calibre` offline:

- Install the related tools:

    ```sh
    apt-get install sphinx sphinx_rtd_theme
    ```
- To update the documentation run `make html` inside the `docs` directory.
    Open the build/html/index.html file to view the results

        #!sh
        firefox docs/build/html/index.html


## Roadmap

- [X] Come up with a working version
- [X] Use mypy for static checking
- [X] Generate Sphinx documentation
- [X] Authors, Document Tags Support
- [ ] optional argument for specifying the mendeley path as well
- [ ] Unittests
- [ ] basic CI script that runs unittests, mypy
- [ ] Code quality badge?
- [ ] Github badges (pymendeley, mendeley2calibre)
  - [ ] Code quality
  - [ ] CI
  - [ ] Version
  - [ ] Documentation
- [ ] cleanup todos
- [ ] specify a stable commit in the mendeley2calibre setup.py file
- [ ] Peek demo
