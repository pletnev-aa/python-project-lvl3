import logging
from pathlib import Path


def save_data(path, data):
    if isinstance(data, bytes):
        decoding = 'wb'
    else:
        decoding = 'w'
    with open(path, decoding) as file:
        file.write(data)
        logging.info('Save file: {}'.format(path))
        file.close()
    return path


def make_dir(path):
    try:
        Path.mkdir(path)
        logging.info('Create directory for files: {}'.format(path))
    except OSError as e:
        logging.warning('Error writing of file: {}'.format(e))
