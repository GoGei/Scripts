import os
from os import listdir
from os.path import isfile, join
from PIL import Image

root = os.path.dirname(os.path.abspath(__file__))
allowed_extensions = ['png', 'jpg']
folder = 'initial'
source = f'{root}\\{folder}'

onlyfiles = [f for f in listdir(source) if isfile(join(source, f)) and f.split('.')[-1] in allowed_extensions]
print(onlyfiles)

target_folder = 'converted'
size = 512, 512

for file in onlyfiles:
    im = Image.open(source + f'\\{file}')
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(f'{root}\\{target_folder}\\{file.split(".")[0]}.png')
