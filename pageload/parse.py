import logging
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from urllib import parse, error


TAGS = {
    'link': 'href',
    'script': 'src',
    'img': 'src',
}


def get_name(obj):
    obj = parse.urlparse(obj)
    if obj.netloc:
        name = '-'.join(obj.netloc.split('.')) + '-'.join(obj.path.split('/'))
        return name
    else:
        name = '-'.join(obj.path.split('/'))
        name = name if len(name.split('.')) > 1 else name + '.html'
        return name


def get_data(url):
    try:
        r = requests.get(url)
    except error.HTTPError:
        logging.warning(
            'Error request: {}'.format(url)
        )
        return None
    data = r.content
    r.close()
    return data


def get_domain(url):
    url = parse.urlparse(url)
    domain = url.scheme + '://' + url.netloc
    return domain


def get_assets(html, domain, output):
    html_soup = BeautifulSoup(Path.read_text(html), 'html.parser')
    assets = {}
    for link in html_soup.find_all(TAGS.keys()):
        name = TAGS[link.name]
        try:
            res = link[name]
            link_domain = parse.urlparse(res).netloc
            if link_domain == domain or link_domain == '':
                assets[get_name(domain) + get_name(res)] = get_data(
                    domain + res
                )
                link[name] = output / Path(get_name(domain) + get_name(res))
        except KeyError:
            continue
    return assets, html_soup.prettify(formatter='html5')
