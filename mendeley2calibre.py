#!/usr/bin/env python3

import argparse
from mendeley import Mendeley
from mendeley.session import MendeleySession
import logging
from calibre2mendeley.clogger import setup_logging

# setup logging
logger = logging.getLogger(__file__)
setup_logging(logger)

# Parse cmdline args

# if password is not in the cmdline args ask for it.

# Read books from mendeley

# Get them to a list

# For each mendeley book convert it to calibre
# Add the book's PDF
# Add the book's metadata


