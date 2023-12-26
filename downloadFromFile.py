from yt_dlp import YoutubeDL
import sys

ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
    'verbose': 'true',
    'paths': {
        'home': './music'
    }
}

if len( sys.argv ) <= 1:
    f = open("links.txt", "r")
    URLS = f.readlines()
else:
    URLS = [sys.argv[1]]

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)

if 'f' in locals():
    f.close()
