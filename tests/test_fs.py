import tempfile
from pathlib import Path

import pytest
from pageload import fs


@pytest.fixture
def output():
    return Path('ru-hexlet-io-courses_files')


@pytest.fixture
def data():
    with open('tests/fixtures/page-loader-hexlet-repl-co.html') as data:
        return data.read()


@pytest.fixture
def name_file():
    return Path('page-loader-hexlet-repl-co.html')

def test_make_dir(output):
    with tempfile.TemporaryDirectory() as path:
        path = Path(path / output)
        fs.make_dir(path)
        assert Path.is_dir(path)
        with pytest.raises(OSError) as exc_info:
            path = Path('test' * 256 / output)
            assert fs.make_dir(path) == exc_info
        with pytest.raises(FileNotFoundError) as exc_info:
            path = Path('test' / output)
            assert fs.make_dir(path) == exc_info


def test_save_file(name_file, data):
    assert Path.is_file(fs.save_data(name_file, data))
    with pytest.raises(OSError) as exc_info:
        assert fs.save_data(Path(str(name_file) * 256), data) == exc_info
    with pytest.raises(FileNotFoundError) as exc_info:
        assert fs.save_data(Path('test' / name_file), data) == exc_info
