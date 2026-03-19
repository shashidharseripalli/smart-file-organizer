from pathlib import Path

STATS_FILE = Path("logs/stats.txt")


def increment_counter():
    STATS_FILE.parent.mkdir(exist_ok=True)

    if not STATS_FILE.exists():
        STATS_FILE.write_text("0")

    count = int(STATS_FILE.read_text())
    STATS_FILE.write_text(str(count + 1))


def get_count():
    if not STATS_FILE.exists():
        return 0

    return int(STATS_FILE.read_text())


def reset():
    STATS_FILE.write_text("0")