import os
from audio_dl.reformat import reformat_all_files

def rename_all_files(output_dir, fmt, incorrect_filetype):
    files = os.listdir(output_dir)

    for file in files:
        old_path = os.path.join(output_dir, file)
        new_name = file.strip().lower().replace(' ', '_')
        new_path = os.path.join(output_dir, new_name)
        os.rename(old_path, new_path)
        if incorrect_filetype:
            files = os.listdir(output_dir)
            print("Some files were not downloaded with the correct format. . .\nReformatting . . .")
            reformat_all_files(files=files, fmt=fmt)
        else:
            pass
