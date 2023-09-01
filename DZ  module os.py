import os

folder = r"files"
files = []
dirs = []
for item in os.listdir(folder):
    path = os.path.join(folder, item)
    if os.path.isfile(path):
        files.append(path)
    else:
        dirs.append(path)
print(files + dirs)
