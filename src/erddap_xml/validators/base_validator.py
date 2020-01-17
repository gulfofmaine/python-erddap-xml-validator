from lxml import etree as ET  # type: ignore


class DatasetValidationError(Exception):
    """ Thrown when a dataset is unable to be validated """

    def __init__(self, dataset: str, message: str):
        self.message = f"Unable to validate dataset ({dataset}): {message}"

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message


class DatasetValidator:
    """ Base dataset validation class """

    erddap_type = NotImplemented

    def __init__(self, dataset_path: str, root: ET.Element):
        self.dataset_path = dataset_path
        self.root = root

    def check_type(self) -> bool:
        """ Checks that the type is set on the dataset """
        if self.erddap_type is NotImplemented:
            raise DatasetValidationError(
                self.dataset_path, "erddap_type is not set on DatasetValidator"
            )

        if self.root.attrib["type"] != self.erddap_type:
            raise DatasetValidationError(self.dataset_path, "Invalid dataset type")

        return True

    def validate(self) -> bool:
        """ Validate a given dataset XML so that it should work on ERDDAP """
        return self.check_type()
