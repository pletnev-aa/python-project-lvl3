#!/usr/bin/env python3
import logging
import sys

from pageload import cli, page_loader
from pageload.logging import setup
from pageload.exceptions import FileSystemError, NetworkError

logger = logging.getLogger(__name__)


def main():
    path, url, log_level = cli.get_args()
    setup(log_level)
    try:
        page = page_loader.download(url, path)
    except (NetworkError, FileSystemError):
        sys.exit(1)
    print(page)


if __name__ == '__main__':
    main()
