import argparse
from pathlib import Path


def get_args():
    usage = '%(prog)s [options] <url>'
    parser = argparse.ArgumentParser(prog='page-loader',
                                     description='download and save page',
                                     usage=usage)
    parser.add_argument('url', type=str)
    parser.add_argument(
        '-o', '--output',
        default='.',
        nargs='?',
        help='set the directory to save to',
    )
    args = parser.parse_args()
    url = args.url
    path = Path(args.output)
    return path, url
