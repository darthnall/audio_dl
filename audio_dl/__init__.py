from __future__ import unicode_literals
import youtube_dl
import os
from time import localtime, strftime
from .reformat import convert_files

def start():
    out = os.open("./audio_dl/output", os.O_RDONLY)
    valid_formats = ["mp4", "mp3", "ogg", "wav"]
    while True:
        fmt = str(input(f"Available formats: {valid_formats}\nSelect format: "))
        if fmt in valid_formats:
            break
        else:
            print("Select a valid format. --list for options.")

    time = strftime("%Y%M%D-$H$M$S", localtime())
    output_dir = os.mkdir(f"{time}", dir_fd=out)

    ydl_opts = {
            "format": "bestaudio",
            "output": output_dir,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": fmt,
                "preferredquality": "192",
                }],
            }

    #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #    url = str(input("Paste playlist: "))
    #    ydl.download((url,))

    files = os.listdir(output_dir)

    for file in files:
        invalid_files = []

        old_name = file.strip().lower().split(' ')
        new_name = '_'.join(old_name)
        os.rename(file, new_name)

        ext = file.split(".")[1]
        if ext in valid_formats and ext == fmt:
            pass
        else:
            invalid_files.append(file)

        if invalid_files:
            convert_files(invalid_files)
