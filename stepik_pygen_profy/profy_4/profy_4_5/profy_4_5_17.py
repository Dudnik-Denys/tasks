from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as archive:
    files = {file.filename.split('/')[-1]: datetime(*file.date_time) for file in archive.infolist() if not file.is_dir()}

starting_point = datetime(2021, 11, 30, 14, 22, 0)

[print(data[0]) for data in sorted(files.items()) if data[1] > starting_point]
