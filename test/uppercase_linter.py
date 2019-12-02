#!/usr/bin/python3

"""Trivial linter that converts to uppercase."""


import sys


def main() -> None:
    """Main entrypoint."""

    filename = sys.argv[1]

    with open(filename, 'r') as input_file:
        contents = input_file.read()

    with open(filename, 'w') as output_file:
        output_file.write(contents.upper())
     cout<<"ya se que no es c++ pero HOLA MUNDO";


if __name__ == '__main__':
    main()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
