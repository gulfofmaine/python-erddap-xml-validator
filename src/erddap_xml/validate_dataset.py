#!/usr/bin/env python3
""" Dataset XML stub validation

Funtions throw DatasetValidationError if an invalid dataset is found
"""
from pathlib import Path
from typing import Union

from lxml import etree as ET  # type: ignore

from erddap_xml.validators import DatasetValidationError
from erddap_xml.validators import validators


def validate_dataset_tag(dataset_path: str, root: ET.Element) -> bool:
    """ Validate that a dataset tag has required elements """
    if root.tag != "dataset":
        raise DatasetValidationError(dataset_path, "Root tag is not `dataset`")

    for key in ("type", "datasetID", "active"):
        if key not in root.attrib:
            raise DatasetValidationError(
                dataset_path, f"`{key}` is not in root dataset tag"
            )

        if root.attrib[key] == "":
            raise DatasetValidationError(
                dataset_path, f"`{key}` doesn't have a value in the root dataset tag"
            )

    return True


def dataset_id(dataset_path: str, tree: ET.ElementTree) -> str:
    """ Return the datasetId from the root dataset tag """
    root = tree.getroot()
    try:
        return root.attrib["datasetID"]
    except KeyError:
        raise DatasetValidationError(
            dataset_path, "`datasetID` attribute does not exist on root dataset tag"
        )


def validate_dataset_xml(dataset: Union[str, Path]) -> ET.ElementTree:
    """ Returns dataset ElementTree if the dataset has valid XML

    a DatasetValidationError will be thrown when a dataset is invalid with
    details about why it's invalid.
    """
    dataset_path = str(dataset)
    tree = ET.parse(dataset_path)

    root = tree.getroot()

    validate_dataset_tag(dataset_path, root)

    dataset_type = root.attrib["type"]

    Validator = validators[dataset_type]

    if Validator(dataset_path, root).validate():
        return tree

    raise DatasetValidationError(dataset_path, "Unable to validate")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Validate an ERDDAP dataset")
    parser.add_argument("input_path", help="ERDDAP dataset XML stub")

    args = parser.parse_args()

    if validate_dataset_xml(args.input_path) is not None:
        print("Valid dataset")
    else:
        print("Invalid dataset")
