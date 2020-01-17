import argparse

from erddap_xml.validate_dataset import validate_dataset_xml

parser = argparse.ArgumentParser(description="Validate an ERDDAP dataset")
parser.add_argument("input_path", help="ERDDAP dataset XML stub")


def main(args=None):
    args = parser.parse_args(args=args)

    if validate_dataset_xml(args.input_path) is not None:
        print("Valid Dataset")
    else:
        raise Exception("Invalid Dataset")
