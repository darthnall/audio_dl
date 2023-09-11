from __future__ import unicode_literals
import youtube_dl
import os
import datetime
from .rename import rename_all_files

def start():
    valid_formats = ["m4a", "mp4", "mp3", "ogg", "wav", "webm"]
    while True:
        fmt = str(input("Select format: (--list for options)\n"))
        if fmt == "--list":
            print("Options:")
            for i in valid_formats:
                print(f"- {i}")
        elif any(fmt in valid_formats for fmt in valid_formats):
            print(f"Selected format: {fmt}")
            break
        else:
            print("Select a valid format. --list for options.")

    now = datetime.datetime.now().strftime("%Y%m%d_%H%m%s")

    output_dir = f"./output/{now}"
    os.mkdir(output_dir)
    output_dir = os.path.abspath(output_dir) 

    ydl_opts = {
            "format": f"bestaudio[ext={fmt}]/bestaudio/m4a",
            "outtmpl": os.path.join(output_dir, f"%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredquality": "192",
                }],
            }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = str(input("Paste playlist:\n"))
        try:
            ydl.download((url,))
            files = os.listdir(output_dir)
            for file in files:
                ext = file.split('.')[1]
                print(f"Extension: {ext}")
                if ext != fmt:
                    rename_all_files(output_dir=output_dir, fmt=fmt, incorrect_filetype=True)
                else:
                    rename_all_files(output_dir=output_dir, fmt=fmt, incorrect_filetype=False)
        except youtube_dl.DownloadError:
            print("Something went wrong. Try again.")


