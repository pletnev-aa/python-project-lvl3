import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from pageload.url import is_local, make_local_name

TAGS = ('img', 'link', 'script')

ATTRIBUTES = {
    'img': 'src',
    'link': 'href',
    'script': 'src',
}


def update(page, url, files_dir):
    tree = BeautifulSoup(page, 'html.parser')
    files = {}
    tags = tree.find_all(TAGS)
    for tag in tags:
        name = ATTRIBUTES[tag.name]
        resource_url = tag.get(name)
        full_url = urljoin(url, resource_url)

        if is_local(full_url, url):
            local_name = make_local_name(full_url)
            files[full_url] = local_name
            tag[name] = os.path.join(files_dir, local_name)

    updated_page = tree.prettify()
    return updated_page, files
