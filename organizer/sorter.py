import shutil
from pathlib import Path
from organizer.logger import logger


def get_category(ext, categories):
    for name, exts in categories.items():
        if ext.lower() in exts:
            return name
    return "Others"


def move_file(path: Path, base_folder, categories):
    if not path.exists():
        return

    category = get_category(path.suffix, categories)

    target_folder = base_folder / category
    target_folder.mkdir(exist_ok=True)

    new_path = target_folder / path.name

    counter = 1
    while new_path.exists():
        new_path = target_folder / f"{path.stem}_{counter}{path.suffix}"
        counter += 1

    shutil.move(str(path), str(new_path))
    logger.info(f"Moved {path} → {new_path}")
