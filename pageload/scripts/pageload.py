#!/usr/bin/env python3
from pageload import cli
from pageload import pageload


def main():
    path, url = cli.get_args()
    return print(pageload.download(path, url))


if __name__ == '__main__':
    main()
