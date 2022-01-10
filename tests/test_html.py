import pytest
from bs4 import BeautifulSoup
from pageload.url import make_local_name
from pageload.html import update


@pytest.mark.parametrize('test_html, expected_html, url', [
    ('tests/fixtures/test_page.html',
     'tests/fixtures/expected.html',
     'https://ru.hexlet.io/courses',)])
def test_html_update(test_html, expected_html, url):
    with open(test_html) as content:
        test_html = content.read()
        content.close()
    with open(expected_html) as content:
        expected_html = content.read()
        content.close()
    files_dir = make_local_name(url, ext='_files')
    expected_html = BeautifulSoup(expected_html, 'html.parser').prettify()
    html, _ = update(test_html, url, files_dir)
    assert html == expected_html
