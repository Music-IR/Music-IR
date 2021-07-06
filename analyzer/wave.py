from spleeter.audio.adapter import AudioAdapter
from spleeter.separator import Separator

from analyzer import utils


def get_waveform(path: str):
    audio_loader = AudioAdapter.default()
    sample_rate = 44100
    waveform, _ = audio_loader.load(path, sample_rate=sample_rate)
    return waveform, audio_loader


if __name__ == '__main__':
    file_url = "https://github.com/deezer/spleeter/raw/master/audio_example.mp3"
    download_path = "output/test.mp3"
    utils.downloader(file_url, download_path)
    separator = Separator('spleeter:2stems')
    waveform, loader = get_waveform(download_path)
    print(waveform.shape)
    predictions = separator.separate(waveform)
    print(predictions["vocals"].shape)

