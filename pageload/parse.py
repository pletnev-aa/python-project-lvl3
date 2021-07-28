import logging
import re
from pathlib import Path
from urllib.parse import urlparse, urlunparse, urljoin
import requests
from bs4 import BeautifulSoup


TAGS = {
    'link': 'href',
    'script': 'src',
    'img': 'src',
}


def get_data(url):
    try:
        if requests.get(url).status_code == requests.codes.ok:
            return requests.get(url).content
        raise
    except:  # noqa: 
        logging.warning(
            'Error request: {}'.format(url)
        )


def get_assets(url, domain, output):
    html_soup = BeautifulSoup(get_data(url), 'html.parser')
    names = []
    links = []
    for tag in html_soup.find_all(TAGS.keys()):
        key = TAGS[tag.name]
        name = tag.get(key)
        if name and name.startswith('/'):
            link = urljoin(url, name)
            if urlparse(link).netloc == domain:
                links.append(link)
                name = urlparse(link).path
                if Path(name).suffix:
                    name = output / Path(get_name(
                        domain + name.split(Path(name).suffix)[0],
                        suffix=Path(name).suffix))
                else:
                    name = output / Path(get_name(
                        domain + name, suffix='.html'))
                tag[key] = name
                names.append(name)
    return dict(zip(names, links)), html_soup.prettify(formatter="html5")


def get_name(obj, sep='-', suffix=''):
    name = sep.join(re.findall(r'([A-Za-z0-9]+)', obj))
    # if len(name) > 50:
    #     name = name[0:50]
    if suffix:
        return name + suffix
    return name


def parse(url):
    url = urlparse(url)
    name = get_name(url.netloc + url.path, suffix='.html')
    output = get_name(url.netloc + url.path, suffix='_files')
    domain = url.netloc
    assets, soup = get_assets(urlunparse(url), domain, output)
    return {
        'html_name': name,
        'html': soup,
        'output': output,
        'assets': assets,
    }
