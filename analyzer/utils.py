import os
import urllib.request
from pathlib import Path


def downloader(url: str, path: str):
    if not os.path.isfile(path):
        parent = Path(path).parent
        if not parent.exists():
            os.makedirs(parent)
        with urllib.request.urlopen(url) as f:
            with open(path, 'wb') as output:
                output.write(f.read())
