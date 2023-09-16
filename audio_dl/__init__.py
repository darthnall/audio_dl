from __future__ import unicode_literals
import youtube_dl
from .handlers import ydl_init, clean_up

def start():
    valid_formats = ["m4a", "mp4", "mp3", "ogg", "wav", "webm"]

    while True:
        fmt = input(f"Valid formats: {valid_formats}\nFormat: ")
        if fmt in valid_formats:
            break
        else:
            print("Please select a valid format.")

    output_dir = ydl_init()

    ydl_opts = {
            "format": f"bestaudio[ext={fmt}]/bestaudio/m4a",
            "outmmpl": f"./{output_dir}/%(title)s%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredquality": "192",
                }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download((str(input("Paste playlist: "),)))
        clean_up(output_dir)
