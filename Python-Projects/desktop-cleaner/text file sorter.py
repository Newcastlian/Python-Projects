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

if __name__ == "__main__": 
    organize_text_files()
