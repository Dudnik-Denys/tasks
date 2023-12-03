from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    files = [file for file in zip_file.infolist() if not file.is_dir()]

archived_size = sum([file.compress_size for file in files])
unarchived_size = sum([file.file_size for file in files])

print(f'Объем исходных файлов: {unarchived_size} байт(а)\n'
      f'Объем сжатых файлов: {archived_size} байт(а)')
