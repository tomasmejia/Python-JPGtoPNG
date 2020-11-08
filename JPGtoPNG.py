import sys
from pathlib import Path
from PIL import Image


# get first and second arg
image_folder = Path(sys.argv[1])
output_folder = Path(sys.argv[2])

if not image_folder.exists():
    raise FileNotFoundError("Image folder doesn't exist")

if not output_folder.exists():
    Path.mkdir(output_folder)

for filename in Path(image_folder).iterdir():
    img = Image.open(filename)
    img.save(f'{output_folder}/{filename.stem}.png', 'png')
    print(f'{filename.name} -> All done!')
