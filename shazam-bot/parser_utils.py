"""parser utils for CLI"""

import argparse


def get_cli_argparser():
    """get parser for CLI arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--youtube_url",
        type=str,
        help="URL of youtube video to ID",
        required=True,
    )

    return parser
