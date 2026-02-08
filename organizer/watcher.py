import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from organizer.sorter import move_file
from organizer.config_loader import load_config
from organizer.logger import logger


class Handler(FileSystemEventHandler):

    def __init__(self):
        self.base, self.categories, self.remove_dups = load_config()

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        move_file(file_path, self.base, self.categories)


def start():
    base, _, _ = load_config()

    observer = Observer()
    observer.schedule(Handler(), str(base), recursive=False)
    observer.start()

    logger.info("Started watching folder")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
