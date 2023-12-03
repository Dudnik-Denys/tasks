from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as archive:
    files = sorted([file for file in archive.infolist() if not file.is_dir()], key=lambda file: file.filename.split('/')[-1])

for file in files:
    print(f'{file.filename.split("/")[-1]}\n'
          f'  Дата модификации файла: {datetime(*file.date_time)}\n'
          f'  Объем исходного файла: {file.file_size} байт(а)\n'
          f'  Объем сжатого файла: {file.compress_size} байт(а)\n')
