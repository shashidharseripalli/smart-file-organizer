# Smart File Organizer

A real-time file automation system that automatically monitors a folder, categorizes files by type, removes duplicates, and organizes everything in the background.

Built using Python, Watchdog, and Streamlit.

---

## Problem

Folders like Downloads/Desktop quickly become messy.

Manually sorting files wastes time.

This tool automates that process completely.

Drop files → auto organized.

---

## Features

- Real-time folder monitoring
- Automatic file categorization
- Duplicate file removal
- Background service
- Streamlit dashboard
- Configurable rules (JSON)
- Logging for debugging

---

## Demo Behavior

When files are added:
a.txt       → Documents/ photo.jpg   → Images/ video.mp4   → Videos/ code.py     → Code/ file.zip    → Archives/ unknown.xyz → Others/

Everything is sorted automatically within seconds.

---

## Project Structure
smart-file-organizer/ │ ├── organizer/       
# Core automation logic ├── dashboard/        
# Streamlit dashboard UI ├── main.py           
# CLI runner ├── config.json       
# Settings ├── requirements.txt ├── README.md ├── .gitignore

---

## Tech Stack

- Python
- Watchdog
- Streamlit
- Logging

---

## Installation

Clone repo:

```bash
git clone https://github.com/<your-username>/smart-file-organizer.git
cd smart-file-organizer

Install dependencies:
pip install -r requirements.txt
Run
Dashboard (recommended)
streamlit run dashboard/app.py

Terminal only
python main.py

Configuration
Edit config.json:
{
  "watch_folder": "AutoSort",
  "remove_duplicates": true
}

```
Customize:
-folders
-extensions
-categories

Why This Project Matters
This demonstrates:
#OS automation
#Event-driven systems
#File handling
#Background services
#Real-world Python engineering
#Not a toy script — a practical automation tool.


Future Improvements
#Multiple folder support
#File stats dashboard
#System tray app
#Packaging as .exe
#ML-based file classification 


