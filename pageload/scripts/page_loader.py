#!/usr/bin/env python3
import logging
import sys

from pageload import cli, page_loader
from pageload.config import set_logging
from requests import exceptions


def main():
    path, url = cli.get_args()
    set_logging()
    try:
        result = page_loader.download(url, path)
        logging.info('Save file: {}'.format(result))
    except (OSError, exceptions.RequestException) as error:
        logging.warning(error)
        sys.exit(1)


if __name__ == '__main__':
    main()
