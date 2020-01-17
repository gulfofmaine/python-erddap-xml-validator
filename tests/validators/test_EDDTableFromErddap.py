from lxml import etree as ET

from erddap_xml.validators.EDDTableFromErddap import EDDTableFromErddap

dataset_path = "./tests/validators/EDDTableFromErddap.xml"
tree = ET.parse(dataset_path)
root = tree.getroot()


def test_EDDTableFromErddap_check_source_url():
    validator = EDDTableFromErddap(dataset_path, root)

    assert validator.check_source_url()


def test_EDDTableFromErddap_validate():
    validator = EDDTableFromErddap(dataset_path, root)

    assert validator.validate()
