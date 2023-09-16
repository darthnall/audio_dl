import ffmpeg, os
from time import strftime, localtime

valid_formats = ["m4a", "mp4", "mp3", "ogg", "wav", "webm"]

def make_output_dir():
    time = strftime("%H%M%S", localtime())
    os.mkdir(time)
    start = os.path.getmtime(time)
    print(start) # Print line
    return start

def convert_file(file, fmt):
    pass

def find_files(time):
    pass

def clean_up(files, fmt):
    for file in files:
        new_name = "_".join(file.strip().lower().split(' '))
        os.rename(file, new_name)
        if file.split(".") != fmt:
            convert_file(file, fmt)
