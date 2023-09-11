from __future__ import unicode_literals
import youtube_dl
import os
from datetime import datetime

def start():
    valid_formats = ["mp4", "mp3", "ogg", "wav"]
    while True:
        fmt = str(input("Select format: (--list for options)\n"))
        if fmt == "--list":
            print("Options:")
            for i in valid_formats:
                print(f"- {i}")
        elif any(fmt in valid_formats for fmt in valid_formats):
            break
        else:
            print("Select a valid format. --list for options.")

    output_dir = os.path.abspath(os.mkdir(f"./output/{datetime}"))

    ydl_opts = {
            "format": "bestaudio",
            "output": output_dir,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": fmt,
                "preferredquality": "192",
                }],
            }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = str(input("Paste playlist:\n"))
        ydl.download((url,))

    files = os.listdir(output_dir)

    for file in files:
        old_name = file.strip().lower().split(' ')
        new_name = '_'.join(old_name)
        os.rename(file, new_name)
