from lmendeley.GenericReference import GenericReference

import os
import sh
import tempfile
from typing import List, Dict
import urllib.request
from copy import deepcopy

import logging
from .clogger import setup_logging

logger = logging.getLogger(__file__)
setup_logging(__file__)


class CalibreReference(GenericReference):
    """Simple class to hold a Calibre document's reference data.
    """

    """Keys in a document that the CalibreReference instance cares about"""
    param_keys = [
        "comments",
        "cover",
        "identifiers",
        "languages",
        "pubdate",
        "publisher",
        "rating",
        "series",
        "series_index",
        "size",
        "sort",
        "tags",
        "timestamp",
        "title",
    ]  # type: List[str]

    param_key_to_type = {
        "comments": str,
        "cover": str,
        "identifiers": list,
        "languages": str,
        "pubdate": str,
        "publisher": str,
        "rating": int,
        "series": str,
        "series_index": str,
        "size": str,
        "sort": str,
        "tags": list,
        "timestamp": int,
        "title": str,
    }  # type: Dict[str, type]


    # TODO - use them
    custom_param_keys = [
        "isbn",
        "doi",
        "uuid",
        "citationKey",
    ]
    custom_param_datatypes = [
        "text",
        "text",
        "text",
        "text",
    ]
    custom_param_keys_to_datatypes = zip(custom_param_keys,
                                         custom_param_datatypes)

    def __init__(self, *args, **kargs):
        GenericReference.__init__(self, *args, **kargs)

        """Parameters of a Calibre Reference."""
        self.params = {
            key: CalibreReference.param_key_to_type[key]() \
            for key in CalibreReference.param_keys
        }

        self.params.update(kargs)

    def write_to_db(self, library_path: str) -> bool:
        """Write the current instance to the Calibre db.

        Current tool constitutes a thin wrapper around the calibredb command

        :param library_path: Path to the toplevel calibre library that is to be
                             used
        :returns True if operation was successful
        """

        def interact_with_lib(*calibre_db_args) -> sh.RunningCommand:
            """Interact with the calibre library"""
            args = list(deepcopy(calibre_db_args))
            args.append("--with-library={}".format(library_path))
            return sh.calibredb(args)


        # Add the new book, then search and grab its ID - Use the latter to set
        # the metadata accordingly

        # write the book to a temporary file
        self._temp_res_dir = os.path.join(tempfile.gettempdir(),
                                          "tmp_calibr_file.{}".format(
                                              self.get_doc_extension()))
        conts = urllib.request.urlopen(self.doc_url).read()
        with open(self._temp_res_dir, 'wb') as f:
            f.write(conts)

        interact_with_lib("add", self._temp_res_dir,
                          "--title", self.params["title"])

        # deal with bug in cli parsing of calibre - escape parens
        calibr_id = interact_with_lib("search", "title:\"{}\""
                                      .format(self.params["title"].replace('(', '\\(').replace(')', '\\)')))


        if not calibr_id:
            logger.warn("Failed to write book to library: {}".format(self))
            return False

        args = []
        for key, val in self.params.items():
            if val:
                if self.param_key_to_type[key] is str or \
                        self.param_key_to_type[key] is int:
                    field_val = val
                elif self.param_key_to_type[key] is list:  # e.g. tags field
                    if isinstance(val, list):
                        val_tmp = val
                    else:
                        # account for single-element lists
                        val_tmp = [val]

                    field_val = ""
                    for i in val_tmp:
                        if i:
                            field_val += "{},".format(i)
                    field_val = field_val.rstrip(',')
                else:
                    raise RuntimeError("Unknown type: {}"
                                       .format(self.param_key_to_type[key]))
                args.extend(["--field", "{}:{}".format(key, field_val)])

        # authors, authors_sort
        # Authors are set using the following syntax in calibredb
        # --field authors:"firstName1 last_name1 & first_name2 last_name2"
        if self.authors:
            authors_tmp = "{}".format(" & ".join([" ".join(i)
                                                      for i in self.authors]))
            args.extend(["--field", "authors:{}".format(authors_tmp)])
            args.extend(["--field", "author_sort:{}".format(authors_tmp)])

        interact_with_lib("set_metadata", int(calibr_id), *args)
        return True

