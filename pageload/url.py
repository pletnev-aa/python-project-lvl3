import os
import re
from urllib.parse import urlparse


def make_local_name(url, ext='.html'):
    parsed_url = urlparse(url)
    root, extension = os.path.splitext(urlparse(url).path)
    path = _generate(os.path.join(parsed_url.netloc + root))

    if extension:
        ext = extension

    return '{0}{1}'.format(path, ext)


def _generate(name):
    name = name.rstrip('/')
    return re.sub(r'[^\w]', '-', name)


def is_local(full_url, url):
    return urlparse(full_url).netloc == urlparse(url).netloc
