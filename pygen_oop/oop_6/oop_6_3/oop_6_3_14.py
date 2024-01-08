def non_closed_files(files: list):
    return [file for file in files if not file.closed]
