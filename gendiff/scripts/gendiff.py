from gendiff.make_diff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        usage="gendiff [-h] [-f FORMAT] first_file second_file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument(
        "-f", "--format", dest="FORMAT", metavar="FORMAT",
        help="set format of output"
    )
    args = parser.parse_args()
    # print(args)
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
