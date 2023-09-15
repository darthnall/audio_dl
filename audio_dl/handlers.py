import ffmpeg, os
from time import strftime, localtime
from sys import exit
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
def get_output(timeout):
    if os.chdir("./output") and timeout <= 3:
        time = strftime("%Y%M%D-$H$M$S", localtime())
        os.mkdir(time)
        output_path = Path(time)
        output_str = os.fspath(output_path)
        print(output_path, output_str)
        return output_path, output_str
    else:
        create_output(timeout=timeout)

def create_output(timeout=0):
    if timeout >= 3:
        exit("Creating output directory timed out. Make sure you have an output directory.")
    os.mkdir("./output")
    os.chdir("./output")
    get_output(timeout=timeout+1)
