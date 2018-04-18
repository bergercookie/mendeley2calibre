#!/usr/bin/env python3

import click
import logging

from mendeley2calibre.utils import convert_mendeley_to_calibre_ref
from lmendeley.MendeleyDbInterface import MendeleyDbInterface
from mendeley2calibre.clogger import setup_logging

# setup logging
logger = logging.getLogger(__file__)
setup_logging(__file__)


# Parse cmdline args
@click.command()
@click.option("--calibre-lib", "-c",
              required=True,
              type=click.Path(exists=True),
              help="Top-level path to the calibre library")
def main(calibre_lib):
    logger.info("Initialising conversion procedure: Mendeley -> Calibre...")
    logger.info("Calibre lib: {}".format(calibre_lib))

    with MendeleyDbInterface() as mendeley_db:
        # Read books from mendeley
        mendeley_db.load_all_references()

        # For each mendeley book convert it to calibre
        for mendeley_ref in mendeley_db.doc_id_to_reference.values():
            logger.info("Converting {}...".format(mendeley_ref))
            calib_ref = convert_mendeley_to_calibre_ref(mendeley_ref)
            calib_ref.write_to_db(calibre_lib)

if __name__ == "__main__":
    main()
