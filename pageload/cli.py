import argparse

from pageload import logging
from pageload.page_loader import DEFAULT_DIR


def get_args():
    usage = '%(prog)s [options] <url>'
    default_log_level = 'warning'
    parser = argparse.ArgumentParser(prog='page-loader',
                                     description='Download and save page',
                                     usage=usage)
    parser.add_argument('url', type=str)
    parser.add_argument(
        '-o', '--output',
        default=DEFAULT_DIR,
        help='Set the directory to save to',
    )
    parser.add_argument(
        '-l',
        '--log-level',
        help='Sets log level',
        default=default_log_level,
        choices=logging.CONFIGS.keys(),
    )
    args = parser.parse_args()
    return args.output, args.url, args.log_level
