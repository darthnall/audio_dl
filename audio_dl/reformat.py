import ffmpeg

def reformat_all_files(files, fmt):
    for file in files:
        ffmpeg.output(ffmpeg.input(file), file, format=fmt)
