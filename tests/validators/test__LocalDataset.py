from lxml import etree as ET

from erddap_xml.validators._LocalDataset import _LocalDataset

dataset_path = "./tests/validators/EDDTableFromNcCFFiles.xml"
tree = ET.parse(dataset_path)
root = tree.getroot()


def test__LocalDataset_reload_minutes():
    validator = _LocalDataset(dataset_path, root)

    assert validator.reload_minutes()
