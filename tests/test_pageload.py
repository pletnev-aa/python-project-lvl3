import pytest
import tempfile
from pageload import parse, fs
from pathlib import Path


@pytest.mark.parametrize('url,html', [
    ('https://page-loader.hexlet.repl.co/',
     'tests/fixtures/page-loader-hexlet-repl-co.html',
     ),
])
def test_download_html(url, html):
    with tempfile.TemporaryDirectory() as path:
        path = Path(path)
        name = parse.get_name(url) + '.html'
        result = fs.save_data(
            path / name,
            parse.get_data(url)
        )
        assert Path.is_file(result)
        assert open(result).read() == open(html).read()
