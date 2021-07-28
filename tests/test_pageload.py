import tempfile
from pathlib import Path

import pytest
import requests_mock
from pageload import fs, parse

url = 'https://page-loader.hexlet.repl.co'


@pytest.mark.parametrize('html,img,exp_html,output', [
    ('tests/fixtures/page-loader-hexlet-repl-co.html',
     'tests/fixtures/page-loader-hexlet-repl-co-assets-professions-nodejs.png',
     'tests/fixtures/expected.html',
     'page-loader-hexlet-repl-co_files'
     ),
])
def test_download_html(html, img, exp_html, output):
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
        url_parse = parse.parse(url)
        fs.make_dir(path / url_parse['output'])
        mock.get(
            url_parse['assets'][Path(Path(output) / Path(img).name)],
            content=test_img
        )
        page = fs.save_data(
            path / url_parse['html_name'],
            url_parse['html']
        )
        test_image = fs.save_data(
            path / url_parse['output'] / Path(img).name,
            parse.get_data(
                url_parse['assets'][Path(Path(output) / Path(img).name)])
        )
        assert Path.is_file(page)
        assert Path(page).name == Path(html).name
        assert Path.read_text(page) == exp_html
        assert Path.is_file(test_image)
        assert Path.read_bytes(test_image) == test_img
