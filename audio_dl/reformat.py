from ffmpeg import FFmpeg
import os

def reformat_all_files(files, fmt):
    for file in files:
        output_dir = os.path.abspath(file).split("/").pop()
        output_dir = "/".join(output_dir)
        filename = file.split(".")[0]
        ffmpeg = (
                FFmpeg()
                .input(file)
                .output(
                    f"{output_dir}/{filename}.{fmt}",
                    )
                )
        ffmpeg.execute()
