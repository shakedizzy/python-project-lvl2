#!/usr/bin/env python3

import argparse
import gendiff.engine


def define_args():
    parser = argparse.ArgumentParser(description='Compares two configuration \
        files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    return args


def main():
    args = define_args()
    gendiff.engine.main(args)


if __name__ == '__main__':
    main()
