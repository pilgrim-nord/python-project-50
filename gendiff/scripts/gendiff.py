
from gendiff.scripts.cli import parse_arguments
from gendiff.scripts.generate import generate_diff


def main():

    args = parse_arguments()

    diff = generate_diff(args.first_file, args.second_file, args.format)

    print(diff)


if __name__ == "__main__":
    main()
