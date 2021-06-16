import os
import pytest
import tempfile
from pageload import pageload


@pytest.mark.parametrize('url,exp_name', [
    ('https://ru.hexlet.io/courses',
     'ru-hexlet-io-courses.html'
     ),
])
def test_filename(url, exp_name):
    with tempfile.TemporaryDirectory() as path:
        exp_name = os.path.join(path, exp_name)
        assert os.path.isfile(pageload.download(path, url))
        assert exp_name == pageload.download(path, url)
