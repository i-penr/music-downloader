from yt_dlp import YoutubeDL

f = open("links.txt", "r")
URLS = f.readlines()

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

with YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)

f.close()