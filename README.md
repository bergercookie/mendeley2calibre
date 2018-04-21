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

## Roadmap

- [X] Come up with a working version
- [X] Use mypy for static checking
- [] Implement basic unittests
