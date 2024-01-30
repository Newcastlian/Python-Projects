import os
import shutil
from pathlib import Path

def organize_text_files():
    desktop_path = Path(os.path.expanduser("~/Desktop"))
    txt_folder_path = desktop_path / "TextFiles"

    # Create a folder named TextFiles if it doesn't exist
    txt_folder_path.mkdir(exist_ok=True)

    # Get a list of text files on the desktop
    txt_files = [f for f in desktop_path.iterdir() if f.is_file() and f.suffix.lower() == ".txt"]

    # Move each text file to the TextFiles folder
    for txt_file in txt_files:
        destination = txt_folder_path / txt_file.name
        shutil.move(str(txt_file), str(destination))
        print(f"Moved {txt_file.name} to {destination}")

def organize_folder_files():
    desktop_path = Path(os.path.expanduser("~/Desktop"))
    folder_files_path = desktop_path / "FolderFiles"

    # Create a folder named FolderFiles if it doesn't exist
    folder_files_path.mkdir(exist_ok=True)

    # Get a list of folders on the desktop (excluding the target FolderFiles folder)
    folders = [f for f in desktop_path.iterdir() if f.is_dir() and f.name not in ["FolderFiles", "TextFiles", "Applications"]]

    # Move each folder to the FolderFiles folder
    for folder in folders:
        destination = folder_files_path / folder.name
        destination.mkdir(exist_ok=True)  # Create destination folder if it doesn't exist
        shutil.move(str(folder), str(destination))
        print(f"Moved {folder.name} to {destination}")

def organize_applications():
    desktop_path = Path(os.path.expanduser("~/Desktop"))
    applications_folder_path = desktop_path / "Applications"

    # Create a folder named Applications if it doesn't exist
    applications_folder_path.mkdir(exist_ok=True)

    # Get a list of executable files on the desktop
    applications = [f for f in desktop_path.iterdir() if f.is_file() and f.suffix.lower() in [".exe", ".lnk", ".url"]]

    # Move each application to the Applications folder
    for app in applications:
        destination = applications_folder_path / app.name
        shutil.move(str(app), str(destination))
        print(f"Moved {app.name} to {destination}")

if __name__ == "__main__": 
    organize_text_files()
    organize_applications()
    organize_folder_files()
