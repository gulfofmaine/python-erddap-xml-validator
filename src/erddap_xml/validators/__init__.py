from typing import Dict
from typing import Type

from .base_validator import DatasetValidationError  # noqa: F401
from .base_validator import DatasetValidator
from .EDDTableFromErddap import EDDTableFromErddap
from .EDDTableFromNcCFFiles import EDDTableFromNcCFFiles

validators: Dict[str, Type[DatasetValidator]] = {
    "EDDTableFromErddap": EDDTableFromErddap,
    "EDDTableFromNcCFFiles": EDDTableFromNcCFFiles,
}
