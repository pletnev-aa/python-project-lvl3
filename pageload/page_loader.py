import sys
from pageload import fs, parse
from progress.bar import Bar


def download(url, path):
    data = parse.parse(url)
    try:
        fs.make_dir(path / data['output'])
        fs.save_data(path / data['html_name'], data['html'])
    except:
        sys.exit(1)
    for asset in data['assets']:
        link = data['assets'][asset]
        with Bar(
            'LOAD - {}'.format(link),
            max=len(data['assets']) / 100,
            suffix='%(percent)d%%') as bar:  # noqa: E129
            data['assets'][asset] = parse.get_data(data['assets'][asset])
            bar.next()
    for asset in data['assets']:
            fs.save_data(path / asset, data['assets'][asset])  # noqa: E117
    return path / data['html_name']
