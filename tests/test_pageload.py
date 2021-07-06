import pytest
import tempfile
import requests
import requests_mock
from pathlib import Path
from pageload import parse, fs


@pytest.mark.parametrize('url,html', [
    ('https://page-loader.hexlet.repl.co',
     'tests/fixtures/page-loader-hexlet-repl-co.html',
     ),
])
def test_download_html(url, html):
    with open(html) as data:
        exp_html = data.read()
    with requests_mock.Mocker() as mock:
        mock.get(url, text=exp_html)
        data.close()
    with tempfile.TemporaryDirectory() as path:
        ath = Path(path)
        name = parse.get_name(url) + '.html'
        result = fs.save_data(ath / name, requests.get(url).text)
        assert Path.is_file(result)
        assert Path(result).name == Path(html).name
