from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    files = [file for file in zip_file.infolist() if not file.is_dir()]

print(len(files))
