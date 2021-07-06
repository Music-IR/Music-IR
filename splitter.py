import os
from spleeter.separator import Separator
import urllib.request


def downloader(url: str, path: str):
    if not os.path.isfile(path):
        with urllib.request.urlopen(url) as f:
            with open(path, 'wb') as output:
                output.write(f.read())


if __name__ == '__main__':
    file_url = "https://github.com/deezer/spleeter/raw/master/audio_example.mp3"
    download_path = "output/test.mp3"
    downloader(file_url, download_path)
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(download_path, "output/")
