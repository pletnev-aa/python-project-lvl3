import pytest
import tempfile
import requests
import requests_mock
from pathlib import Path
from pageload import parse, fs


@pytest.mark.parametrize('url,html,img,exp_html', [
    ('https://page-loader.hexlet.repl.co',
     'tests/fixtures/page-loader-hexlet-repl-co.html',
     'tests/fixtures/page-loader-hexlet-repl-co-assets-professions-nodejs.png',
     'tests/fixtures/expected.html'
     ),
])
def test_download_html(url, html, img, exp_html):
    with open(html) as data:
        test_html = data.read()
        data.close()
    with open(img, 'rb') as data:
        test_img = data.read()
        data.close()
    with open(exp_html) as data:
        exp_html = data.read()
        data.close()
    with requests_mock.Mocker() as mock:
        mock.get(url, text=test_html)
    with tempfile.TemporaryDirectory() as path:
        path = Path(path)
        name = parse.get_name(url) + '.html'
        app_html = fs.save_data(
            path / name,
            requests.get(url).text
        )
        assert Path.is_file(app_html)
        assert Path(app_html).name == Path(html).name
        assert Path.read_text(app_html) == test_html
        domain = parse.get_domain(url + '/courses')
        app = Path(parse.get_name(url) + '_files')
        fs.make_dir(path / app)
        assets, finished_html = parse.get_assets(app_html, domain, app)
        mock.get(assets[Path(img).name], content=test_img)
        finished_img = fs.save_data(
            path / app / Path(img).name,
            requests.get(assets[Path(img).name]).content
        )
        result = fs.save_data(app_html, finished_html)
        assert domain == url
        assert Path.is_dir(path / app)
        assert Path.is_file(finished_img)
        assert Path.read_bytes(finished_img) == test_img
        assert Path.read_text(result) == exp_html
