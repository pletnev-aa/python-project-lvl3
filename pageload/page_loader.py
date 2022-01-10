import logging
import os
import traceback

import requests
from pageload.exceptions import NetworkError
from pageload.url import make_local_name
from pageload import html, repository
from progress.bar import ChargingBar

DEFAULT_DIR = os.getcwd()

logger = logging.getLogger(__name__)


def download(url, path):
    page_name = make_local_name(url, ext='.html')
    page_path = os.path.join(path, page_name)
    try:
        page = get_content(url)
    except requests.exceptions.RequestException as exp:
        logger.debug(traceback.format_exc(2, chain=False))
        logger.error('Cannot download page: {0} \n{1}'.format(
            url,
            traceback.format_exc(0, chain=False),
        ))
        raise NetworkError from exp

    files_dir = make_local_name(url, ext='_files')
    updated_page, files_urls = html.update(page, url, files_dir)
    page_path = repository.save(updated_page, page_path)

    if files_urls:
        dir_path = os.path.join(path, files_dir)
        os.makedirs(dir_path, exist_ok=True)
        download_assets(files_urls, dir_path)

    return page_path


def download_assets(files, dir_path):
    with ChargingBar('Downloading', max=len(files)) as bar:
        for url, local_name in files.items():
            try:
                asset = get_content(url)
                local_path = os.path.join(dir_path, local_name)
                repository.save(asset, local_path, 'wb')
                bar.next()
            except requests.exceptions.RequestException:
                logger.debug(traceback.format_exc(2, chain=False))
                logger.warning('{} download will be skipped'.format(url))


def get_content(url):
    response = requests.get(url)
    response.raise_for_status()
    logger.info('Got content {}'.format(url))
    return response.content
