#!/bin/bash

import os

from zipfile import ZipFile


def main(filename):
    with ZipFile(filename, 'rb') as zip:
        



if __name__ == "__main__":
    if len(os.Args) != 2:
        print('No epub file specified')
        os.exit(1)

    main(os.Args[1])
