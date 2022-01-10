import pytest
from pageload.exceptions import NetworkError, FileSystemError
from pageload.page_loader import download


url = 'https://ru.hexlet.io/courses'


def test_download_wrong_status_code(requests_mock, tmpdir):
    requests_mock.get(url, status_code=404)
    with pytest.raises(NetworkError):
        download(url, tmpdir)


def test_save_wrong_filepath(requests_mock):
    requests_mock.get(url)
    with pytest.raises(FileSystemError):
        download(url, 'wrong/path')
