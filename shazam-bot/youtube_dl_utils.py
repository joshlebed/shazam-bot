from urllib.parse import parse_qs, urlparse

OUTPUT_TEMPLATE = "%(id)s"


class YoutubeDlLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


def get_output_filepath(video_id):
    output_path = OUTPUT_TEMPLATE % {"id": video_id}
    return f'{output_path}.mp3'


def get_video_id(value):
    """
    copied from online somewhere
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse(value)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in ("www.youtube.com", "youtube.com"):
        if query.path == "/watch":
            p = parse_qs(query.query)
            return p["v"][0]
        if query.path[:7] == "/embed/":
            return query.path.split("/")[2]
        if query.path[:3] == "/v/":
            return query.path.split("/")[2]
    return None
