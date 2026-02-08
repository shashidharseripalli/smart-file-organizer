import sys
from pathlib import Path
import streamlit as st
import threading

# allow imports from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from organizer.watcher import start
from organizer.config_loader import load_config

st.title("Smart File Organizer")

watch_folder, _, _ = load_config()
st.write(f"Monitoring folder: {watch_folder}")


def run():
    start()


if st.button("Start Organizer"):
    threading.Thread(target=run, daemon=True).start()
    st.success("Organizer running in background")


log_file = Path("../logs/organizer.log")

if log_file.exists():
    logs = log_file.read_text().splitlines()
    st.subheader("Recent Logs")
    st.text("\n".join(logs[-25:]))
