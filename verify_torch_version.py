from argparse import ArgumentParser, Namespace

import torch
from packaging import version


def main() -> None:
    args = parse_args()

    found_version = version.parse(torch.__version__).release
    specified_version = version.parse(args.torch_version).release

    assert found_version == specified_version, (found_version, specified_version)


def parse_args() -> Namespace:
    parser = ArgumentParser(description="Verify version of torch.")

    parser.add_argument(
        "--torch-version",
        type=str,
        help="Expected version of torch.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
