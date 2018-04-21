"""Utility methods"""

from lmendeley.MendeleyReference import MendeleyReference
from .CalibreReference import CalibreReference
from typing import Dict


"""Mendeley <-> Calibre correspondences"""
props_correspondences = {
    "language": "languages",
    "series": "series",
    "seriesNumber": "series_index",
    "title": "title",
    "publisher": "publisher",
}  # Dict[str, str]


def convert_mendeley_to_calibre_ref(mendeley_ref: MendeleyReference) \
        -> CalibreReference:
    """Convert a MendeleyReference to the corresponding CalibreReference
    instance.

    TODO: Unittest this - Have a sample reference - convert it to the Calibre
    format

    """

    calib_ref = CalibreReference()

    # TODO: Make conversion method Mendeley <-> Calibre

    # fill the corresponding fields
    calib_ref.doc_url = mendeley_ref.doc_url

    # author_sort - authors
    # TODO

    # comment
    # bundle abstract, notes, ... in the comments
    if mendeley_ref.params["abstract"]:
        calib_ref.params["comments"] = "{}\n\n---\n\n".format(
            mendeley_ref.params["abstract"])

    # Add the rest of correspondences for which there is no Calibre field
    for prop_str in ["pages",
                     "publication",
                     "citationKey",
                     "institution",
                     "volume",
                     "note", ]:
        if mendeley_ref.params[prop_str]:  # if not empty...
            calib_ref.params["comments"] += "{}: {}\n"\
                .format(prop_str, mendeley_ref.params[prop_str])


    # convert properties
    # bundle isbn, doi to the identifiers
    calib_ref.params["identifiers"] = [mendeley_ref.params[i] for i in ["doi",
                                                                        "uuid"]]
    calib_ref.params["identifiers"] = [i.strip('{}') for i in
                                       calib_ref.params["identifiers"] if i]

    # favourite -> high rating
    if mendeley_ref.params["favourite"]:
        calib_ref.params["rating"] = 5

    # Direct correspondences
    for m_param, c_param in props_correspondences.items():
        calib_ref.params[c_param] = mendeley_ref.params[m_param]

    # TODO - copy the mendeley tags as well
    # add the rest of mendeley properties in the calibre "tags"
    calib_ref.params["tags"] = mendeley_ref.params["type"]

    return calib_ref


def convert_calibre_to_mendeley_ref(calibre_ref: CalibreReference) \
        -> MendeleyReference:
    """Convert a MendeleyReference to the corresponding CalibreReference
    instance.

    .. todo:: Unittest this - Have a sample reference - convert it to the
              Calibre format
    .. todo:: Implement this

    """

    raise NotImplementedError()

    mendeley_ref = MendeleyReference()
    # fill the corresponding fields
    return mendeley_ref
