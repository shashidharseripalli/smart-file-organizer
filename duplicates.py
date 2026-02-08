import hashlib
from organizer.logger import logger


def file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


def find_duplicates(files):
    seen = {}
    duplicates = []

    for file in files:
        h = file_hash(file)
        if h in seen:
            duplicates.append(file)
        else:
            seen[h] = file

    return duplicates


def remove_duplicates(files):
    duplicates = find_duplicates(files)
    for file in duplicates:
        file.unlink()
        logger.info(f"Deleted duplicate: {file}")
