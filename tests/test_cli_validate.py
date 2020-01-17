from erddap_xml import cli_validate

dataset_path = "./tests/validators/EDDTableFromErddap.xml"


def test_cli_validate(capsys):
    cli_validate.main([dataset_path])

    captured = capsys.readouterr()
    assert "Valid Dataset" in captured.out
