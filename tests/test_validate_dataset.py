from erddap_xml import validate_dataset

dataset_path = "./tests/validators/EDDTableFromErddap.xml"


def test_validate_dataset_xml():
    validate = validate_dataset.validate_dataset_xml(dataset_path)

    assert validate
