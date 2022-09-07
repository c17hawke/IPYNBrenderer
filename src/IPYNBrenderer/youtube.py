from IPython import display
from ensure import ensure_annotations
from IPYNBrenderer.custom_exception import InvalidURLException
from IPYNBrenderer.logger import logger
from py_youtube import Data


@ensure_annotations
def get_time_info(URL: str) -> int:
    def _verify_vid_id_len(vid_id, __expected_len=11):
        len_of_vid_id = len(vid_id)
        if len_of_vid_id != __expected_len:
            raise InvalidURLException(
                f"Invalid video id with length: {len_of_vid_id}, expected: {__expected_len}"
            )

    try:
        split_val = URL.split("=")
        if len(split_val) > 3:
            raise InvalidURLException
        if "watch" in URL:
            if "&t" in URL:
                vid_id, time = split_val[-2][:-2], int(split_val[-1][:-1])
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
            else:
                vid_id, time = split_val[-1], 0
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
        else:
            if "=" in URL and "?t" in URL:
                vid_id, time = split_val[0].split("/")[-1][:-2], int(split_val[-1])
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
            else:
                vid_id, time = URL.split("/")[-1], 0
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
    except Exception:
        raise InvalidURLException


@ensure_annotations
def render_YouTube_video(URL: str, width: int = 780, height: int = 600) -> str:
    try:
        if URL is None:
            raise InvalidURLException("URL cannot be None")
        data = Data(URL).data()
        if data["publishdate"] is not None:
            time = get_time_info(URL)
            vid_ID = data["id"]
            embed_URL = f"https://www.youtube.com/embed/{vid_ID}?start={time}"
            logger.info(f"embed URL: {embed_URL}")
            iframe = f"""<iframe
            width="{width}" height="{height}"
            src="{embed_URL}"
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer;
            autoplay; clipboard-write;
            encrypted-media; gyroscope;
            picture-in-picture" allowfullscreen>
            </iframe>
            """
            display.display(display.HTML(iframe))
            return "success"
        else:
            raise InvalidURLException
    except Exception as e:
        raise e
