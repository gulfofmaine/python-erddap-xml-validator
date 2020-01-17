from urllib import parse

from .base_validator import DatasetValidationError
from .base_validator import DatasetValidator


class EDDTableFromErddap(DatasetValidator):
    """ Validate EDDTableFromErddap datasets """

    erddap_type = "EDDTableFromErddap"

    def check_source_url(self) -> bool:
        """ Check that the source URL exists, uses a valid scheme, and has a defined host """
        source_url_tag = self.root.find("sourceUrl")

        if source_url_tag is None:
            raise DatasetValidationError(
                self.dataset_path,
                "EDDTableFromErddap datasets must have a sourceUrl child tag",
            )

        url = parse.urlparse(source_url_tag.text)

        if "http" not in url.scheme:
            raise DatasetValidationError(
                self.dataset_path, "HTTP or HTTPS should be specified in sourceUrl"
            )

        if url.netloc == "":
            raise DatasetValidationError(
                self.dataset_path, "Host must be defined in sourceUrl"
            )

        return True

    def validate(self) -> bool:
        return all(
            [self.check_source_url(), super(EDDTableFromErddap, self).validate()]
        )
