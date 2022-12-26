import os
from os import listdir
from os.path import isfile, join


def rename_file(filename):
    old_name = filename
    new_name = old_name.replace('[YT2mp3.info] - ', '').replace('(320kbps)', '').strip()
    new_name, music_format = new_name.split('.')[0], new_name.split('.')[1]
    new_name = f'{new_name.strip()}.{music_format}'
    print(old_name, '->', new_name)
    os.rename(f'{source}\\{old_name}', f'{source}\\{new_name}')


# https://320ytmp3.info/
root = os.path.dirname(os.path.abspath(__file__))
folder = 'folder'
source = f'{root}\\{folder}'

onlyfiles = [f for f in listdir(source) if isfile(join(source, f))]
print(onlyfiles)

for file in onlyfiles:
    rename_file(file)
