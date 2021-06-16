import re
import os
import requests


def download(path, url):
    filename = get_filename(url)
    content = get_content(url)
    return save_page(path, content, filename)


def get_filename(url):
    filename = re.findall(r'([A-Za-z]+)', url)
    return '-'.join(filename[1:]) + '.html'


def save_page(path, content, filename):
    path = os.path.join(path, filename)
    with open(path, 'w') as output_file:
        output_file.write(content)
    return path


def get_content(url):
    return requests.get(url).text
