import logging

import yt_dlp
from youtube_dl_utils import OUTPUT_TEMPLATE, YoutubeDlLogger, my_hook


def download_mp3(youtube_url):
    YDL_OPTIONS = {
        "format": "bestaudio/best",
        "outtmpl": OUTPUT_TEMPLATE,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "logger": YoutubeDlLogger(),
        "progress_hooks": [my_hook],
    }

    logging.info(f"downloading...{youtube_url}")

    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.download([youtube_url])

        logging.info("done downloading and converting")
