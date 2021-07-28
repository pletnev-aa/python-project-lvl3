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
        if Path.is_dir(path):
            logging.info('Directory exists: {}'.format(path))
            return path
        else:
            Path.mkdir(path)
            logging.info('Create directory: {}'.format(path))
    except OSError():
        logging.warning('Error make dir: {}'.format(path))
