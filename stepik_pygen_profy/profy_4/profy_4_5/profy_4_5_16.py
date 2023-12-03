from zipfile import ZipFile


def compress_power_coefficient(file) -> float:
    return (file.compress_size / file.file_size) * 100


with ZipFile('workbook.zip') as archive:
    files = {compress_power_coefficient(file): file.filename.split('/')[-1] for file in archive.infolist() if not file.is_dir()}

better_coefficient = min(files)
print(files[better_coefficient])
