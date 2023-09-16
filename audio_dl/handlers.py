import ffmpeg, os
from time import strftime, localtime

valid_formats = ["m4a", "mp4", "mp3", "ogg", "wav", "webm"]

def ydl_init():
    time = strftime("%H%M%S", localtime())
    os.mkdir(time)
    output_dir = os.fspath(time)
    return output_dir

def convert_file(file, fmt):
    pass

def clean_up(output_dir, fmt):
    files = os.listdir(output_dir)
    for file in files:
        new_name = "_".join(file.strip().lower().split(' '))
        os.rename(file, new_name)
        if file.split(".") != fmt:
            convert_file(file, fmt)
