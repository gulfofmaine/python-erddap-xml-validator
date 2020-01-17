import os

from .base_validator import DatasetValidationError
from .base_validator import DatasetValidator


class _LocalDataset(DatasetValidator):
    def reload_minutes(self) -> bool:
        """ Check that the `reloadEveryNMinutes` tag exists and is a reasonable value

        Default minimum reloadEveryNMinutes is 15, but that can be overridden via
        setting ERDDAP_DATASET_MINIMUM_RELOAD_MINUTES environment variable to a value.
        """
        try:
            reload_minutes = float(self.root.find("reloadEveryNMinutes").text)
        except (AttributeError, ValueError, TypeError):
            raise DatasetValidationError(
                self.dataset_path,
                "`reloadEveryNMinutes` doesn't have a valid reload time",
            )

        minimum_reload_minutes: float = 15

        try:
            minimum_reload_minutes = float(
                os.environ.get("ERDDAP_DATASET_MINIMUM_RELOAD_MINUTES", "0")
            )
        except (TypeError, ValueError):
            pass

        if minimum_reload_minutes < 1:
            minimum_reload_minutes = 1

        if reload_minutes < minimum_reload_minutes:
            raise DatasetValidationError(
                self.dataset_path,
                f"`reloadEveryNMinutes` ({reload_minutes}) is set below the minimum {minimum_reload_minutes}",
            )

        return True

    def validate(self) -> bool:
        return all([self.reload_minutes(), super(_LocalDataset, self).validate()])
