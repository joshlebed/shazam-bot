"""CLI entry point"""
import logging
import os
import time

from constants import LOGGING_LEVEL
from download_mp3 import download_mp3
from parser_utils import get_cli_argparser
from shazam import shazam_file
from youtube_dl_utils import get_output_filepath, get_video_id


def main():
    """
    parse command line args, call other components
    """

    logging.info("running main()")
    parser = get_cli_argparser()
    args = parser.parse_args()
    youtube_url = args.youtube_url
    video_id = get_video_id(youtube_url)
    logging.info(f"youtube_url: {youtube_url}")

    output_filepath = get_output_filepath(video_id)
    logging.info(f"output_filepath: {output_filepath}")
    
    # main routine here
    if not os.path.isfile(output_filepath):
        logging.info("couldn't find file, downloading from youtube")
        download_mp3(youtube_url)
    else:
        logging.info("found file, skipping download")

    shazam_file(output_filepath, video_id)

if __name__ == "__main__":
    logging.basicConfig(level=LOGGING_LEVEL)
    start_time = time.time()
    main()
    logging.info(f"total runtime: {(time.time() - start_time):.3f} seconds")
