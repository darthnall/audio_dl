from __future__ import unicode_literals
import youtube_dl
from .handlers import make_output_dir
from .handlers import clean_up
from .handlers import valid_formats

def start():

    while True:
        fmt = input(f"Valid formats: {valid_formats}\nFormat: ")
        if fmt in valid_formats:
            break
        else:
            print("Please select a valid format.")

    output_dir = make_output_dir()

    ydl_opts = {
            "format": f"bestaudio[ext={fmt}]/bestaudio/m4a",
            "outmmpl": "%(title)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredquality": "192",
                }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = str(input("Paste playlist: "))
        ydl.download((url,))

    clean_up(output_dir, fmt=fmt)
