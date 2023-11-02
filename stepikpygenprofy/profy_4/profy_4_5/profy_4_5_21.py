from zipfile import ZipFile


def extract_this(zip_name: str, *args):
    with ZipFile(zip_name) as archive:
        if args:
            [archive.extract(file) for file in archive.infolist() if file.filename.split('/')[-1] in args]
        else:
            archive.extractall()


extract_this('workbook.zip', 'earth.jpg')
