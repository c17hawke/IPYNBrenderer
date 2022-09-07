import pytest
from IPYNBrenderer import render_site
from IPYNBrenderer.custom_exception import InvalidURLException

class TestRenderSite:
    URL_test_success_data = [
        ("http://pytorch.org", "success"),
        ("https://pytorch.org", "success"),
    ]

    URL_test_bad_data = [
        ("http://pytorch"),
        ("http//pytorch"),
        ("http:/pytorch"),
        ("http/pytorch"),
        ("http/pytorch"),
        ("pytorch.org"),
        ("http://asyef/"),
    ]

    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_site_success(self, URL, response):
        assert render_site(URL) == response

    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_site_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_site(URL)