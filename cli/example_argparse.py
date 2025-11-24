import argparse


def main():
    parser = argparse.ArgumentParser(
        description="argparse example",
        epilog="Example usage: python script_name.py World --count 3"
    )

    parser.add_argument(
        "name",
        type=str,
        help="The name of the person to greet (e.g., 'World' or 'Alice')."
    )

    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of times to repeat the greeting (default: 1)."
    )

    args = parser.parse_args()
    print(args.name, args.count)


if __name__ == "__main__":
    main()