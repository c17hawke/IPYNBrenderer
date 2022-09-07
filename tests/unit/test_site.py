import pytest
from IPYNBrenderer import is_valid

URL_test_data = [
    ("http://pytorch.org", True),
    ("https://pytorch.org", True),
    ("http://pytorch", False),
    ("http//pytorch", False),
    ("http:/pytorch", False),
    ("http/pytorch", False),
    ("http/pytorch", False),
    ("pytorch.org", False),
    ("http://asyef/", False),
]

@pytest.mark.parametrize("URL, response", URL_test_data)
def test_is_valid(URL, response):
    assert is_valid(URL) == response