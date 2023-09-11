import os

files = os.listdir('.')

for file in files:
    old_name = file.strip().lower().split(' ')
    new_name = '_'.join(old_name)
    os.rename(file, new_name)
