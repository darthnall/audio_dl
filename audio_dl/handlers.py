import ffmpeg, os
from time import strftime, localtime

def ydl_init():
    time = strftime("%H%M%S", localtime())
    os.mkdir(time)
    output_dir = os.fspath(time)
    return output_dir

def progress_hooks(p, file):
    if p["status"] == "downloading":
        pass
    if p["status"] == "finished":
        rename_file(file)

def rename_file(file):
    new_name = "_".join(file.strip().lower().split(' '))
    os.rename(file, new_name)
    return new_name
