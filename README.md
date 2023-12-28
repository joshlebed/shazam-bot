## shazam this set

NOTE: DEPRECATED. THIS REPO HAS BEEN ROLLED INTO [lib-sync](https://github.com/clobraico22/lib-sync)

uses:

https://github.com/Numenorean/ShazamAPI

install ffmpeg and ffprobe first:

```bash
brew install ffmpeg  # mac
```










## user guide

### prereqs

- [python 3.10](https://www.python.org/downloads/release/python-31010/) installed locally

### steps

- in this directory, run:

```bash
python3.10 -m venv .venv  # create python virtual environment
source .venv/bin/activate  # activate virtual environment
pip install -r requirements.txt  # install dependencies

# run script
python shazam.py [input_file] \
-l \
-s \
```

## dev quickstart

one time setup:

```bash
python3.10 -m venv .venv
```

activate python virtual environment and update dependencies (after each pull):

```bash
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

```bash
# run script
python shazam.py [input_file] \
-l \
-s \

# run mp3 downloader
python download_mp3.py
```

## TODO:

switch this to python3.7 so that tempocnn can be used for tempo data
- rewrite shazam library to be multithreaded and much faster
- add this to fb messenger bot
