"""Setup a custom logger that outputs messages in a colored manner and utilizes
the standard logging module.

Relevant Links
##

- `<https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output/>`_
"""

import logging
import sys
import os
try:
    import colorlog
except ImportError:
    pass


def setup_logging(logger_name):
    root = logging.getLogger(logger_name)
    root.setLevel(logging.DEBUG)
    format = '%(name)s: %(asctime)s - %(levelname)-8s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    if 'colorlog' in sys.modules and os.isatty(2):
        cformat = '%(log_color)s' + format
        f = colorlog.ColoredFormatter(cformat, date_format,
                                      log_colors={'DEBUG': 'cyan',
                                                  'INFO': 'green',
                                                  'WARNING': 'bold_yellow',
                                                  'ERROR': 'bold_red',
                                                  'CRITICAL': 'bold_red'})
    else:
        f = logging.Formatter(format, date_format)
    ch = logging.StreamHandler()
    ch.setFormatter(f)
    root.addHandler(ch)

