import os
import argparse


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
        help='output dir (default: "/app")',
    )
    parser.add_argument(
        '-V', '--version',
        nargs='?',
        help='output the version number',
    )
    args = parser.parse_args()
    url = args.url
    path = get_path(args.output)
    return path, url


def get_path(path):
    if os.getcwd() != path:
        return os.path.join(os.getcwd() + path)
    return path
