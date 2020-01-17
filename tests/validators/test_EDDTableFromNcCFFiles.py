from lxml import etree as ET

from erddap_xml.validators.EDDTableFromNcCFFiles import EDDTableFromNcCFFiles

dataset_path = "./tests/validators/EDDTableFromNcCFFiles.xml"
tree = ET.parse(dataset_path)
root = tree.getroot()


def test_EDDTableFromNcCFFiles_validate():
    validator = EDDTableFromNcCFFiles(dataset_path, root)

    assert validator.validate()
