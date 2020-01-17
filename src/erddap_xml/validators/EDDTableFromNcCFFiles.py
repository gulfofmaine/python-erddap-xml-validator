from ._LocalDataset import _LocalDataset


class EDDTableFromNcCFFiles(_LocalDataset):
    erddap_type = "EDDTableFromNcCFFiles"

    def validate(self) -> bool:
        return all([super(EDDTableFromNcCFFiles, self).validate()])
