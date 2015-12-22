# anifs

Anime File Sorter Library

## Installation

Create a virtual environment with Python 3 using virtualenv. 
Activate the virtualenv and download the requirement list 
(replace user with your own GitHub user name):

    curl -L -O https://github.com/katthjul/anifs/raw/master/requirements.txt

Install anifs and its dependencies by:

    pip install -r requirements.txt

## Development

Clone this repository to a suitable location.
Generate a new requirements.txt with anifs in editable mode:

    ./make_reqs requirements.txt /path/to/git/repos > reqs-dev.txt

Create a virtual environment with Python 3 using virtualenv. 
Activate the virtualenv and install anifs:

    pip install -r /path/to/reqs-dev.txt

Any changes in the local repo will now be available in the virtualenv.
