import ffmpeg, os
from time import strftime, localtime
from sys import exit
from pathlib import Path

def convert_files(files, fmt):
    for file in files:
        pass

def rename_files(files):
    for file in files:
        new_name = "_".join(file.strip().lower().split(' '))
        os.rename(file, new_name)
    return os.listdir(".")

# TODO: optimize this function
def get_output():
    time = strftime("%H%M%S", localtime())
    timeout = 0

    while timeout >= 3:
        try:
            os.chdir("./output")
        except FileNotFoundError:
            os.mkdir("./output")
            os.chdir("./output")
        finally:
            timeout =+ 1

    os.mkdir(time)
    output_path = Path(time)
    output_str = os.fspath(output_path)

    print(output_path, output_str) # TODO: Remove this when optimized
    return output_path, output_str
