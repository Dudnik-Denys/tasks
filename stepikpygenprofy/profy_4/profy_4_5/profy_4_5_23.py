from zipfile import ZipFile


def file_size(file_object):
    sizing = 0
    size = file_object.file_size
    sizes = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB'}

    while size / 1024 >= 1:
        sizing += 1
        size /= 1024

    return round(size), sizes[sizing]


tab = '  '

with ZipFile('desktop.zip') as archive:
    files = [file for file in archive.infolist()]
    for file in files:
        if file.is_dir():
            filename = file.filename.split('/')
            if len(filename) <= 2:
                print(filename[-2])
            else:
                print(tab * (len(filename) - 2) + filename[-2])
        else:
            filename = file.filename.split('/')
            print(tab * (len(filename) - 1) + filename[-1], *file_size(file))
