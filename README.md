# music-downloader
Very simple python script that downloads music from youtube from a list of URLs using ytdlp.

# How does it work
Simply add the youtube links to the `links.txt` file (one link per line) and execute the python script (`downloadFromFile.py`). The mp3 should be downloaded in a new created folder called `music`.

# Dependencies
This script uses the [ytdlp](https://pypi.org/project/yt-dlp/) package. To install it, run the following program (using `pip`):

```bash
pip install yt_dlp
```

This script also uses [ffmpeg](https://ffmpeg.org/). To install it, run the following command (with `apt`):

```bash
sudo apt install ffmpeg
```
