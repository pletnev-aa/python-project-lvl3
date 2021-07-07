from pageload import fs, parse


def download(path, url):
    data = parse.get_data(url)
    html_name = parse.get_name(url) + '.html'
    html = fs.save_data(path / html_name, data)
    output = parse.get_name(url) + '_files'
    fs.make_dir(path / output)
    domain = parse.get_domain(url)
    assets, html_soup = parse.get_assets(html, domain, output)
    for asset in assets:
        assets[asset] = fs.save_data(path / output / asset, assets[asset])
    return fs.save_data(path / html_name, html_soup)
