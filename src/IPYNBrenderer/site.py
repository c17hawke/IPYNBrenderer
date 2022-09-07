from IPython import display
from ensure import ensure_annotations
import urllib.request
from IPYNBrenderer.custom_exception import InvalidURLException
from IPYNBrenderer.logger import logger


@ensure_annotations
def is_valid(URL: str) -> bool:
    try:
        response_status = urllib.request.urlopen(URL).getcode()
        assert response_status == 200
        logger.debug(f"response_status: {response_status}")
        return True
    except Exception as e:
        logger.exception(e)
        return False


@ensure_annotations
def render_site(URL: str, width: str = "100%", height: str = "600") -> str:
    try:
        if is_valid(URL):
            response = display.IFrame(src=URL, width=width, height=height)
            display.display(response)
            return "success"
        else:
            raise InvalidURLException
    except Exception as e:
        raise e
