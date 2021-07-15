#!/usr/bin/env python3
import sys
from pageload import cli
from pageload import page_loader
from pageload.config import set_logging
from requests import exceptions


def main():
    path, url = cli.get_args()
    set_logging()
    try:
        print(page_loader.download(path, url))
    except (OSError, exceptions.RequestException):
        sys.exit(1)


if __name__ == '__main__':
    main()
