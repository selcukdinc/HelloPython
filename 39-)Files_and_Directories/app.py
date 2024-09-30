from pathlib import Path
# Absolute path
# C:\Program Files\Microsoft
# /usr/local/bin
# Relative path

path = Path()
# path.exists() = check path exists
# path.mkdir() = create new directory
# path.rmdir() = remove directory
# path.glob('*.*') = search all directories and type of files  |
#       path.glob('*.py') search only .py files in all directories
#       returns 'generator object'

for file in path.glob('*'):
    print(file)

