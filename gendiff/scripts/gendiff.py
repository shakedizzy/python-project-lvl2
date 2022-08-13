#!/usr/bin/env python3

import gendiff.engine
from gendiff.lib.cli import define_args


def main():
    args = define_args()
    gendiff.engine.main(args.first_file, args.second_file, args.set_format)


if __name__ == '__main__':
    main()
