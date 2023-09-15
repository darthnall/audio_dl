from __future__ import unicode_literals
import youtube_dl
import os
import ffmpeg
from time import strftime, localtime
from pathlib import Path

def convert_files(files, fmt):
    for file in files:
        ffmpeg.output(ffmpeg.input(file), file, format=fmt)

def rename_files(files):
    for file in files:
        new_name = "_".join(file.strip().lower().split(' '))
        os.rename(file, new_name)
    return os.listdir(".")

# TODO: optimize this function
def mkoutput():
    os.chdir(Path("./output"))
    time = strftime("%Y%M%D-$H$M$S", localtime())
    os.mkdir(time)
    output_path = Path(time)
    output_str = os.fspath(output_path)
    print(output_path, output_str)
    return output_path, output_str

def start():
    valid_formats = ["m4a", "mp4", "mp3", "ogg", "wav", "webm"]
    output = mkoutput()
    while True:
        fmt = input(f"Valid formats: {valid_formats}\nFormat: ")
        if fmt in valid_formats:
            break
        else:
            print("Please select a valid format.")

    ydl_opts = {
            "format": f"bestaudio[ext={fmt}]/bestaudio/m4a",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredquality": "192",
                }],
            }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = str(input("Paste playlist: "))
        ydl.download((url,))

    files = rename_files(output)

    invalid_files = []
    for file in files:
        ext = file.split(".")[-1]
        if ext in valid_formats and ext == fmt:
            pass
        else:
            invalid_files.append(file)

        if invalid_files:
            convert_files(invalid_files, fmt)
