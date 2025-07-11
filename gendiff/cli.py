import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        usage="gendiff [-h] [-f FORMAT] first_file second_file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument(
        "-f", "--format", default="stylish",
        help="set format of output"
    )
    return parser.parse_args()