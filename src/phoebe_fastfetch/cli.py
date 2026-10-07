"""Command-line interface for Phoebe Fastfetch."""

import argparse
from collections.abc import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ff",
        description="Display a random Phoebe Hub image with Fastfetch.",
    )
    parser.add_argument(
        "fastfetch_args",
        nargs=argparse.REMAINDER,
        help="arguments passed through to Fastfetch",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    build_parser().parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
