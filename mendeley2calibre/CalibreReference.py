from lmendeley.GenericReference import GenericReference

import os
import sh
import tempfile
from typing import List
import urllib.request
from copy import deepcopy


class CalibreReference(GenericReference):
    """Simple class to hold a Calibre document's reference data.
    """

    """Keys in a document that the CalibreReference instance cares about"""
    param_keys = [
        "author_sort",
        "authors",
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

    def write_to_db(self, library_path: str) -> None:
        """Write the current instance to the Calibre db.

        Current tool constitutes a thin wrapper around the calibredb command

        :param library_path: Path to the toplevel calibre library that is to be
                             used
        """

        def interact_with_lib(*calibre_db_args):
            """Interact with the calibre library"""
            args = list(deepcopy(calibre_db_args))
            args.append("--with-library={}".format(library_path))
            sh.calibredb(args)


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
        interact_with_lib("search", self.params["title"])
        print("add_ret: ", add_ret)
        print("search_ret: ", search_ret)


        # TODO: Insert a book in calibre - how to manage the fields?

