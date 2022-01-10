import logging

CONFIGS = {
    'debug': {
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'level': 'DEBUG',
        'handlers': [
            logging.StreamHandler(),
            logging.FileHandler('page_loader.log'),
        ],
    },
    'warning': {
        'format': '%(asctime)s - %(levelname)s - %(message)s',
        'level': 'WARNING',
        'handlers': [
            logging.StreamHandler(),
            logging.FileHandler('page_loader.log'),
        ],
    },
}


def setup(level):
    logging.basicConfig(
        level=CONFIGS[level]['level'],
        format=CONFIGS[level]['format'],
        handlers=CONFIGS[level]['handlers'],
    )
