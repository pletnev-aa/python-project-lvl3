#!/usr/bin/env python3
from pageload import cli
from pageload import page_loader
from pageload.config import set_logging


def main():
    path, url = cli.get_args()
    set_logging()
    html = page_loader.download(path, url)
    return print(html)


if __name__ == '__main__':
    main()
