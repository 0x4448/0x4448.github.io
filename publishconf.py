import os
import sys

sys.path.insert(0, os.curdir)
from pelicanconf import *  # noqa: E402,F401,F403

SITEURL = "https://0x4448.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
