from spleeter.separator import Separator
from analyzer import utils

if __name__ == '__main__':
    file_url = "https://github.com/deezer/spleeter/raw/master/audio_example.mp3"
    download_path = "output/test.mp3"
    utils.downloader(file_url, download_path)
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(download_path, "output/")
