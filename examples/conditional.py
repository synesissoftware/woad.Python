#! /usr/bin/env python

"""Print a sequence only when the stream supports colour."""

from __future__ import print_function

import sys

import woad


def main():

    stream = sys.stdout
    green = woad.seq_for(stream, woad.FG_GREEN)
    reset = woad.seq_for(stream, woad.RESET)

    print(green + 'ok' + reset)

    return 0


if __name__ == '__main__':

    sys.exit(main())
