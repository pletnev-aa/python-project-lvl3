from pathlib import Path
import pytest
import requests_mock
from pageload import parse

url = 'https://page-loader.hexlet.repl.co'


@pytest.mark.parametrize('html,output,exp_html', [
    ('tests/fixtures/page-loader-hexlet-repl-co.html',
     'page-loader-hexlet-repl-co_files',
     'tests/fixtures/expected.html',)])
def test_parser(html, output, exp_html):
    with open(html) as data:
        test_html = data.read()
        data.close()
    with open(exp_html) as data:
        exp_html = data.read()
        data.close()
    with requests_mock.Mocker() as mock:
        mock.get(url, text=test_html)
        result = parse.parse(url)
        assert result['html_name'] == Path(html).name
        assert result['html'] == exp_html
        assert result['output'] == output
        assert isinstance(result['assets'], dict)
