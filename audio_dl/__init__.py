from __future__ import unicode_literals
import youtube_dl
from handlers import get_output, rename_files

def start():
    valid_formats = ["m4a", "mp4", "mp3", "ogg", "wav", "webm"]
    output = get_output(timeout=0)
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
            from handlers import convert_files
            convert_files(invalid_files, fmt)
