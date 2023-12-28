import argparse
import logging
import os
import pickle
import time
import traceback
from datetime import timedelta
from pathlib import Path

from ShazamAPI import Shazam

# URLS_IN_TIMESTAMP_ORDER_FILEPATH = "urls_in_timestamp_order.pickle"
# matches_by_url_filepath = "matches_by_url.pickle"


# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("input_file")
#     parser.add_argument("-s", "--save_matches_to_pickle", action="store_true")
#     parser.add_argument("-l", "--load_matches_from_pickle", action="store_true")
#     args = parser.parse_args()
#     input_file_path = Path(args.input_file)
#     save_matches_to_pickle = args.save_matches_to_pickle
#     load_matches_from_pickle = args.load_matches_from_pickle
#     # shazam_file(input_file_path, save_matches_to_pickle, load_matches_from_pickle)


def shazam_file(input_file_path, video_id):
    save_matches_to_pickle = True

    urls_in_timestamp_order_filepath = f"{video_id}_urls_in_timestamp_order.pickle"
    matches_by_url_filepath = f"{video_id}_matches_by_url.pickle"

    load_matches_from_pickle = False
    if not (
        os.path.isfile(urls_in_timestamp_order_filepath)
        and os.path.isfile(matches_by_url_filepath)
    ):
        logging.info("no cache found, shazaming")
        load_matches_from_pickle = False
    else:
        logging.info("found cache, skipping download")
        load_matches_from_pickle = True

    start_time = time.time()
    input_file = open(input_file_path, "rb").read()

    shazam = Shazam(input_file)
    recognize_generator = shazam.recognizeSong()

    matches_by_url = {}
    urls_in_timestamp_order = []

    while True and not load_matches_from_pickle:
        try:
            result = next(recognize_generator)
            timestamp = timedelta(seconds=result[0])
            details = result[1]
            if len(details["matches"]) >= 1:
                track = details["track"]
                subtitle = track["subtitle"]
                title = track["title"]
                url = track["url"]
                if url not in matches_by_url:
                    urls_in_timestamp_order.append(url)
                    print(f"{str(timestamp)} {subtitle:40} - {title:80} {url}")
                    matches_by_url[url] = {
                        "timestamps": [timestamp],
                        "subtitle": subtitle,
                        "title": title,
                    }
                else:
                    matches_by_url[url]["timestamps"].append(timestamp)

        except StopIteration as _:
            print("reached end of file.")
            break

        except Exception as _:
            logging.error(traceback.format_exc())

    end_time = time.time()
    print(f"done shazaming. elapsed time: {end_time - start_time}")

    if load_matches_from_pickle:
        with open(urls_in_timestamp_order_filepath, "rb") as pickle_file:
            urls_in_timestamp_order = pickle.load(pickle_file)
        with open(matches_by_url_filepath, "rb") as pickle_file:
            matches_by_url = pickle.load(pickle_file)

    if save_matches_to_pickle:
        with open(urls_in_timestamp_order_filepath, "wb") as pickle_file:
            pickle.dump(urls_in_timestamp_order, pickle_file)
        with open(matches_by_url_filepath, "wb") as pickle_file:
            pickle.dump(matches_by_url, pickle_file)

    for url in urls_in_timestamp_order:
        match = matches_by_url[url]
        num_matches = len(match["timestamps"])
        timestamp = match["timestamps"][0]
        subtitle = match["subtitle"]
        title = match["title"]
        if num_matches >= 3:
            print(f"{num_matches:3} {str(timestamp)} {subtitle:30} - {title:50} {url:20}")
