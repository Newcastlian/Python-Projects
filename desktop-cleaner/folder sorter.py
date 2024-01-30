import os
import shutil
from pathlib import Path

def organize_folder_files():
    desktop_path = Path(os.path.expanduser("~/Desktop"))
    folder_files_path = desktop_path / "FolderFiles"

    # Create a folder named FolderFiles if it doesn't exist
    folder_files_path.mkdir(exist_ok=True)

    # Get a list of folders on the desktop (excluding the target FolderFiles folder)
    folders = [f for f in desktop_path.iterdir() if f.is_dir() and f.name != ["FolderFiles","TextFiles","Applications"]]

    # Move each folder to the FolderFiles folder
    for folder in folders:
        destination = folder_files_path / folder.name
        destination.mkdir(exist_ok=True)  # Create destination folder if it doesn't exist
        shutil.move(str(folder), str(destination))
        print(f"Moved {folder.name} to {destination}")

if __name__ == "__main__":
    organize_folder_files()
