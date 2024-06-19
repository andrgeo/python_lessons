from pathlib import Path
from sys import argv

dir_name = argv[1]
home = Path.cwd()

(home / dir_name).mkdir(exist_ok=True)

for f in home.glob('*.txt'):
    path_destination = Path(home / dir_name) / f.name
    f.replace(path_destination)