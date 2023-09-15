from __future__ import unicode_literals
import youtube_dl
import os
from time import strftime, localtime
from .reformat import convert_files

def rename(files, out):
    for file in files:
        old_name = file.strip().lower().split(' ')
        new_name = '_'.join(old_name)
        os.rename(file, new_name)
    return os.listdir(out)


def start():
    valid_formats = ["m4a", "mp4", "mp3", "ogg", "wav", "webm"]
    out = os.open("./output", os.O_RDONLY)
    print(out)
    while True:
        fmt = input(f"Valid formats: {valid_formats}\nFormat: ")
        if fmt in valid_formats:
            break
        else:
            print("Please select a valid format.")

    time = strftime("%Y%M%D-$H$M$S", localtime())
    output_dir = os.mkdir(f"{time}", dir_fd=out)

    ydl_opts = {
            "format": f"bestaudio[ext={fmt}]/bestaudio/m4a",
            "outtmpl": output_dir,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredquality": "192",
                }],
            }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = str(input("Paste playlist: "))
        ydl.download((url,))

    files = os.listdir(output_dir)
    files = rename(files, out)

    invalid_files = []
    for file in files:
        ext = file.split(".")[-1]
        if ext in valid_formats and ext == fmt:
            pass
        else:
            invalid_files.append(file)

        if invalid_files:
            convert_files(invalid_files, fmt)
