import logging
from pathlib import Path


def save_data(path, data):
    if isinstance(data, bytes):
        decoding = 'wb'
    else:
        decoding = 'w'
    try:
        with open(path, decoding) as file:
            file.write(data)
            logging.info('Save file: {}'.format(path))
            file.close()
    except (FileNotFoundError, OSError) as e:
        logging.warning('{}: {}'.format(e, path))
        raise e
    return path


def make_dir(path):
    try:
        if Path.is_dir(path):
            logging.info('Directory exists: {}'.format(path))
            return path
        else:
            Path.mkdir(path)
            logging.info('Create directory: {}'.format(path))
    except (FileNotFoundError, OSError) as e:
        logging.warning('{}: {}'.format(e, path))
        raise e
