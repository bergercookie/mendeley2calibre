#!/usr/bin/env python3

import argparse
import logging
from mendeley2calibre.clogger import setup_logging

# setup logging
logger = logging.getLogger(__file__)
setup_logging(logger)

logger.info("Initialising conversion procedure: Mendeley -> Calibre...")

# Parse cmdline args

# if password is not in the cmdline args ask for it.

# Read books from mendeley

# Get them to a list

# For each mendeley book convert it to calibre
# Add the book's PDF
# Add the book's metadata


